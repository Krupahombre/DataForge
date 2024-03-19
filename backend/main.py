from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.server.routers.test_router import router as test_router

app = FastAPI()

app.include_router(test_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
