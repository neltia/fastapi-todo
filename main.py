import uvicorn
from fastapi import FastAPI
from todo.controller import todo_router

# main app init
app = FastAPI(
    title="Todo API",
    description="Todo API with Unkey service auth",
    version="0.0.1",
    docs_url="/docs"
)

# route add
app.include_router(todo_router)

# app run as debug
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
