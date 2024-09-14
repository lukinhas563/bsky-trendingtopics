from datetime import datetime
from colorama import Fore, init, Back
from typing import Tuple

class Logger:
    def __init__(self) -> None:
        self.__colors = {"yellow": Fore.YELLOW, "green": Fore.GREEN, "red": Fore.RED, "white": Fore.WHITE, "reset": Fore.RESET}
        self.__background = {"yellow": Back.YELLOW, "green": Back.GREEN, "red": Back.RED, "white": Back.WHITE, "reset": Back.RESET}
        init(autoreset=True)

    def __getDate(self) -> Tuple[str, str]:
        DATETIME = datetime.now()
        DATE = DATETIME.strftime("%d/%m/%Y")
        TIME = DATETIME.strftime("%H:%M")
    
        return (DATE, TIME)

    def print(self, message: str) -> None:
        DATE, TIME = self.__getDate()

        print(f"({self.__colors['green']}{DATE}{self.__colors['reset']}) [{self.__colors['yellow']}{TIME}{self.__colors['reset']}] {message}")
    
    def printError(self, message: str) -> None:
        DATE, TIME = self.__getDate()

        reset_color = self.__colors['reset']
        reset_background = self.__background['reset']
        date_color = self.__colors['green']
        time_color = self.__colors['yellow']
        background = self.__background['red']
        error_color = self.__colors['white']
        message_color = self.__colors['red']

        print(f"({date_color}{DATE}{reset_color}) [{time_color}{TIME}{reset_color}] {background}{error_color} Error! {reset_background}{reset_color} {message_color}{message}")

    def printSuccess(self, message: str) -> None:
        DATE, TIME = self.__getDate()

        reset_color = self.__colors['reset']
        reset_background = self.__background['reset']
        date_color = self.__colors['green']
        time_color = self.__colors['yellow']
        background = self.__background['green']
        sucess_color = self.__colors['white']
        message_color = self.__colors['green']

        print(f"({date_color}{DATE}{reset_color}) [{time_color}{TIME}{reset_color}] {background}{sucess_color} Success! {reset_background}{reset_color} {message_color}{message}")

    def printWarning(self, message: str) -> None:
        DATE, TIME = self.__getDate()

        reset_color = self.__colors['reset']
        reset_background = self.__background['reset']
        date_color = self.__colors['green']
        time_color = self.__colors['yellow']
        background = self.__background['yellow']
        warning_color = self.__colors['white']
        message_color = self.__colors['yellow']

        print(f"({date_color}{DATE}{reset_color}) [{time_color}{TIME}{reset_color}] {background}{warning_color} Warning! {reset_background}{reset_color} {message_color}{message}")