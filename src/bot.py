from atproto import Client

class Bot:
    def __init__(self) -> None:
        self.handler = None
        self.password = None
    
    def connect(self, handler: str, password: str):
        self.handler = handler
        self.password = password

class BlueskyBot(Bot):
    def __init__(self) -> None:
        self.client = Client()
        self.profile = None

    def connect(self, handler: str, password: str):
        self.client.login(handler, password)
        return super().connect(handler, password)
    
    def post(self, message) -> None:
        try:
            post = self.client.send_post(message)
            post.cid
            print(f"Posted: {message}")
            return
        except Exception as e:
            print(f"Error: {e}")
            return
    
    def like(self, uri: str, cid: str) -> None:
        try:
            self.client.like(uri, cid)
            print(f"Liked: {uri}")
            return
        except Exception as e:
            print(f"Error: {e}")
            return