from auth.model import api_key_create
import unkey
import os
from dotenv import load_dotenv


load_dotenv()


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


async def create_api_key(authorize_key: str, api_key_create: api_key_create):
    unkey_root_key = os.environ["UNKEY_ROOT_KEY"]
    unkey_api_id = os.environ["UNKEY_API_ID"]

    if authorize_key != unkey_api_id:
        return False, ""

    client = unkey.Client(api_key=unkey_root_key)
    await client.start()
    result = await client.keys.create_key(api_id=unkey_api_id, owner_id="")

    if result.is_ok:
        result_data = result._value.to_dict()
        return result_data["valid"], result_data["code"]
    else:
        return False, result.unwrap_err()
