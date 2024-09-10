from atproto import AsyncFirehoseSubscribeReposClient, parse_subscribe_repos_message, models, CAR
from message_queue import MessageQueue

class FirehoseClient:
    def __init__(self, message_queue: MessageQueue) -> None:
        self.__message_queue = message_queue
        self.__client = AsyncFirehoseSubscribeReposClient()

    async def __on_message_handler(self, message) -> None:
        commit = parse_subscribe_repos_message(message)

        if not isinstance(commit, models.ComAtprotoSyncSubscribeRepos.Commit):
            return

        if not commit.blocks:
            return

        car = CAR.from_bytes(commit.blocks)

        for cid, block in car.blocks.items():

            try:
                if isinstance(block, dict):
                    if '$type' in block:
                        if block['$type'] == 'app.bsky.feed.post':
                            if block.get('langs') and block['langs'][0] == 'pt':
                                if block.get('text'):
                                    self.__message_queue.add_message(block.get('text'))

            except Exception as e:
                print(f"Error processing the block {cid}: {e}")

    async def start(self) -> None:
        await self.__client.start(self.__on_message_handler)
    
    async def stop(self) -> None:
        await self.__client.stop()