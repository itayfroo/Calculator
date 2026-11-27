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
            return 0            #לזכור לשנותתתתתתתת
        if oper>999:
            raise RecursionError("maximum recursion depth exceeded")
        return BinaryOperators.multiplication(oper,UnaryOperators.factorial(oper-1))

    @staticmethod
    def unary_minus(oper:float) ->float:
        return UnaryOperators.tilda(oper)