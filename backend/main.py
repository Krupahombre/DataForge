import logging
import os
import sys

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.server.routers.data_generator_router import router as data_generator_router

app = FastAPI()

app.include_router(data_generator_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if not os.path.isfile(sys.argv[1]):
    print('Logging config file not found')
    raise FileNotFoundError('Logging config file not found')
logging.config.fileConfig(sys.argv[1], disable_existing_loggers=False)


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8090, log_config=None)
