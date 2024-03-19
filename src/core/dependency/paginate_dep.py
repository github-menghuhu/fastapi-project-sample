from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.domain.schemas_base import Pagination


async def paginate(db: AsyncSession, query: Select, page: int, size: int) -> Pagination:
    query_list = await db.execute(query.limit(size).offset((page - 1) * size))
    total = await db.scalar(
        # pylint: disable=not-callable
        select(func.count()).select_from(query.subquery())
    )
    return Pagination(
        total=total if total else 0,
        page=page,
        size=size,
        items=query_list.scalars().all(),
    )
