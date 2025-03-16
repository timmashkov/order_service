from adapters.alchemy_adapter import AlchemyAdapter
from adapters.rabbit_adapter import RabbitMQAdapter
from application.config import settings
from domain.order.repositories.read_repository import OrderReadRepository
from domain.order.repositories.write_repository import OrderWriteRepository
from domain.order_item.repositories.read_repository import OrderItemReadRepository
from domain.order_item.repositories.write_repository import OrderItemWriteRepository
from main.common.base_entities.singleton import OnlyContainer, Singleton


class Container(Singleton):

    alchemy_manager = OnlyContainer(
        AlchemyAdapter,
        dialect=settings.POSTGRES.dialect,
        host=settings.POSTGRES.host,
        login=settings.POSTGRES.login,
        password=settings.POSTGRES.password,
        port=settings.POSTGRES.port,
        database=settings.POSTGRES.database,
        echo=settings.POSTGRES.echo,
    )

    rabbit_manager = OnlyContainer(
        RabbitMQAdapter,
        **settings.RABBIT_MQ,
    )

    order_write_manager = OnlyContainer(
        OrderWriteRepository,
        session_adapter=alchemy_manager(),
    )

    order_read_manager = OnlyContainer(
        OrderReadRepository,
        session_adapter=alchemy_manager(),
    )

    order_item_read_manager = OnlyContainer(
        OrderItemReadRepository,
        session_adapter=alchemy_manager(),
    )

    order_item_write_manager = OnlyContainer(
        OrderItemWriteRepository,
        session_adapter=alchemy_manager(),
    )
