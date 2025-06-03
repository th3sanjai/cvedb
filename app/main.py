from fastapi import FastAPI
from api import router as api_router
from logger import Logger
from cli import CLI
from help import Helper
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from db import create_db_and_tables
from fetch import fetch_and_store_cves
import uvicorn
import asyncio

logger = Logger()

app = FastAPI(
    docs_url="/docs",            
    redoc_url=None,              
    openapi_url="/openapi.json"  
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_frontend():
    logger.info("Serving frontend for initial request")
    return FileResponse("static/index.html")

app.include_router(api_router, prefix="/api/cves")


async def setup():
    logger.info("Setting up the database and fetching CVEs, this may take a while...")
    await create_db_and_tables()
    await fetch_and_store_cves()
    
def main():
    cli = CLI()
    args = cli.cli()
    if args.help:
        helper = Helper()
        helper.help()
        return

    if args.setup_db:
        logger.info("Setting up the database schema...")
        asyncio.run(setup())
        return
    
    logger.info(f"Starting CVEDB api server on {args.host}:{args.port} with reload={args.reload}")
    uvicorn.run(
        "main:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level="info"
    )

if __name__ == "__main__":
    main()
