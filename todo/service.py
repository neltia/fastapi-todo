from common.models.enums import ResponseCodeEnum
from common.models.response import ResponseResult
from todo.model import TodoItem


def get_todo_list(todo_list: list, todo: TodoItem) -> ResponseResult:
    result_code = ResponseCodeEnum.SUCCESS

    todo_list.append(todo)

    msg = "success"
    result = ResponseResult(result_code=result_code, result_msg=msg)
    return result


def create_todo_item(todo_list: list) -> ResponseResult:
    result_code = ResponseCodeEnum.SUCCESS
    data = {"list": todo_list}

    result = ResponseResult(result_code=result_code, data=data)
    return result


def get_todo_item(todo_list: list, todo_id: int) -> ResponseResult:
    result_code = ResponseCodeEnum.SUCCESS

    if todo_id not in todo_list:
        status_code = ResponseCodeEnum.NOT_FOUND
        description = f"task number: {todo_id} Not found"
        result = ResponseResult(result_code=status_code, error_msg=description)

    data = {"item": todo_list[todo_id]}
    result = ResponseResult(result_code=result_code, data=data)
    return result


def put_todo_item(todo_list: list, todo_id: int, todo: TodoItem) -> ResponseResult:
    result_code = ResponseCodeEnum.SUCCESS

    if todo_id not in todo_list:
        status_code = ResponseCodeEnum.NOT_FOUND
        description = f"task number: {todo_id} Not found"
        result = ResponseResult(result_code=status_code, error_msg=description)

    todo_list[todo_id] = todo

    msg = "update success"
    result = ResponseResult(result_code=result_code, result_msg=msg)
    return result


def delete_todo(todo_list: list) -> ResponseResult:
    result_code = ResponseCodeEnum.SUCCESS

    todo_list.clear()

    msg = "delete all success"
    result = ResponseResult(result_code=result_code, result_msg=msg)
    return result
