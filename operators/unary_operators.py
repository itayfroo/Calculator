from exceptions import FactorialException
from operators.binary_operators import BinaryOperators
class UnaryOperators:

    operators = {"left":["~","-"],"right":["!"]}
    @staticmethod
    def tilda(oper:float) -> float:
        """
        :param oper: float
        :return: -oper
        """
        return BinaryOperators.multiplication(oper,-1)

    @staticmethod
    def factorial(oper: float) -> float:
        """
        :param oper: float
        :return: oper!(if oper<0 return NegativeFactorialException)
        """
        if 0<=oper<2:
            return 1
        if oper<0:
            raise FactorialException("FactorialException: cant take negative factorial!")
        if oper>999:
            raise FactorialException("FactorialException: maximum recursion depth exceeded(supports up to 999!)")
        return BinaryOperators.multiplication(oper,UnaryOperators.factorial(oper-1))

    @staticmethod
    def unary_minus(oper:float) ->float:
        return UnaryOperators.tilda(oper)