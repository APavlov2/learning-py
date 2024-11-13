import os
from app.config.db import DbConfig
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

config = DbConfig()

# Define a singleton class for the database connection
class Database:
    _instance = None
    _engine = None
    _SessionLocal = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._engine = create_async_engine(config.get("DB_CONNECTION_STRING"), echo=True)
            cls._SessionLocal = sessionmaker(bind=cls._engine, class_=AsyncSession, expire_on_commit=False)
        return cls._instance

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._SessionLocal

# Initialize the declarative base
Base = declarative_base()

# Singleton instance to be used throughout the application
db_instance = Database()
