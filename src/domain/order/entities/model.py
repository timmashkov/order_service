from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from domain.order.entities.enums import OrderStatus, PaymentMethod
from domain.order_item.entities.model import OrderItemResultData
from main.common.base_entities.patched_filter import PatchedFilter
from main.database.models import Order


class OrderIncomingData(BaseModel):
    user_uuid: UUID = Field(description=Order.uuid.comment)
    status: OrderStatus = Field(
        default=OrderStatus.CREATED, description=Order.status.comment
    )
    address: str = Field(description=Order.address.comment)
    price: Decimal = Field(description=Order.price.comment)
    is_payed: bool = Field(description=Order.is_payed.comment)
    pay_method: PaymentMethod = Field(
        default=PaymentMethod.CARD, description=Order.pay_method.comment
    )
    comment: str = Field(description=Order.comment.comment)
    items: Optional[List[OrderItemResultData]]


class OrderResultData(OrderIncomingData):
    uuid: UUID = Field(description=Order.uuid.comment)
    created_at: datetime = Field(description=Order.created_at.comment)
    updated_at: datetime = Field(description=Order.updated_at.comment)


class OrderFilter(PatchedFilter):
    uuid: Optional[UUID] = None
    status: Optional[OrderStatus] = None
    address: Optional[str] = None
    price: Optional[Decimal] = None
    is_payed: Optional[bool] = None
    pay_method: Optional[PaymentMethod] = None
    comment: Optional[str] = None

    class Constants(PatchedFilter.Constants):
        model = Order
