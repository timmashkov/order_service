from enum import Enum


class OrderStatus(Enum):
    CREATED: str = "CREATED"
    PROCESSING: str = "PROCESSING"
    READY: str = "READY"
    CANCELED: str = "CANCELED"

    @property
    def description(self) -> str:
        if self == self.CREATED:
            return "Создан"
        if self == self.PROCESSING:
            return "В обработке"
        if self == self.READY:
            return "Готов"
        if self == self.CANCELED:
            return "Отменен"
        return ""


class PaymentMethod(Enum):
    CASH: str = "CASH"
    CARD: str = "CARD"

    @property
    def description(self) -> str:
        if self == self.CASH:
            return "Наличными"
        if self == self.CARD:
            return "Картой"
        return ""
