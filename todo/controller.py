from fastapi import APIRouter, Path
from fastapi import HTTPException
from todo.model import TodoItem

todo_router = APIRouter()
todo_list = []


@todo_router.post("/todo", status_code=201)
async def post(todo: TodoItem) -> dict:
    todo_list.append(todo)
    return {"message": "success"}


@todo_router.get("/todo")
async def getTodo() -> dict:
    return {"list": todo_list}


@todo_router.get("/todo/{id}")
async def getTodoItem(id: int = Path(gt=-1, title="todo id")) -> dict:
    if id not in todo_list:
        status_code = 404
        description = f"task number: {id} Not found"
        raise HTTPException(status_code=status_code, detail=description)

    return {"item": todo_list[id]}


@todo_router.put("/todo/{todo_id}")
async def putTodoItem(todo: TodoItem, todo_id: int = Path(gt=-1, title="todoItem id")) -> dict:
    todo_list[todo_id] = todo
    return {"message": "update success"}


@todo_router.delete("/todo")
async def deleteTodo() -> dict:
    todo_list.clear()
    return {"message": "delete all success"}
