
from sanic import Sanic
from app.controllers.api.home_controller import HomeController
from app.database.db import db_instance

class SessionMiddleware():
    def __init__(self, *args, app: Sanic, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self.init()

    async def inject_session(self, request):
        request.ctx.session = db_instance.session()

    async def close_session(self, request, response):
        await request.ctx.session.close()

    def init(self):
        self._app.register_middleware(self.inject_session, "request")
        self._app.register_middleware(self.close_session, "response")

