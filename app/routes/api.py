
from sanic import Sanic
from app.controllers.api.home_controller import HomeController

class APIRoutes():
    def __init__(self, *args, app: Sanic, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self.init()

    def init(self):
        self._app.add_route(
            HomeController.index,
            '/'
        )
        self._app.add_route(
            HomeController.user_list,
            '/user/list',
            methods=["GET"],
        )
        self._app.add_route(
            HomeController.user_add,
            '/user/add',
            methods=["POST"],
        )