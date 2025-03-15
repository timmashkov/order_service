from application.config import settings
from application.server import ApiServer
from presentation.api.order_item_router import OrderItemRouter
from presentation.api.order_router import OrderRouter

order_app = ApiServer(
    name=settings.NAME,
    routers=[OrderRouter().api_router, OrderItemRouter().api_router],
    start_callbacks=[],
    stop_callbacks=[],
).app
