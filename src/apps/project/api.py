from typing import Union
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.celery import celery_app
from src.celery.tasks import test_async_task
from src.core.dependency.db_dep import get_async_session
from src.core.domain.constant import ResponseCode, ResponseMessage
from src.core.domain.exception import AsyncTaskException
from src.core.domain.schemas_base import (
    CommonResponse,
    PaginateResponse,
    QueryPaginationParams,
)

from .schemas import (
    AsyncTask,
    AsyncTaskStatus,
    CreateProject,
    CreateProjectParams,
    QueryProject,
    QueryProjectList,
)
from .service import (
    create_project,
    delete_project_by_id,
    query_project_by_id,
    query_project_list,
)

router = APIRouter()


@router.post("/", response_model=CommonResponse[CreateProject])
async def create_project_api(
    create_project_params: CreateProjectParams,
    db: AsyncSession = Depends(get_async_session),
):
    """
    接口层
    :param create_project_params: 参数
    :param db: 数据库链接对象依赖
    :return:
    """
    name = create_project_params.name
    desc = create_project_params.desc
    tags = create_project_params.tags
    print(f"name:{name}")
    print(f"desc:{desc}")
    print(f"tags:{tags}")

    project = await create_project(db, create_project_params)
    return CommonResponse(
        data=project,
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
        code=ResponseCode.query_success,
        message=ResponseMessage.query_success,
    )


@router.get("/{project_id}/", response_model=CommonResponse[Union[QueryProject]])
async def query_project_by_id_api(
    project_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    """
    接口层
    :param db:
    :param project_id:
    :return:
    """

    project = await query_project_by_id(db, project_id)
    return CommonResponse(
        data=project,
        code=ResponseCode.query_success,
        message=ResponseMessage.query_success,
    )


@router.delete("/{project_id}/", response_model=CommonResponse)
async def delete_project_by_id_api(
    project_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    """
    接口层
    :param db:
    :param project_id:
    :return:
    """

    await delete_project_by_id(db, project_id)
    return CommonResponse(
        code=ResponseCode.delete_success,
        message=ResponseMessage.delete_success,
    )


@router.post("/async-task/", response_model=CommonResponse[AsyncTask])
def create_async_task():
    """
    测试异步任务
    :param db:
    :return:
    """
    task = test_async_task.delay(1, 10)
    print(f"async task id:{task.id}")
    return CommonResponse(
        data=task,
        code=ResponseCode.request_success,
        message=ResponseMessage.request_success,
    )


@router.get("/async-task/{task_id}", response_model=CommonResponse[AsyncTaskStatus])
def query_async_task(task_id: UUID):
    """
    测试异步任务
    :param task_id:
    :return:
    """
    task = celery_app.AsyncResult(str(task_id))
    if task.failed():
        raise AsyncTaskException()

    is_ready = task.ready()
    print(f"async task ready status:{is_ready}")
    return CommonResponse(
        data=AsyncTaskStatus(task_id=task_id, is_ready=is_ready),
        code=ResponseCode.request_success,
        message=ResponseMessage.request_success,
    )
