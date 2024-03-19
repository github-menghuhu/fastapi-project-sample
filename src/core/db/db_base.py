from datetime import datetime

from sqlalchemy import Boolean, DateTime
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.core.domain.settings import (
    IS_PRINT_SQL,
    POSTGRESQL_HOST,
    POSTGRESQL_NAME,
    POSTGRESQL_PASSWORD,
    POSTGRESQL_PORT,
    POSTGRESQL_USER,
)

DATABASE_URL = f"postgresql+asyncpg://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_NAME}"
engine = create_async_engine(DATABASE_URL, echo=IS_PRINT_SQL, future=True)
async_session_maker = async_sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(AsyncAttrs, DeclarativeBase):
    is_delete: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now
    )
    updated_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )
