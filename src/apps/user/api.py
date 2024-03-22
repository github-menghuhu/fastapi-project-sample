from authing import AuthenticationClient
from fastapi import APIRouter, Depends, status

from src.core.dependency.authing_dep import get_authing_client
from src.core.domain.constant import ResponseCode, ResponseMessage
from src.core.domain.exception import AuthException
from src.core.domain.schemas_base import CommonResponse

from .schemas import SignInOut, SignInParams, SignUpOut, SignUpParams

router = APIRouter()


@router.post("/sign-up", response_model=CommonResponse[SignUpOut])
def sign_up_api(
    sign_up_params: SignUpParams,
    authing_client: AuthenticationClient = Depends(get_authing_client),
):
    sign_up_result = authing_client.sign_up_by_email_password(
        email=sign_up_params.email,
        password=sign_up_params.password,
    )

    http_code = sign_up_result["statusCode"]
    if http_code != 200:
        raise AuthException(
            http_code=status.HTTP_401_UNAUTHORIZED,
            api_code=sign_up_result["apiCode"],
            message=f'request_id:{sign_up_result["requestId"]}, info:{sign_up_result["message"]}',
        )

    return CommonResponse(
        data=sign_up_result["data"],
        code=ResponseCode.create_success,
        message=ResponseMessage.create_success,
    )


@router.post("/sign-in", response_model=CommonResponse[SignInOut])
def sign_in_api(
    sign_in_params: SignInParams,
    authing_client: AuthenticationClient = Depends(get_authing_client),
):
    sign_in_result = authing_client.sign_in_by_email_password(
        email=sign_in_params.email,
        password=sign_in_params.password,
    )

    http_code = sign_in_result["statusCode"]
    if http_code != 200:
        raise AuthException(
            http_code=http_code,
            api_code=sign_in_result["apiCode"],
            message=f'request_id:{sign_in_result["requestId"]}, info:{sign_in_result["message"]}',
        )

    return CommonResponse(
        data=sign_in_result["data"],
        code=ResponseCode.request_success,
        message=ResponseMessage.request_success,
    )
