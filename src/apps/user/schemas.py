from pydantic import BaseModel, EmailStr, Field


class Sign(BaseModel):
    email: EmailStr
    password: str | None = Field(min_length=6, max_length=20)


class SignUpParams(Sign):
    pass


class SignInParams(Sign):
    pass


class SignUpOut(BaseModel):
    user_id: str = Field(alias="userId")
    name: str | None = None
    gender: str | None = None
    nick_name: str | None = Field(default=None, alias="nickname")
    phone: str | None = None
    email: EmailStr


class SignInOut(BaseModel):
    scope: str
    access_token: str
    id_token: str
    token_type: str
    expires_in: int
