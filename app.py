import os
import sys
import schedule
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from src.firehoseClient import FirehoseClient
from src.processing import ProcessPostText
from src.bot import BlueskyBot
from src.utils.stopWords import stop_words
from dotenv import load_dotenv
from datetime import datetime
from functools import partial
import webserver

def trending_topics(firehose: FirehoseClient, bot: BlueskyBot, limit=1000):
    firehose.reset()
    firehose.start(limit)

    result = firehose.get_result()

    trends = result.most_common(5)
    print(result.most_common(40))

    date = datetime.now()
    message = f"""
    🔥 Trending Topics 🔥
    📅 {date.strftime("%d/%m/%Y")} 🕝 {date.strftime("%H:%M")}

    1. {trends[0][0]} #{trends[0][1]}
    2. {trends[1][0]} #{trends[1][1]}
    3. {trends[2][0]} #{trends[2][1]}
    4. {trends[3][0]} #{trends[3][1]}
    5. {trends[4][0]} #{trends[4][1]}
    """

    bot.post(message)

def main():
    load_dotenv()
    SOCIAL_HANDLER = os.getenv("SOCIAL_HANDLER")
    SOCIAL_PASSWORD = os.getenv("SOCIAL_PASSWORD")
    bot = BlueskyBot()

    if not bot.connect(SOCIAL_HANDLER, SOCIAL_PASSWORD):
        print("Failed to connect to Bluesky. Exiting.")
        return
    
    firehose = FirehoseClient(processing=ProcessPostText(stop_words))

    print("Starting...")

    # Agendando para rodar a cada 14 minutos
    schedule.every(14).minutes.do(partial(trending_topics, firehose, bot, limit=500000))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    webserver.keep_alive()
    
    main()
