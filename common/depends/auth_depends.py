from common.models.enums import ResponseCodeEnum
from common.models.response import ResponseResult
from fastapi import Header
from typing_extensions import Annotated
import unkey
import os
from dotenv import load_dotenv

load_dotenv()


# 사용자 API 키 요청 인증 확인
async def api_key_required(x_api_key: Annotated[str, Header()]):
    # 헤더에 키 값이 없는 경우 확인
    if x_api_key is None or x_api_key == "":
        status_code = ResponseCodeEnum.INVALID_PARAM
        error_msg = "not found key"
        return ResponseResult(result_code=status_code, error_msg=error_msg)

    # 인증 여부 확인
    unkey_root_key = os.environ["UNKEY_ROOT_KEY"]
    unkey_api_id = os.environ["UNKEY_API_ID"]
    client = unkey.Client(api_key=unkey_root_key)
    await client.start()
    result = await client.keys.verify_key(key=x_api_key, api_id=unkey_api_id)

    # unkey 서버 not ok 응답 확인
    if not result.is_ok:
        status_code = ResponseCodeEnum.SERVER_ERROR
        error_msg = "auth server not running"
        return ResponseResult(result_code=status_code, error_msg=error_msg)

    # 인증 여부 검사
    result_data = result._value.to_dict()
    is_valid = result_data["valid"]
    if is_valid:
        return
    else:
        status_code = ResponseCodeEnum.UNAUTHORIZED
        error_msg = "unvalid key"
        return ResponseResult(result_code=status_code, error_msg=error_msg)
