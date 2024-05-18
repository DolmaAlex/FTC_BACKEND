from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import DB_USER, DB_PASS, DB_HOST, DB_NAME

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_db_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


async def create_db_tables():
    from app.models import Base  # корректируем путь импорта в соответствии с вашей структурой проекта
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
