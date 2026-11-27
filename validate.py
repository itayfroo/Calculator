from exceptions import InvalidExpressionException
from operators import unary_operators
from operators.precedence import OperatorPrecedence
from operators.unary_operators import UnaryOperators


class Validate:


    def __init__(self,expression:list):
        self._expression = expression


    @staticmethod
    def check_char_validation(oper: str) -> bool:
        precedences = OperatorPrecedence()
        operators = precedences.get_operators_precedence().keys()
        return oper.isdigit() or oper in operators


    def _check_brackets_validation(self) -> bool:
        """
        :param expression: list of operators and operands
        :return: True if for every '(' there is a ')' else False
        """
        bracket_opener = 0
        for char in self._expression:
            if char == "(":
                bracket_opener += 1
            elif char == ")":
                bracket_opener -= 1
        if bracket_opener == 0:
            return True
        else:
            raise InvalidExpressionException("InvalidExpressionException: Not every '(' has a ')'!")


    def _check_right_unary_operators(self):
        operators = UnaryOperators.operators["right"]
        try:
            for i in range(len(self._expression)):
                if self._expression[i] in operators:
                    if self._expression[i-1] !=")":
                        float(self._expression[i-1])
            return True
        except Exception as e:
            raise InvalidExpressionException(f"InvalidExpressionException: right unary operand has to come after a number!")



    def validate_expression(self):
        return self._check_brackets_validation() and self._check_right_unary_operators()
