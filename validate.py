from exceptions import InvalidExpressionException, BracketsException
from operators import unary_operators
from operators.precedence import OperatorPrecedence
from operators.unary_operators import UnaryOperators


class Validate:


    def __init__(self,expression:list):
        self._expression = expression


    @staticmethod
    def check_char_validation(oper: str,operators) -> bool:
        return oper.isdigit() or oper in operators


    def _check_brackets_validation(self) -> bool:
        """
        :param expression: list of operators and operands
        :return: True if for every '(' there is a ')' else False
        """
        brackets = []
        last =''
        for char in self._expression:
            if char == "(":
                if last!='' and last not in OperatorPrecedence().get_operators_precedence().keys():
                    raise BracketsException("'(' came after no operator!")
                brackets.append(char)

            elif char == ")":
                if len(brackets)==0:
                    raise BracketsException("')' came before a '(' !")
                elif last=="(":
                    raise BracketsException("Empty brackets '()'!")
                brackets.pop()
            last=char
        if len(brackets) == 0:
            return True
        else:
            raise BracketsException("Not every '(' has a ')'!")


    def _check_right_unary_operators(self):
        operators = UnaryOperators.operators["right"]
        for i in range(len(self._expression)):
            if self._expression[i] in operators:
                if i == 0:
                    raise InvalidExpressionException(f"'{self._expression[i]}' cant be first in expression!")
                if self._expression[i-1] !=")":
                    try:
                        float(self._expression[i-1])
                    except:
                        raise InvalidExpressionException(f"Right unary operand has to come after a number!")
        return True




    def validate_expression(self):
        return self._check_brackets_validation() and self._check_right_unary_operators()
