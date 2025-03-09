from typing import List, Optional, Union
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from adapters.alchemy_adapter import AlchemyAdapter
from main.common.repository_interfaces import AbstractReadRepository
from main.database.models import Order


class OrderReadRepository(AbstractReadRepository):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        self._model = Order
        self._session: async_sessionmaker = session_adapter.autocommit_session

    async def get_item(self, uuid: Union[str, UUID]) -> Optional[Order]:
        async with self._session() as session:
            stmt = select(self._model).where(self._model.uuid == uuid)
            answer = await session.execute(stmt)
        return answer.scalar_one_or_none()

    async def get_items(self) -> List[Order]:
        async with self._session() as session:
            stmt = select(self._model).order_by(self._model.created_at)
            answer = await session.execute(stmt)
        return list(answer.scalars().all())
