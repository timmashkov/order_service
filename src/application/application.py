from application.config import settings
from application.container import Container
from application.server import ApiServer
from presentation.api.order_item_router import OrderItemRouter
from presentation.api.order_router import OrderRouter

order_app = ApiServer(
    name=settings.NAME,
    routers=[OrderRouter().api_router, OrderItemRouter().api_router],
    start_callbacks=[
        Container.broker_process_manager().start_broker_process,
        Container.rabbit_manager().connect,
        Container.rabbit_manager().init_queues,
    ],
    stop_callbacks=[Container.broker_process_manager().stop_broker_process],
).app
