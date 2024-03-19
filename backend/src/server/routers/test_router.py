from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/test", tags=["Test"])


@router.get("/", status_code=status.HTTP_200_OK)
async def test_ep(user_input: str):
    return {"your input": user_input}
