from fastapi import FastAPI
from .core.config import config
from .api_v1 import api_router as api_v1_router


app = FastAPI(
    title=config.PROJECT_NAME,
)

app.include_router(api_v1_router, prefix=config.API_V1_URL)
