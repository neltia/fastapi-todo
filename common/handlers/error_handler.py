from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from common.models.response import ResponseResult
from common.models.enums import ResponseCodeEnum


def setup_exception_handlers(app):
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=ResponseCodeEnum(exc.status_code),
            content=ResponseResult(
                result_code=str(exc.status_code),
                message=exc.detail
            ).model_dump(exclude_unset=True, exclude_none=True)
        )

    @app.exception_handler(404)
    async def not_found_exception_handler(request: Request, exc):
        return JSONResponse(
            status_code=ResponseCodeEnum.NOT_FOUND,
            content=ResponseResult(
                result_code="404",
                result_msg="Resource not found"
            ).model_dump(exclude_unset=True, exclude_none=True)
        )
