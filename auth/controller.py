from typing import Dict, Optional
from fastapi import Header
from fastapi import APIRouter
from fastapi import HTTPException
import unkey
import os
from dotenv import load_dotenv


load_dotenv()
auth_router = APIRouter()


async def is_key_verify(request_key: str):
    unkey_root_key = os.environ["UNKEY_ROOT_KEY"]
    unkey_api_id = os.environ["UNKEY_API_ID"]

    client = unkey.Client(api_key=unkey_root_key)
    await client.start()
    result = await client.keys.verify_key(key=request_key, api_id=unkey_api_id)

    if result.is_ok:
        result_data = result._value.to_dict()
        return result_data["valid"], result_data["code"]
    else:
        return False, result.unwrap_err()


@auth_router.get("/verify")
async def protected_route(
    *,
    x_api_key: str = Header(None),
) -> Dict[str, Optional[str]]:
    if x_api_key is None:
        status_code = 400
        error_msg = "not found key"
        raise HTTPException(status_code=status_code, detail=error_msg)

    result_code, result_msg = await is_key_verify(request_key=x_api_key)
    # print(result_msg)

    if result_code:
        return {"message": "valid"}
    else:
        status_code = 401
        error_msg = "unvalid key"
        raise HTTPException(status_code=status_code, detail=error_msg)
