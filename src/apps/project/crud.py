from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependency.paginate_dep import paginate
from src.core.domain.schemas_base import Pagination

from .models import Project


async def create_project(
    db: AsyncSession, name: str, desc: str | None = None, tags: list | None = None
) -> Project:
    """
    数据层
    :param db:
    :param name:
    :param desc:
    :param tags:
    :return:
    """
    project = Project(name=name, desc=desc, tags=tags)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project


async def query_project_list(db: AsyncSession, page: int, size: int) -> Pagination:
    sql = select(Project).order_by(Project.id.desc())
    return await paginate(db, sql, page, size)


async def query_project_by_id(db: AsyncSession, project_id: int) -> Project | None:
    sql = select(Project).where(Project.id == project_id)
    result = await db.execute(sql)
    return result.scalar()


async def delete_project_by_id(db: AsyncSession, project_id: int) -> None:
    project = await query_project_by_id(db, project_id)

    if project is not None:
        project.desc = "delete"
        await db.commit()

    return
