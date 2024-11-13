from app.models.users import User
from app.database.db import db_instance
from sqlalchemy import select

class UserRepository:
    def __init__(self):
        self.model = User

    async def getUsers(self) -> list:
        async with db_instance.session() as session:
            result = await session.execute(select(self.model))
            users = result.scalars().all()
        return [user.__dict__ for user in users]

    async def addUser(self, data) -> User:
        new_user = User(name=data["name"], fullname=data["fullname"], email=data["email"])
        async with db_instance.session() as session:
            session.add(new_user)
            await session.commit()
        return new_user

