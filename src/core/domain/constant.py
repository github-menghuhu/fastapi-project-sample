from dataclasses import dataclass


@dataclass(frozen=True)
class ResponseCode:
    """
    自定义响应码
    """

    request_success = 2000
    create_success = 2001
    update_success = 2003
    delete_success = 2004

    request_error = 4000


@dataclass(frozen=True)
class ResponseMessage:
    """
    自定义响应信息
    """

    request_success = "request success"
    create_success = "create success"
    update_success = "update success"
    delete_success = "delete success"

    request_error = "request error"
