from sanic import Sanic
from app.config.app import AppConfig
from app.routes.api import APIRoutes
from app.middlewares.session import SessionMiddleware
from app.database.db import db_instance, Base

app_config = AppConfig()
app = Sanic(app_config.APP_NAME, config=app_config)

# Serve static files
app.static("/static/", "./app/public/", directory_view=True, name="public_folder")

# TODO: Move to database/migration folder with a hook class
# Ensure tables are created at startup
@app.listener("before_server_start")
async def setup_db(app, loop):
    async with db_instance.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

SessionMiddleware(app=app)
APIRoutes(app=app)

if __name__ == "__main__":
    app.run(host=app_config.HOST, port=app_config.PORT, dev=app_config.DEBUG)
