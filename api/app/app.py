from fastapi import FastAPI
from .core.config import config
from .api_v1 import api_router as api_v1_router
from .db.base import drop_database, create_database

app = FastAPI(
    title=config.PROJECT_NAME,
)

app.include_router(api_v1_router, prefix=config.API_V1_URL)


@app.on_event('startup')
async def startup():
    await drop_database()
    await create_database()
