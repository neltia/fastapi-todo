from fastapi import Header
from fastapi import HTTPException
from typing_extensions import Annotated
import unkey
import os
from dotenv import load_dotenv

load_dotenv()


async def api_key_required(x_api_key: Annotated[str, Header()]):
    # 헤더에 키 값이 없는 경우 확인
    if x_api_key is None or x_api_key == "":
        raise HTTPException(status_code=400, detail="not found key")

    # 인증 여부 확인
    unkey_root_key = os.environ["UNKEY_ROOT_KEY"]
    unkey_api_id = os.environ["UNKEY_API_ID"]
    client = unkey.Client(api_key=unkey_root_key)
    await client.start()
    result = await client.keys.verify_key(key=x_api_key, api_id=unkey_api_id)

    # unkey 서버 not ok 응답 확인
    if not result.is_ok:
        status_code = 500
        error_msg = "auth server not running"
        raise HTTPException(status_code=status_code, detail=error_msg)

    # 인증 여부 검사
    result_data = result._value.to_dict()
    is_valid = result_data["valid"]
    if is_valid:
        return
    else:
        status_code = 401
        error_msg = "unvalid key"
        raise HTTPException(status_code=status_code, detail=error_msg)
