from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.mongo import db
from .api_v1 import api_router as api_v1_router
from .core.config import config

app = FastAPI(
    title=config.PROJECT_NAME,
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router, prefix=config.API_V1_URL)


@app.on_event('startup')
async def startup():
    ...
    await db.connect_to_database(host=config.STATISTIC_DB)
    # await drop_database()
    # await create_database()


@app.on_event('shutdown')
async def shutdown():
    await db.close_database_connection()
