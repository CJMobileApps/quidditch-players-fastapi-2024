from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()


@router.get("/")
async def read_index():
    return FileResponse('static/index.html')
