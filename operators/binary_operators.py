class BinaryOperators:

    @staticmethod
    def addition(oper1:float,oper2:float) -> float :
        """
        :param oper1: float
        :param oper2: float
        :return: oper1+oper2
        """
        return oper1+oper2

    @staticmethod
    def substruction(oper1:float,oper2:float) -> float :
        """
        :param oper1: float
        :param oper2: float
        :return: oper1-oper2
        """
        return oper1-oper2

    @staticmethod
    def multiplication(oper1:float,oper2:float) -> float :
        """
        :param oper1: float
        :param oper2: float
        :return: oper1*oper2
        """
        return oper1*oper2

    @staticmethod
    def devision(oper1:float,oper2:float) ->float :
        """
        :param oper1: float
        :param oper2: float
        :return: oper1/oper2(if oper2==0 return DevisionByZeroException)
        """
        result=0
        try:
           result=oper1/oper2
           return result
        except ArithmeticError as e:
            raise ArithmeticError("Can't devide by zero!")


    @staticmethod
    def power(oper1:float,oper2:float) ->float:
        """
        :param oper1: float
        :param oper2: float
        :return: oper1^oper2
        """
        return pow(oper1,oper2)

    @staticmethod
    def modulu(oper1: float, oper2: float) -> float:
        """
        :param oper1: float
        :param oper2: float
        :return: oper1 % oper2(if oper2==0 return DevisionByZeroException)
        """
        result = 0
        try:
            result = oper1 % oper2
            return result
        except ArithmeticError as e:
            raise ArithmeticError("Can't modulu by zero!")

    @staticmethod
    def maximum(oper1:float,oper2:float) ->float:
        """
        :param oper1: float
        :param oper2: float
        :return: max(oper1,oper2)
        """
        return oper1 if oper1>oper2 else oper2

    @staticmethod
    def minimum(oper1:float,oper2:float) ->float:
        """
        :param oper1: float
        :param oper2: float
        :return: min(oper1,oper2)
        """
        return oper2 if oper1>oper2 else oper1


    @staticmethod
    def average(oper1:float,oper2:float) ->float:
        """
        :param oper1: float
        :param oper2: float
        :return: average(oper1,oper2)
        """
        return BinaryOperators.devision(BinaryOperators.addition(oper1,oper2),2)