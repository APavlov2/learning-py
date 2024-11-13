import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DbConfig(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add('DB_HOST', os.getenv("DB_HOST", "localhost"))
        self.add('DB_PORT', int(os.getenv("DB_PORT", 5432)))
        self.add('DB_PASSWORD', os.getenv("DB_PASSWORD"))
        self.add('DB_DATABASE', os.getenv("DB_DATABASE"))
        self.add('DB_USERNAME', os.getenv("DB_USERNAME"))
        self.add('DB_DRIVER', os.getenv("DB_DRIVER"))
        self.buildConnectionString()

    def add(self, key: str, value):
        self.update({key.upper(): value})

    def buildConnectionString(self):
        connection_string = f'{self.get("DB_DRIVER")}+asyncpg://{self.get("DB_USERNAME")}:{self.get("DB_PASSWORD")}@{self.get("DB_HOST")}:{self.get("DB_PORT")}/{self.get("DB_DATABASE")}'
        self.add('DB_CONNECTION_STRING', connection_string)
        