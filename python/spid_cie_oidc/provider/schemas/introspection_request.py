from typing import Literal
from pydantic import BaseModel, HttpUrl, constr

class IntrospectionRequest(BaseModel):
    client_assertion: constr(pattern=r"^[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+") # type: ignore # noqa: F722
    client_assertion_type: Literal[
        "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
    ]
    client_id: HttpUrl
    token: constr(pattern=r"^[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+") # type: ignore # noqa: F722
