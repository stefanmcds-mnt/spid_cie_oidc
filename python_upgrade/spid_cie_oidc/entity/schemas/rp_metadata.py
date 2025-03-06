from enum import Enum
from typing import Annotated, List, Optional
from pydantic import BaseModel, HttpUrl, model_validator
from .jwks import JwksSpid

class GrantTypeSupported(str, Enum):
    refresh_token = "refresh_token"  # nosec - B105
    authorization_code = "authorization_code"

class RPMetadata(BaseModel):
    organization_name: str
    redirect_uris: List[HttpUrl]
    #response_types = ["code"]
    response_types: Annotated[str, "code"]
    grant_types: List[GrantTypeSupported]
    client_id: HttpUrl
    # TODO: Could be specified in multiple languages
    client_name: str
    signed_jwks_uri: Optional[HttpUrl]
    jwks_uri: Optional[HttpUrl]
    jwks: Optional[JwksSpid]

    @model_validator(mode='after')
    def validate(cls, values):
        jwks_there = False
        for i in ("jwks_uri", "jwks", "signed_jwks_uri"):
            if values.get(i):
                jwks_there = True
                break

        if not jwks_there:
            raise ValueError(
                "one of signed_jwks_uri or jwks_uri or jwks must be set"
            )
        return values

class RPMetadataSpid(RPMetadata):
    pass

class RPMetadataCie(RPMetadataSpid):
    #application_type = "web"
    application_type: Annotated[str, "web"]
    tls_client_certificate_bound_access_tokens: Optional[bool]
