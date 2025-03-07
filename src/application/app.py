from infrastructure.server.config import settings
from infrastructure.server.server import ApiServer

order_app = ApiServer(
    name=settings.NAME,
    routers=[],
    start_callbacks=[],
    stop_callbacks=[],
).app
