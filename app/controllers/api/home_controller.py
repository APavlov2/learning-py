from sanic.response import json
from app.models.users import User
from app.repositories.user import UserRepository

class HomeController:
    # create addNumbers static method
    @staticmethod
    def index(request):
        return json({"message": "Hello, Worlds!"})

    @staticmethod
    async def user_list(request):
        repo = UserRepository()
        return json({"users": await repo.getUsers()})

    @staticmethod
    async def user_add(request):
        data = request.json
        repo = UserRepository()
        user = await repo.addUser(data)
        return json({"user": user.toJSON()})


