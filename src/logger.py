from datetime import datetime
from colorama import Fore, init

class Logger:
    def __init__(self) -> None:
        self.__colors = {"yellow": Fore.YELLOW, "green": Fore.GREEN, "reset": Fore.RESET}
        init()

    def print(self, message: str) -> None:
        DATETIME = datetime.now()
        DATE = DATETIME.strftime("%d/%m/%Y")
        TIME = DATETIME.strftime("%H:%M")

        print(f"({self.__colors['green']}{DATE}{self.__colors['reset']}) [{self.__colors['yellow']}{TIME}{self.__colors['reset']}] {message}")