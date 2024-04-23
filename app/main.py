import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.api.api_router import api_router

app = FastAPI(description="main API")

app.include_router(api_router)

app.mount('/', StaticFiles(directory='static', html=True), name='static')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
