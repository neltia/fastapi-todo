from unkey.undefined import UNDEFINED
from auth.model import api_key_create
import unkey
import os
from dotenv import load_dotenv


load_dotenv()


async def is_key_verify(request_key: str):
    unkey_api_id = os.environ["UNKEY_API_ID"]

    client = unkey.Client()
    await client.start()
    result = await client.keys.verify_key(key=request_key, api_id=unkey_api_id)

    if result.is_ok:
        result_data = result._value.to_dict()
        return result_data["valid"], result_data["code"]
    else:
        return False, result.unwrap_err()


async def create_api_key(authorize_key: str, api_key_create: api_key_create):
    unkey_root_key = os.environ["UNKEY_ROOT_KEY"]
    unkey_api_id = os.environ["UNKEY_API_ID"]

    if authorize_key != unkey_root_key:
        return False, ""

    key_request = api_key_create.model_dump()
    # print(key_request)
    owner_id = key_request["owner_id"]
    prefix = key_request["prefix"]
    meta = key_request["meta"]
    expires = key_request["expires"]

    if len(key_request["meta"].keys()) > 0:
        meta = UNDEFINED
    if expires == 0:
        expires = UNDEFINED

    client = unkey.Client(api_key=unkey_root_key)
    await client.start()
    result = await client.keys.create_key(
        api_id=unkey_api_id, owner_id=owner_id, prefix=prefix,
        meta=meta, expires=expires
    )

    if result.is_ok:
        result_data = result._value.to_dict()
        return True, result_data
    else:
        return False, result.unwrap_err()
