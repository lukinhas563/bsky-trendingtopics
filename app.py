import os
import sys
import asyncio
import webserver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from message_queue import MessageQueue
from src.firehoseClient import FirehoseClient
from src.bot import BlueskyBot
from src.processing import ProcessPost
from src.utils.stopWords import stop_words
from dotenv import load_dotenv

async def process_queue(queue: MessageQueue, process_post: ProcessPost):
    while True:
        print("Next processing in 1 minute...")
        await asyncio.sleep(60)

        messages = queue.get_messages()
        print(f"Processing {len(messages)} messages.")

        for message in messages:
            process_post.process_post_text(message)
        
        print("Processed!")
        result = process_post.get_result()

        print(f"Result: {result.most_common(5)}")

        process_post.reset()

async def main():
    load_dotenv()
    SOCIAL_HANDLER = os.getenv("SOCIAL_HANDLER")
    SOCIAL_PASSWORD = os.getenv("SOCIAL_PASSWORD")
    bot = BlueskyBot()

    print("Connecting...")
    if not await bot.connect(SOCIAL_HANDLER, SOCIAL_PASSWORD):
        print("Failed to connect to Bluesky. Exiting.")
        return

    message_queue = MessageQueue(max_size=1000)
    firehose = FirehoseClient(message_queue=message_queue)

    print("Starting FirehoseClient...")
    firehose_task = asyncio.create_task(firehose.start())
    print("FirehoseClient has been started.")
    
    print("Starting queue processing...")
    queue_task = asyncio.create_task(process_queue(message_queue, process_post=ProcessPost(stop_words=stop_words)))
    print("Processing has been started.")

    async def shutdown():
        print("Shutting down...")
        await firehose.stop()
        firehose_task.cancel()
        queue_task.cancel()

    try:
        await firehose_task
        await queue_task
    except (asyncio.CancelledError, KeyboardInterrupt):
        await shutdown()

if __name__ == "__main__":
    asyncio.run(main())
