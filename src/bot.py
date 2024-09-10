from atproto import AsyncClient

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

    def post(self, message: str) -> None:
        try:
            #post = self.__client.send_post(message)
            print(f"Posted: {message}")
        except Exception as e:
            print(f"Error posting message: {e}")

    async def like(self, uri: str, cid: str) -> None:
        try:
            await self.__client.like(uri, cid)
            print(f"Liked: {uri}")
        except Exception as e:
            print(f"Error liking post: {e}")
