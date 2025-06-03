from fastapi import APIRouter, HTTPException, Query
from typing import List
import crud
from schema import CVESchema
from logger import Logger
logger = Logger()

router = APIRouter()

@router.get("/list", response_model=List[CVESchema])
async def list_cves(
    page: int = Query(0, ge=0, description="Start index for pagination"),
    limit: int = Query(10, ge=1, le=10000, description="Max results per page (1-100)")
):
    logger.info(f"Fetching CVEs with pagination: page={page}, limit={limit}")
    cves = await crud.get_cves(skip=page, limit=limit)
    return cves

@router.get("/{cve_id}", response_model=CVESchema)
async def get_cve(cve_id: str):
    logger.info(f"Fetching CVE with ID: {cve_id}")
    cve = await crud.get_cve_by_id(cve_id)
    if not cve:
        raise HTTPException(status_code=404, detail="CVE not found")
    return cve