from fastapi import status
from fastapi.responses import JSONResponse

from .constant import ResponseCode, ResponseMessage


class AuthException(Exception):
    # authing异常
    def __init__(
        self,
        http_code: int = status.HTTP_401_UNAUTHORIZED,
        api_code: int = ResponseCode.auth_error,
        message: str = ResponseMessage.auth_error,
    ):
        self.status_code = http_code
        self.content = {"code": api_code, "message": message}


async def authing_handler(request, exc: AuthException):
    return JSONResponse(content=exc.content, status_code=exc.status_code)


class NoPermissionException(Exception):
    # 无权限异常
    def __init__(
        self,
        code: int = ResponseCode.no_permission,
        message: str = ResponseMessage.no_permission,
    ):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.content = {"code": code, "message": message}


async def no_permission_handler(request, exc: NoPermissionException):
    return JSONResponse(content=exc.content, status_code=exc.status_code)


class NotFoundException(Exception):
    # 资源未找到
    def __init__(
        self,
        code: int = ResponseCode.not_found,
        message: str = ResponseMessage.not_found,
    ):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.content = {"code": code, "message": message}


async def not_found_handler(request, exc: NotFoundException):
    return JSONResponse(content=exc.content, status_code=exc.status_code)


class AsyncTaskException(Exception):
    # 异步任务异常
    def __init__(
        self,
        code: int = ResponseCode.exec_async_task_fail,
        message: str = ResponseMessage.exec_async_task_fail,
    ):
        self.status_code = status.HTTP_200_OK
        self.content = {"code": code, "message": message}


async def async_task_handler(request, exc: AsyncTaskException):
    return JSONResponse(content=exc.content, status_code=exc.status_code)
