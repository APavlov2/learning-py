import os
from sanic.config import Config
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AppConfig(Config):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add('HOST', os.getenv("HOST_IP", "0.0.0.0"))
        self.add('PORT', int(os.getenv("PORT", 8000)))
        self.add('DEBUG', os.getenv("SANIC_ENV", "PRODUCTION") != "PRODUCTION")
        self.add('APP_NAME', os.getenv("APP_NAME", "AppName"))

    def add(self, key: str, value):
        self.update({key.upper(): value})
