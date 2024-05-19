from pydantic import BaseModel
from typing import List


# api key 생성 요청 시 사용
class api_key_create(BaseModel):
    roles: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "roles": ["role1", "role2"]
            }
        }
