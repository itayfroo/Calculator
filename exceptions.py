class InvalidExpressionException(Exception):

    def __init__(self,message:str):
        super().__init__()
        self.__message = message


    def get_message(self):
        return self.__message