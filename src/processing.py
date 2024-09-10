import re
from collections import Counter

class ProcessPost:
    def __init__(self, stop_words: set[str]) -> None:
        self.__stop_words = stop_words
        self.__word_counter = Counter()
        pass
    
    def __preprocess_text(self, text):
        """
        Pré-processa o texto removendo pontuações e convertendo para minúsculas.
        """

        text = re.sub(r'[^\w\s#]|[\d]', '', text)
        text = text.lower()
        return text
    
    def process_post_text(self, text: str) -> None:
        """
        Processa o texto do post, removendo stop-words e atualizando o contador de palavras.
        """

        words = self.__preprocess_text(text).split()
        filtered_words = [word for word in words if word not in self.__stop_words]
    
        self.__word_counter.update(filtered_words)
    
    def get_result(self) -> Counter:
        return self.__word_counter
    
    def reset(self) -> None:
        """
        Reseta o contador de palavras para começar o processamento do zero.
        """
        
        self.__word_counter.clear()
