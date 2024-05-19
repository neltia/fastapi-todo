from pydantic import BaseModel
from typing import Optional, Dict, Union


# api key 생성 요청 시 사용
# - name: 키 이름 지정
# - owner_id: 프로젝트에서 키를 사용할/발급한 사용자와 연결
# - prefix: 키 앞에 붙일 접두사 지정
# - remaining: 총 사용량 제한 설정
# - ratelimit: interval(milliseconds)당 요청 제한 설정
# - refill: 총 사용량 제한 설정: None / Daily / Monthly
# - meta: 키 내부에 삽입할 메타 데이터 (dict)
# - expires: 만료 시간 지정 (단위: 밀리초)
class api_key_create(BaseModel):
    name: str = ""
    owner_id: str = "test-user"
    prefix: str = ""

    remaining: Optional[int] = None
    meta: Optional[Dict] = None
    expires: Union[int, None] = None
