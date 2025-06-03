from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from logger import Logger
logger = Logger()

confiloader = Config()
DATABASE_URL = f"sqlite+aiosqlite:///{confiloader.config_db_path()}" 

engine = create_async_engine(DATABASE_URL, echo=False)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def create_db_and_tables():
    async with engine.begin() as conn:
        logger.info("Creating database tables if they do not exist")
        await conn.run_sync(Base.metadata.create_all)