import asyncio
import httpx
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from db import async_session
from models import CVE
import datetime
from logger import Logger
logger = Logger()
from fake_useragent import UserAgent
import time


BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
RESULTS_PER_PAGE = 2000

def normalize_date(date_str: str) -> str:
    try:
        dt = datetime.datetime.fromisoformat(date_str.replace("Z", ""))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return date_str

async def fetch_page(client: httpx.AsyncClient, start_index: int) -> dict:
    url = f"{BASE_URL}?startIndex={start_index}&resultsPerPage={RESULTS_PER_PAGE}"
    response = await client.request("GET",url, timeout=60,headers={"User-Agent": UserAgent().random})
    return response

async def process_cve(session: AsyncSession, cve_data: dict):
    c = cve_data.get("cve", {})
    cve_id = c.get("id")
    if not cve_id:
        return

    existing = await session.execute(select(CVE).where(CVE.cve_id == cve_id))
    if existing.scalar():
        return  

    descs = c.get("descriptions", [])
    en_desc = next((d["value"] for d in descs if d["lang"] == "en"), "")

    metrics = c.get("metrics", {})
    cvss_v2_metrics = metrics.get("cvssMetricV2", [])
    metric = cvss_v2_metrics[0] if cvss_v2_metrics else {}
    cvss_data = metric.get("cvssData", {}) 
    identifier = c.get("sourceIdentifier")
    published_date = normalize_date(c.get("published"))
    last_modified_date = normalize_date(c.get("lastModified"))
    status = c.get("vulnStatus", "Unknown")

    cpes = []
    for config in c.get("configurations", []):
        for node in config.get("nodes", []):
            for cpe_match in node.get("cpeMatch", []):
                cpes.append({
                    "matchCriteriaId": cpe_match.get("matchCriteriaId"),
                    "criteria": cpe_match.get("criteria"),
                    "vulnerable": cpe_match.get("vulnerable")
                })

    cve_record = CVE(
        cve_id=cve_id,
        description=en_desc,
        identifier=identifier,
        published=published_date,
        lastmodified=last_modified_date,
        status=status,
        severity=metric.get("baseSeverity"),
        base_score=cvss_data.get("baseScore"),
        vector_string=cvss_data.get("vectorString"),
        exploitability_score=metric.get("exploitabilityScore"),
        impact_score=metric.get("impactScore"),
        access_vector=cvss_data.get("accessVector"),
        attack_complexity=cvss_data.get("accessComplexity"),
        authentication=cvss_data.get("authentication"),
        confidentiality_impact=cvss_data.get("confidentialityImpact"),
        integrity_impact=cvss_data.get("integrityImpact"),
        availability_impact=cvss_data.get("availabilityImpact"),
        cpes=cpes or [{}],
    )
    session.add(cve_record)

async def fetch_and_store_cves():
    async with httpx.AsyncClient(verify=False, proxy="http://localhost:8080") as client:
        res = await client.request("GET",f"{BASE_URL}?resultsPerPage=1", headers={"User-Agent": UserAgent().random}, timeout=60)
        total = res.json().get("totalResults", 0)
        logger.info(f"Total CVEs to fetch: {total}")

        start_indices = list(range(0, total, RESULTS_PER_PAGE))

        for start_index in start_indices:
            logger.info(f"Fetching CVEs starting at index: {start_index}")
            time.sleep(3) # Rate limiting to avoid overwhelming the API
            response = await fetch_page(client, start_index)
            if response.status_code != 200:
                logger.error(f"Failed to fetch CVEs at index {start_index}: {response.status_code}")
                continue
            page_data = response.json()
            async with async_session() as session:
                async with session.begin():
                    for vuln in page_data.get("vulnerabilities", []):
                        await process_cve(session, vuln)
            logger.info(f"Processed CVEs from index {start_index} to {start_index + RESULTS_PER_PAGE}")

    logger.info("Finished fetching and storing CVEs")