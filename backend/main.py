import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.server.routers.test_router import router as test_router
from src.server.routers.data_generator_router import router as data_generator_router

app = FastAPI()

app.include_router(test_router)
app.include_router(data_generator_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8090, log_config=None)
