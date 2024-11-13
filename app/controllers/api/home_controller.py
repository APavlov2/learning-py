from sanic.response import json
from app.repositories.user import UserRepository
from app.requests.user import User as UserRequest

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
        data = UserRequest(**request.json)
        repo = UserRepository()
        user = await repo.addUser(data)
        return json({"user": user.toJSON()})


