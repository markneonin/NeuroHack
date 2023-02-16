from typing import Any

from fastapi import APIRouter

test_router = APIRouter()


@test_router.get('/')
async def test() -> Any:
    return 'test'
