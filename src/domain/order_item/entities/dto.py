from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateOrderItemDTO:
    quantity: int
    order_id: UUID
    item_uuid: UUID
