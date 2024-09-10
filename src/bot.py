from atproto import AsyncClient, client_utils

class Bot:
    def __init__(self) -> None:
        pass

class BlueskyBot(Bot):
    def __init__(self) -> None:
        super().__init__()
        self.__client = AsyncClient()
        self.__profile = None

    async def connect(self, handler: str, password: str) -> bool:
        try:
            self.__profile = await self.__client.login(handler, password)
            print(f"Welcome, {self.__profile.display_name}")
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    async def post(self, message: str):
        try:
            post = await self.__client.send_post(message)
            return post
        except Exception as e:
            raise e

    async def like(self, uri: str, cid: str):
        try:
            like = await self.__client.like(uri, cid)
            return like
        except Exception as e:
            raise e
