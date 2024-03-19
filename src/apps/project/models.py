from sqlalchemy import JSON, UUID, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db.db_base import Base
from src.core.utils.func import get_random_uuid


class Project(Base):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    desc: Mapped[str] = mapped_column(String(200), nullable=True)
    tags: Mapped[JSON] = mapped_column(JSON, nullable=True)
    unique_id: Mapped[UUID] = mapped_column(
        UUID, unique=True, nullable=False, default=get_random_uuid
    )
