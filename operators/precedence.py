class OperatorPrecedence:

    def __init__(self):
        self._precedence = self._precedences


    def _precedences(self):
        operators = {"+":1,"-":1,"*":2,"/":2,"^":3,"%":4,"$":5,"&":5,"@":5,"~":6,"!":6,"unary-":7}
        return operators


    def get_operators_precedence(self):
        return self._precedence


    def add_precedence(self,sign:str,precedence:int):
        """
        :param sign: operator sign
        :param precedence: opertor precedences
        :output: updated successfully or failed
        """
        if isinstance(sign,str):
            if isinstance(precedence,int):
                self._precedence[sign] = precedence
                print("Precedence was added successfully!")
            else:
                print("Failed: The precedence has to be a positive integer!")
        else:
            print("Failed: The sign has to be a string!")