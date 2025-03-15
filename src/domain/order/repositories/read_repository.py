from typing import Any, Optional, Union
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import contains_eager

from adapters.alchemy_adapter import AlchemyAdapter
from main.common.repository_interfaces import AbstractReadRepository
from main.database.models import Order, OrderItem


class OrderReadRepository(AbstractReadRepository):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        self._model = Order
        self._session: async_sessionmaker = session_adapter.autocommit_session

    @classmethod
    def __set_filter(cls, query: select, filters: Any = None) -> select:
        if filters:
            query = filters.filter(query)
        return query

    def __get_query(self) -> select:
        query = (
            select(self._model)
            .outerjoin(OrderItem, Order.uuid == OrderItem.order_id)
            .options(contains_eager(Order.items))
        )
        return query

    async def get_item(self, uuid: Union[str, UUID]) -> Optional[Order]:
        async with self._session() as session:
            stmt = self.__get_query().where(self._model.uuid == uuid)
            answer = await session.execute(stmt)
        return answer.scalar_one_or_none()

    async def find(
        self,
        filters: Any = None,
    ) -> Union[list, select]:
        query = self.__get_query()
        query = self.__set_filter(query, filters)
        async with self._session() as session:
            result = await session.execute(query)
            return result.scalars().unique().all()
