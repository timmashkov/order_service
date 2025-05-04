from sqlalchemy import select
from sqlalchemy.orm import contains_eager

from adapters.database.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Order, OrderItem
from infrastructure.database.repositories.read_repository import ReadRepository


class OrderReadRepository(ReadRepository):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Order)

    def __get_query(self) -> select:
        query = (
            select(self._model)
            .outerjoin(OrderItem, Order.uuid == OrderItem.order_id)
            .options(contains_eager(Order.items))
        )
        return query
