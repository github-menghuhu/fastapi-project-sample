from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependency.db_dep import get_async_session
from src.core.domain.constant import ResponseCode, ResponseMessage
from src.core.domain.schemas_base import (
    CommonResponse,
    PaginateResponse,
    QueryPaginationParams,
)

from .schemas import CreateProject, CreateProjectParams, QueryProjectList
from .service import create_project, query_project_list

router = APIRouter()


@router.post("/", response_model=CommonResponse[CreateProject])
async def create_project_api(
    create_user_params: CreateProjectParams,
    db: AsyncSession = Depends(get_async_session),
):
    """
    接口层
    :param create_user_params: 参数
    :param db: 数据库链接对象依赖
    :return:
    """
    name = create_user_params.name
    desc = create_user_params.desc
    tags = create_user_params.tags
    print(f"name:{name}")
    print(f"desc:{desc}")
    print(f"tags:{tags}")

    user = await create_project(db, create_user_params)
    return CommonResponse(
        data=user,
        code=ResponseCode.create_success,
        message=ResponseMessage.create_success,
    )


@router.get("/", response_model=PaginateResponse[QueryProjectList])
async def query_project_list_api(
    query_pagination_params: QueryPaginationParams = Depends(),
    db: AsyncSession = Depends(get_async_session),
):
    """
    接口层
    :param db:
    :param query_pagination_params:
    :return:
    """
    project_list = await query_project_list(
        db, query_pagination_params.page, query_pagination_params.size
    )
    return PaginateResponse(
        data=project_list,
        code=ResponseCode.request_success,
        message=ResponseMessage.request_success,
    )
