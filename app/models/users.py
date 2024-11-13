import json
from app.database.db import Base
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    email: Mapped[str] = mapped_column(String, unique=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}, email={self.email!r})"

    def toJSON(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "fullname": self.fullname,
            "email": self.email
        }
