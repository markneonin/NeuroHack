from fastapi import APIRouter

from app.api_v1.test.controller.test_controller import test_router

api_router = APIRouter()

api_router.include_router(test_router, prefix='/test', tags=['test'])
