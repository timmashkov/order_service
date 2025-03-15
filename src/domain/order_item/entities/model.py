from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from main.common.patched_filter import PatchedFilter
from main.database.models import OrderItem


class OrderItemIncomingData(BaseModel):
    quantity: int = Field(description=OrderItem.quantity.comment)
    order_id: UUID = Field(description=OrderItem.order_id.comment)
    item_uuid: UUID = Field(description=OrderItem.item_uuid.comment)


class OrderItemResultData(OrderItemIncomingData):
    uuid: UUID = Field(description=OrderItem.uuid.comment)
    created_at: datetime = Field(description=OrderItem.created_at.comment)
    updated_at: datetime = Field(description=OrderItem.updated_at.comment)


class OrderItemFilter(PatchedFilter):
    uuid: Optional[UUID] = None
    quantity: Optional[int] = None
    order_id: Optional[UUID] = None
    item_uuid: Optional[UUID] = None

    class Constants(PatchedFilter.Constants):
        model = OrderItem
