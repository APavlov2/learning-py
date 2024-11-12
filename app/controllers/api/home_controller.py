from sanic.response import json

class HomeController:
    # create addNumbers static method
    @staticmethod
    def index(request):
        return json({"message": "Hello, Worlds!"})

    @staticmethod
    def tasks_list(request):
        return json({"tasks": [
            {
                "id": 1,
                "title": "Learn Python intro.",
                "description": "Learning python starts from the beginning."
            },
            {
                "id": 2,
                "title": "Learn Python.",
                "description": "Next is learning DB connection."
            }
        ]})


