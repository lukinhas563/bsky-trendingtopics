from atproto import FirehoseSubscribeReposClient, parse_subscribe_repos_message, models, CAR
from collections import Counter
from processing import ProcessPostText

class FirehoseClient:
    def __init__(self, processing: ProcessPostText) -> None:
        self.__processing = processing
        self.__client = FirehoseSubscribeReposClient()
        self.__message_count = 0
        self.__limit = 1000

    def __on_message_handler(self, message) -> None:
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
                                    self.__processing.process_post_text(block.get('text'))

            except Exception as e:
                print(f"Error processing the block {cid}: {e}")
        
        if self.__message_count % 1000 == 0:
            print(f"Processed {self.__message_count} messages")

        # Increment message count and stop if limit is reached
        self.__message_count += 1
        if self.__message_count >= self.__limit:
            print("Finishing process...")
            self.__client.stop()
            self.__message_count = 0

    def start(self, limit=1000) -> None:
        self.__limit = limit
        # Start the client
        self.__client.start(self.__on_message_handler)
    
    def get_result(self) -> Counter:
        return self.__processing.get_result()
