from typing import Literal

from pydantic import BaseModel, constr

class TokenResponse(BaseModel):
    access_token: constr(pattern=r"^[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+") # type: ignore # noqa: F722
    token_type: Literal["Bearer"]
    expires_in: int
    id_token: constr(pattern=r"^[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+")  # type: ignore # noqa: F722

class TokenRefreshResponse(TokenResponse):
    refresh_token: constr(pattern=r"^[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+") #type: ignore # noqa: F722

class TokenErrorResponse(BaseModel):
    error: Literal["invalid_request", "unauthorized_client"]
    error_description: str
