from pydantic import BaseModel


class TodoItem(BaseModel):
    item: int
    task: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": 1,
                "task": "my task"
            }
        }
