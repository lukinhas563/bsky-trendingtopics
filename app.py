import os
import sys
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from src.firehoseClient import FirehoseClient
from src.processing import ProcessPostText
from src.utils.stopWords import stop_words

async def main():
    firehose = FirehoseClient(processing=ProcessPostText(stop_words))

    await firehose.start(limit=1000)

    result = firehose.get_result()

    print("\nTrending Topics:")
    for i, (word, count) in enumerate(result.most_common(5), start=1):
        print(f"{i}. {word}: {count} vezes")

if __name__ == "__main__":
    asyncio.run(main())
