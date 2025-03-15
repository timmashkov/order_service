import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from main.database.models import Base

if TYPE_CHECKING:
    from main.database.models import Order


class OrderItem(Base):

    quantity: Mapped[int] = mapped_column(
        Integer, nullable=False, comment="Количество элементов"
    )

    order_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("orders.uuid", ondelete="CASCADE"),
        nullable=True,
        comment="Айди заказа",
    )

    item_uuid: Mapped[uuid.UUID] = mapped_column(
        UUID, nullable=False, unique=True, index=True, comment="Айди товара"
    )
    order: Mapped["Order"] = relationship(
        "Order", back_populates="items", lazy="noload"
    )
