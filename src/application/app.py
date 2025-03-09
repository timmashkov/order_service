from application.config import settings
from application.server import ApiServer

order_app = ApiServer(
    name=settings.NAME,
    routers=[],
    start_callbacks=[],
    stop_callbacks=[],
).app
