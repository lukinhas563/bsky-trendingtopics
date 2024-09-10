from typing import Any
from collections import deque

class MessageQueue:
    def __init__(self, max_size = 1000) -> None:
        self.queue = deque(maxlen=max_size)

    def add_message(self, message) -> None:
        self.queue.append(message)
    
    def get_messages(self) -> list[Any]:
        return list(self.queue)