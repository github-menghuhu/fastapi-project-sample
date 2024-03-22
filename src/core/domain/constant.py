from dataclasses import dataclass


@dataclass(frozen=True)
class ResponseCode:
    """
    自定义业务响应码
    """

    # 资源增删改查
    query_success = 2000
    create_success = 2001
    update_success = 2003
    delete_success = 2004

    # 非资源请求
    request_success = query_success

    # 异常详情
    no_permission = 4000
    not_found = 4001
    exec_async_task_fail = 4002
    auth_error = 4003


@dataclass(frozen=True)
class ResponseMessage:
    """
    自定义业务响应信息
    """

    # 资源增删改查
    query_success = "query success"
    create_success = "create success"
    update_success = "update success"
    delete_success = "delete success"

    # 非资源请求
    request_success = "request success"

    # 异常详情
    no_permission = "no operation permission"
    not_found = "resource not found"
    exec_async_task_fail = "async task exec failed"
    auth_error = "authing error"
