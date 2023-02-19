from fastapi import APIRouter

from app.api_v1.statistic.controller.exgauster_controller import exgauster_router

api_router = APIRouter()


api_router.include_router(exgauster_router, prefix='/exgausters', tags=['exgauster'])
