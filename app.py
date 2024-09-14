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
from typing import Tuple, List
from logger import Logger

async def process_queue(queue: MessageQueue, process_post: ProcessPost, bot: BlueskyBot, logger: Logger, process_interval = 60):

    if process_interval <= 3600:
        time_str = f"{process_interval / 60:.0f} minutes"
    else:
        time_str = f"{process_interval / 3600:.1f} hours"

    while True:
        logger.printWarning(f"Next processing in {time_str}...")
        await asyncio.sleep(process_interval)

        messages = queue.get_messages()
        logger.print(f"Processing {len(messages)} messages.")

        for message in messages:
            process_post.process_post_text(message)
        
        logger.printSuccess("Processed!")

        result = process_post.get_result()
        trend: List[Tuple[str, int]] = result.most_common(5)
        logger.print(f"Result: {result.most_common(10)}")

        post_message = f""" TRENDING TOPICS

    1. {trend[0][0].capitalize()} #{trend[0][1]}
    2. {trend[1][0].capitalize()} #{trend[1][1]}
    3. {trend[2][0].capitalize()} #{trend[2][1]}
    4. {trend[3][0].capitalize()} #{trend[3][1]}
    5. {trend[4][0].capitalize()} #{trend[4][1]}
         """
        
        try:
            post = await bot.post(post_message)
            logger.printSuccess(f"Posted: {post.uri} {post_message}")
        except Exception as e:
            logger.printError(f"Error: {e}")
            break
        finally:
            process_post.reset()
            logger.print("Reseted!")


async def main():
    logger = Logger()

    load_dotenv()
    SOCIAL_HANDLER = os.getenv("SOCIAL_HANDLER")
    SOCIAL_PASSWORD = os.getenv("SOCIAL_PASSWORD")
    QUEUE_MAX_SIZE = os.getenv("QUEUE_MAX_SIZE")
    PROCESS_INTERVAL = os.getenv("PROCESS_INTERVAL")

    if not SOCIAL_HANDLER:
        logger.print("HANDLER variable is not set. Exiting.")
        return

    if not SOCIAL_PASSWORD:
        logger.print("PASSWORD variable is not set. Exiting.")
        return
        
    if not QUEUE_MAX_SIZE:
        logger.print("MAX_SIZE variable is not set. Exiting.")
        return

    if not PROCESS_INTERVAL:
        logger.print("PROCESS_INTERVAL is not set. Exiting.")
        return
    
    bot = BlueskyBot()
    
    logger.print("Connecting...")
    if not await bot.connect(SOCIAL_HANDLER, SOCIAL_PASSWORD):
        logger.printError("Failed to connect to Bluesky. Exiting.")
        return

    
    logger.print("Starting FirehoseClient...")
    message_queue = MessageQueue(max_size=int(QUEUE_MAX_SIZE))
    firehose = FirehoseClient(message_queue=message_queue)
    firehose_task = asyncio.create_task(firehose.start())
    logger.printSuccess("FirehoseClient has been started.")
    
    logger.print("Starting queue processing...")
    process_post = ProcessPost(stop_words=stop_words)  
    queue_task = asyncio.create_task(process_queue(message_queue, process_post=process_post, bot=bot, logger=logger, process_interval=int(PROCESS_INTERVAL)))
    logger.printSuccess("Processing has been started.")

    async def shutdown():
        logger.print("Shutting down...")
        try:
            await firehose.stop()
        except Exception as e:
            logger.printError(f"Error stopping Firehose: {e}")
        
        firehose_task.cancel()
        queue_task.cancel()

    try:
        await firehose_task
        await queue_task
    except (asyncio.CancelledError, KeyboardInterrupt):
        await shutdown()

if __name__ == "__main__":
    webserver.keep_alive()
    asyncio.run(main())
