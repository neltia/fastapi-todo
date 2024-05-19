from typing import Dict, Optional
from fastapi import Header, APIRouter, Depends
from fastapi import HTTPException
from fastapi.security import APIKeyHeader
from fastapi import Security
from auth.model import api_key_create
from auth.service import is_key_verify, create_api_key

from common.models.response import ResponseResult
from common.models.enums import ResponseCodeEnum


auth_router = APIRouter()


# 관리자 권한 키 확인
async def authorize_key_required(authorize_key=Security(APIKeyHeader(name="Authorization"))):
    # 헤더에 키 값이 없는 경우 확인
    if authorize_key is None or authorize_key == "":
        raise HTTPException(status_code=401, detail="not found key")
    return authorize_key


# 키 인증 여부 확인
@auth_router.get("/verify", response_model=ResponseResult, response_model_exclude_none=True)
async def protected_route(x_api_key: str = Header(None)) -> Dict[str, Optional[str]]:
    status_code = ResponseCodeEnum.SUCCESS

    if x_api_key is None:
        status_code = ResponseCodeEnum.INVALID_PARAM
        error_msg = "not found key"
        result = ResponseResult(result_code=status_code, error_msg=error_msg)
        return result

    res_code, res_msg = await is_key_verify(request_key=x_api_key)
    if not res_code:
        status_code = ResponseCodeEnum.UNAUTHORIZED
        msg = "unvalid key"
        result = ResponseResult(result_code=status_code, result_msg=msg)
        return result

    msg = "valid"
    result = ResponseResult(result_code=status_code, result_msg=msg)
    return result


# 새 API 키 생성
@auth_router.post("/token", status_code=201, dependencies=[Depends(authorize_key_required)])
async def token_generate(api_key_create: api_key_create, authorize_key: str = Depends(authorize_key_required)) -> dict:
    status_code = ResponseCodeEnum.SUCCESS

    res_code, res_msg = await create_api_key(authorize_key, api_key_create)
    if not res_code:
        status_code = ResponseCodeEnum.UNAUTHORIZED
        msg = "unvalid key"
        result = ResponseResult(result_code=status_code, result_msg=msg)
        return result

    result = ResponseResult(result_code=status_code, result_msg=res_msg)
    return result
