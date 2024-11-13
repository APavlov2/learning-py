from app.models.users import User as UserDb
from app.requests.user import User as UserRequest
from app.database.db import db_instance
from sqlalchemy import select

class UserRepository:
    def __init__(self):
        self.model = UserDb

    async def getUsers(self) -> list:
        async with db_instance.session() as session:
            result = await session.execute(select(self.model))
            users = result.scalars().all()
        return [user.__dict__ for user in users]

    async def addUser(self, data: UserRequest) -> UserRequest:
        new_user = self.model(**data.dict())
        async with db_instance.session() as session:
            session.add(new_user)
            await session.commit()
        return UserRequest.from_orm(new_user)

