from fastapi import APIRouter, Path
from todo.model import TodoItem
from todo.service import get_todo_list, get_todo_item
from todo.service import create_todo_item, put_todo_item, delete_todo

from common.depends.auth_depends import api_key_required
from common.models.response import ResponseResult

todo_router = APIRouter()
# todo_router = APIRouter(dependencies=[Depends(api_key_required)])

# 임시 DB 역할 변수
todo_list = []


# 특정 데코레이터에만 적용
# @todo_router.post("/todo", status_code=201, dependencies=[Depends(api_key_required)])
@todo_router.post("/todo", status_code=201, response_model=ResponseResult, response_model_exclude_none=True)
async def post(todo: TodoItem) -> dict:
    result = create_todo_item(todo_list, todo)
    return result


@todo_router.get("/todo", response_model=ResponseResult, response_model_exclude_none=True)
async def getTodo() -> dict:
    result = get_todo_list(todo_list)
    return result


@todo_router.get("/todo/{todo_id}", response_model=ResponseResult, response_model_exclude_none=True)
async def getTodoItem(todo_id: int = Path(title="todo id")) -> dict:
    result = get_todo_item(todo_list, todo_id)
    return result


@todo_router.put("/todo/{todo_id}", response_model=ResponseResult, response_model_exclude_none=True)
async def putTodoItem(todo: TodoItem, todo_id: int = Path(gt=-1, title="todoItem id")) -> dict:
    result = put_todo_item(todo_list, todo_id, todo)
    return result


@todo_router.delete("/todo", response_model=ResponseResult, response_model_exclude_none=True)
async def deleteTodo() -> dict:
    result = delete_todo(todo_list)
    return result
