from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from domain.order.entities.enums import OrderStatus, PaymentMethod


@dataclass(frozen=True)
class CreateOrderDTO:
    user_uuid: UUID
    status: OrderStatus
    address: str
    price: Decimal
    is_payed: bool
    pay_method: PaymentMethod
    comment: str
    created_at: datetime
    updated_at: datetime
