from fastapi import APIRouter, Depends

from app import schema
from app.api_v1.statistic.service.exgauster_service import ExgausterService

exgauster_router = APIRouter()


@exgauster_router.get('/')
async def get_exgausters(
        service: ExgausterService = Depends()

) -> list[schema.Exgauster]:
    return await service.get_exgausters()


@exgauster_router.get('/{number}')
async def get_exgauster(
        number: int,
        service: ExgausterService = Depends(),

) -> schema.Exgauster:
    return await service.get_exgauster(number)
