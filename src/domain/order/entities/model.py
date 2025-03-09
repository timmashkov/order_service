from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from domain.order.entities.enums import OrderStatus, PaymentMethod


class OrderIncomingData(BaseModel):
    user_uuid: UUID
    status: OrderStatus
    address: str
    price: Decimal
    is_payed: bool
    pay_method: PaymentMethod
    comment: str


class OrderResultData(OrderIncomingData):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
