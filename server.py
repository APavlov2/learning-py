from sanic import Sanic
# from sanic.response import json
from app.config.app import AppConfig
from app.routes.api import APIRoutes

app_config = AppConfig()
app = Sanic(app_config.APP_NAME, config=app_config)

# Serve static files
app.static("/static/", "./app/public/", directory_view=True, name="public_folder")

APIRoutes(app=app)

if __name__ == "__main__":
    app.run(host=app_config.HOST, port=app_config.PORT, dev=app_config.DEBUG)
