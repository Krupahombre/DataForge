from fastapi import APIRouter
from starlette import status

from src.services.data_generator_service import get_available_generators_list

from src.services.generation_brain_service import generate_data_with_response_format

from src.server.models.generator_model import GeneratorModel

router = APIRouter(prefix="/data-generator", tags=["Data Generator"])


@router.post("/", status_code=status.HTTP_200_OK)
async def data_generator(generator_data: GeneratorModel):
    return generate_data_with_response_format(generator_data)


@router.get("/get-generators", response_model=dict[str, list[str]], status_code=status.HTTP_200_OK)
async def get_generators():
    return get_available_generators_list()
