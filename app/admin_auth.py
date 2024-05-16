from starlette.requests import Request
from starlette.responses import RedirectResponse
from sqladmin.authentication import AuthenticationBackend


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        # Здесь должна быть проверка пользователя по базе данных или другой системе
        # Но для примера используем фиксированный логин и пароль
        if username == "ftcadminstate" and password == "paslintyerypin9874678763":
            request.session.update({"user_id": 1})  # здесь может быть любой идентификатор пользователя
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()  # очищаем сессию для выхода пользователя
        return True

    async def authenticate(self, request: Request) -> bool:
        user_id = request.session.get("user_id")
        # Если в сессии нет user_id, значит пользователь не аутентифицирован
        return user_id is not None
