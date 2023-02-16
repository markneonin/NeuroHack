from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import async_session


async def get_session() -> AsyncIterator[AsyncSession]:
    session: AsyncSession = async_session()
    try:
        yield session
    finally:
        await session.close()

