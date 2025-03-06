from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, HttpUrl, conlist, constr, field_validator, validator

# TODO: Schema of claims is not genrated

class AcrValues(str, Enum):
    l1 = "https://www.spid.gov.it/SpidL1"
    l2 = "https://www.spid.gov.it/SpidL2"
    l3 = "https://www.spid.gov.it/SpidL3"

class ScopeSpid(str, Enum):
    openid = "openid"
    offline_access = "offline_access"

class ScopeCie(str, Enum):
    openid = "openid"
    offline_access = "offline_access"
    profile = "profile"
    email = "email"

class ClaimsTypeEssential(BaseModel):
    essential: Optional[bool]

class ClaimsTypeStringValue(BaseModel):
    value: Optional[str]

class ClaimsTypeStringValues(BaseModel):
    values: Optional[conlist(str, min_length=2, max_length=2)] # type: ignore

class ClaimsType(str, Enum):
    essential = ClaimsTypeEssential
    value = ClaimsTypeStringValue
    values = ClaimsTypeStringValues

class UserInfoSpid(BaseModel):
    name: Optional[dict] = Field(
        alias="given_name", default=None
    )
    family_name: Optional[dict] = Field(
        alias="family_name", default=None
    )
    place_of_birth: Optional[dict] = Field(
        alias="place_of_birth", default=None
    )
    date_of_birth: Optional[dict] = Field(
        alias="birthdate", default=None
    )
    gender: Optional[dict] = Field(
        alias="gender", default=None
    )
    company_name: Optional[dict] = Field(
        alias="https://attributes.eid.gov.it/company_name", default=None
    )
    registered_office: Optional[dict] = Field(
        alias="https://attributes.eid.gov.it/registered_office", default=None
    )
    fiscal_number: Optional[dict] = Field(
        alias="https://attributes.eid.gov.it/fiscal_number", default=None
    )
    iva_code: Optional[dict] = Field(
        alias="https://attributes.eid.gov.it/vat_number", default=None
    )
    id_card: Optional[dict] = Field(
        alias="https://attributes.eid.gov.it/document_details", default=None
    )
    mobile_phone: Optional[dict] = Field(
        alias="https://attributes.eid.gov.it/phone_number", default=None
    )
    email: Optional[dict] = Field(
        alias="email", default=None
    )
    address: Optional[dict] = Field(
        alias="address", default=None
    )
    expiration_date: Optional[dict] = Field(
        alias="https://attributes.eid.gov.it/eid_exp_date", default=None
    )
    digital_address: Optional[dict] = Field(
        alias="https://attributes.eid.gov.it/e_delivery_service", default=None
    )

class UserInfoCie(BaseModel):
    given_name: Optional[dict]
    family_name: Optional[dict]
    email: Optional[dict]
    email_verified: Optional[dict]
    gender: Optional[dict]
    birthdate: Optional[dict]
    phone_number: Optional[dict]
    phone_number_verified: Optional[dict]
    address: Optional[dict]
    place_of_birth: Optional[dict]
    document_details: Optional[dict]
    e_delivery_service: Optional[dict]
    fiscal_number: Optional[dict]
    physical_phone_number: Optional[dict]

class IdToken(UserInfoCie):
    pass

TYPES = {
    "essential": ClaimsTypeEssential,
    "value": ClaimsTypeStringValue,
    "values": ClaimsTypeStringValues,
}

CLAIMS_SPID = {"userinfo": UserInfoSpid}

CLAIMS_CIE = {"userinfo": UserInfoCie, "id_token": IdToken}

class AuthenticationRequest(BaseModel):
    client_id: HttpUrl
    response_type: Literal["code"]
    scope: List[str]
    code_challenge: str
    code_challenge_method: Literal["S256"]
    nonce: constr(min_length=32) # type: ignore
    redirect_uri: HttpUrl
    claims: Optional[dict]
    state: constr(min_length=32) # type: ignore
    # TODO: to be improved
    ui_locales: Optional[List[str]]

    # sub claim MUST not be used to prevent that this jwt
    # could be reused as a private_key_jwt
    # sub: HttpUrl

    iss: HttpUrl
    iat: int
    exp: Optional[int]
    jti: Optional[str]
    aud: str | List[HttpUrl]
    acr_values: Optional[List[AcrValues]]
    prompt: Optional[Literal["consent", "consent login"]]

    #@validator("claims")
    @field_validator("claims")
    def validate_claims(cls, claims):
        for k_claim, v_claim in claims.items():
            cl = cls.get_claims()
            claims_items = cl.get(k_claim, None)
            if not claims_items:
                continue
            claims_items(**v_claim)
            for k_item, v_item in v_claim.items():
                if v_item is not None:
                    for k_type, v_type in TYPES.items():
                        v_type(**v_item)
        return claims

    #@validator("scope")
    @field_validator("scope")
    def validate_scope(cls, scope):
        if "openid" not in scope:
            raise ValueError("'scope' attribute must contain 'openid'")

class AuthenticationRequestSpid(AuthenticationRequest):
    scope: List[ScopeSpid]

    def get_claims() -> dict:
        return CLAIMS_SPID

    def example():  # pragma: no cover
        return AuthenticationRequestSpid(  # nosec B106
            client_id= "https://rp.cie.it/callback1/",
            response_type= "code",
            scope= ["openid", "offline_access"],
            code_challenge= "codeChallenge",
            code_challenge_method= "S256",
            nonce= "12345678123456781234567812345678inpiu",
            prompt= "consent",
            redirect_uri= "https://rp.cie.it/callback1/",
            acr_values= ["https://www.spid.gov.it/SpidL2", "https://www.spid.gov.it/SpidL1"],
            claims= {},
            state= "fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd",
            ui_locales= ["codice1", "codice2", "codice3"],
            sub= "https://rp.cie.it/",
            iss= "https://op.spid.agid.gov.it/",
            aud= ["https://rp.spid.agid.gov.it/auth"],
            iat= 1648591200,
            exp= 1648592200,
            jti= "a72d5df0-2415-4c7c-a44f-3988b354040b",
        )

class AuthenticationRequestCie(AuthenticationRequest):
    scope: List[ScopeCie]

    def get_claims() -> dict:
        return CLAIMS_CIE

class AuthenticationRequestDoc(BaseModel):
    client_id: HttpUrl
    response_type: Literal["code"]
    scope: List[str]
    code_challenge: str
    code_challenge_method: Literal["S256"]
    request: constr(pattern=r"^[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+") # type: ignore # noqa: F722

    def example():  # pragma: no cover
        return AuthenticationRequestDoc(  # nosec B106
            client_id= "https://rp.cie.it/callback1/",
            response_type= "code",
            scope= ["openid", "offline_access"],
            code_challenge= "codeChallenge",
            code_challenge_method= "S256",
            request= "eyJhbGciOiJSUzI1NiIsImtpZCI6ImsyYmRjIn0.ew0KICJpc3MiOiAiczZCaGRSa3F0MyIsDQogImF1ZCI6ICJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbSIsDQogInJlc3BvbnNlX3R5cGUiOiAiY29kZSBpZF90b2tlbiIsDQogImNsaWVudF9pZCI6ICJzNkJoZFJrcXQzIiwNCiAicmVkaXJlY3RfdXJpIjogImh0dHBzOi8vY2xpZW50LmV4YW1wbGUub3JnL2NiIiwNCiAic2NvcGUiOiAib3BlbmlkIiwNCiAic3RhdGUiOiAiYWYwaWZqc2xka2oiLA0KICJub25jZSI6ICJuLTBTNl9XekEyTWoiLA0KICJtYXhfYWdlIjogODY0MDAsDQogImNsYWltcyI6IA0KICB7DQogICAidXNlcmluZm8iOiANCiAgICB7DQogICAgICJnaXZlbl9uYW1lIjogeyJlc3NlbnRpYWwiOiB0cnVlfSwNCiAgICAgI.qq",
        )
