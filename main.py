import uvicorn
from fastapi import FastAPI
from common.handlers.error_handler import setup_exception_handlers
from auth.controller import auth_router
from todo.controller import todo_router

# main app init
app = FastAPI(
    title="Todo API",
    description="Todo API with Unkey service auth",
    version="0.0.1",
    docs_url="/docs"
)

# error handler
setup_exception_handlers(app)

# route add
app.include_router(auth_router)
app.include_router(todo_router)

# app run as debug
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
