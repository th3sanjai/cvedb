from sqlalchemy.future import select
from sqlalchemy import func
from models import CVE
from db import async_session
from logger import Logger
logger = Logger()

async def get_cves(skip: int = 0, limit: int = 10):
    async with async_session() as session:
        logger.info(f"Fetching CVEs with skip={skip}, limit={limit} from database")
        result = await session.execute(select(CVE).offset(skip).limit(limit))
        return result.scalars().all()

async def get_cve_by_id(cve_id: str):
    async with async_session() as session:
        logger.info(f"Fetching CVE with ID: {cve_id} from database")
        result = await session.execute(select(CVE).where(CVE.cve_id == cve_id))
        return result.scalar_one_or_none()

async def count_cves():
    async with async_session() as session:
        logger.info("Counting total number of CVEs in the database")
        result = await session.execute(select(func.count()).select_from(CVE))
        return result.scalar()
