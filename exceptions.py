from typing import override


class InvalidExpressionException(Exception):

    def __init__(self,message:str=""):
        super().__init__()
        self.__message = f"InvalidExpressionException: {message}"


    def get_message(self):
        return self.__message


class FactorialException(InvalidExpressionException):
    def __init__(self,message:str =""):
        super().__init__(f"FactorialException: {message}")




class BracketsException(InvalidExpressionException):
    def __init__(self,message:str =""):
        super().__init__(f"BracketsException: {message}")

