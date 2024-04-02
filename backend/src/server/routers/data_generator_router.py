from fastapi import APIRouter, Query
from starlette import status

from src.services.data_generator_service import get_available_generators_list

from src.services.data_generator_service import generate_data

router = APIRouter(prefix="/data-generator", tags=["Data Generator"])


@router.get("/", status_code=status.HTTP_200_OK)
async def data_generator(generators_list: list[str] = Query(None)):
    return generate_data(generators_list)


@router.get("/get-generators", response_model=list[str], status_code=status.HTTP_200_OK)
async def get_generators():
    return get_available_generators_list()
