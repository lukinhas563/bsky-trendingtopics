from atproto import FirehoseSubscribeReposClient

class FirehoseClient:
    def __init__(self) -> None:
        self.client = FirehoseSubscribeReposClient()
        pass

    def start(self) -> None:
        self.client.start()
        return