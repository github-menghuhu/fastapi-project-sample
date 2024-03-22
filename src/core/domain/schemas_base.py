from typing import Generic, Sequence, TypeVar

from fastapi import Query
from pydantic import BaseModel

T = TypeVar("T")


class CommonResponse(BaseModel, Generic[T]):
    """
    自定义响应体结构
    """

    code: int
    message: str | None = None
    data: T = {}  # type: ignore


class Pagination(BaseModel, Generic[T]):
    total: int
    page: int
    size: int
    items: Sequence[T]


class PaginateResponse(BaseModel, Generic[T]):
    """
    分页响应体
    """

    code: int
    message: str | None = None
    data: Pagination[T]


class QueryPaginationParams:
    """
    自定义分页参数
    """

    def __init__(
        self,
        page: int = Query(default=1, ge=1),
        size: int = Query(default=20, ge=1, le=100),
    ):
        self.page = page
        self.size = size
