from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from domain.order.entities.model import OrderResultData


class OrderItemIncomingData(BaseModel):
    quantity: int
    order_id: UUID
    item_uuid: UUID


class OrderItemResultData(OrderItemIncomingData):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    order: Optional[OrderResultData]
