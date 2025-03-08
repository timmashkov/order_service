import uuid
from decimal import Decimal

from sqlalchemy import DECIMAL, Boolean, String, Text
from sqlalchemy.dialects.postgresql import ENUM, UUID
from sqlalchemy.orm import Mapped, mapped_column

from domain.order.entities.enums import OrderStatus, PaymentMethod
from src.infrastructure.database.models.base import Base


class Order(Base):

    user_uuid: Mapped[uuid.UUID] = mapped_column(
        UUID, nullable=False, unique=True, index=True, comment="Айди пользователя"
    )
    status: Mapped[OrderStatus] = mapped_column(
        ENUM(OrderStatus, name="order_status"), comment="Статус заказа"
    )
    address: Mapped[str] = mapped_column(Text, nullable=False, comment="Адрес доставки")
    price: Mapped[Decimal] = mapped_column(
        DECIMAL, nullable=False, comment="Стоимость заказа"
    )
    is_payed: Mapped[bool] = mapped_column(
        Boolean, default=False, comment="Оплачен ли заказ"
    )
    pay_method: Mapped[PaymentMethod] = mapped_column(
        ENUM(PaymentMethod, name="pay_method"), comment="Способ оплаты"
    )
    comment: Mapped[str] = mapped_column(String, comment="Комментарий к заказу")
