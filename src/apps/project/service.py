from sqlalchemy.ext.asyncio import AsyncSession

from src.core.domain.schemas_base import Pagination

from .crud import create_project as db_create_project
from .crud import query_user_list as db_query_user_list
from .models import Project
from .schemas import CreateProjectParams


async def create_project(
    db: AsyncSession, create_user_params: CreateProjectParams
) -> Project:
    """
    业务逻辑层
    :param db:
    :param name:
    :param create_user_params:
    :return:
    """
    user = await db_create_project(
        db, create_user_params.name, create_user_params.desc, create_user_params.tags
    )
    return user


async def query_project_list(db: AsyncSession, page: int, size: int) -> Pagination:
    return await db_query_user_list(db, page, size)
