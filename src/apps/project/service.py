from sqlalchemy.ext.asyncio import AsyncSession

from src.core.domain.exception import NotFoundException
from src.core.domain.schemas_base import Pagination

from .crud import create_project as db_create_project
from .crud import delete_project_by_id as db_delete_project_by_id
from .crud import query_project_by_id as db_query_project_by_id
from .crud import query_project_list as db_query_project_list
from .models import Project
from .schemas import CreateProjectParams


async def create_project(
    db: AsyncSession, create_project_params: CreateProjectParams
) -> Project:
    """
    业务逻辑层
    :param db:
    :param name:
    :param create_user_params:
    :return:
    """
    user = await db_create_project(
        db,
        create_project_params.name,
        create_project_params.desc,
        create_project_params.tags,
    )
    return user


async def query_project_list(db: AsyncSession, page: int, size: int) -> Pagination:
    return await db_query_project_list(db, page, size)


async def query_project_by_id(db: AsyncSession, project_id: int) -> Project:
    project = await db_query_project_by_id(db, project_id)

    if project is None:
        raise NotFoundException()

    return project


async def delete_project_by_id(db: AsyncSession, project_id: int) -> None:
    return await db_delete_project_by_id(db, project_id)
