from exceptions import InvalidExpressionException
from operators import precedence
import exceptions
from operators.precedence import OperatorPrecedence
class Parser:
    @staticmethod
    def _parse_expression(expression: str)  ->str :
        """
        :param expression: string input expression
        :return: expression parsed for calculations
        """
        expression = expression.replace(" ","")
        expression = expression.replace('\t','')
        return expression


    @staticmethod
    def _check_validation(oper:str) -> bool:
        precedences = OperatorPrecedence()
        operators = precedences.get_operators_precedence().keys()
        return oper.isdigit() or oper in operators

    @staticmethod
    def get_parsed_expression(expression:str) -> list:
        """
        :param expression: string math expression
        :return: parsed list of operands and operators
        """
        expression = Parser._parse_expression(input("Enter an expression: "))
        expression_list = []
        operand_flag = False
        operand = 0
        for x in expression:
            if not Parser._check_validation(x):
                raise InvalidExpressionException("InvalidExpressionException: a non exists operator")
            if x.isdigit():
                operand = operand * 10 + int(x)
                operand_flag = True
            else:
                if operand_flag:
                    expression_list.append(operand)
                    operand_flag = False
                    operand = 0
                expression_list.append(x)
        if operand_flag:
            expression_list.append(operand)
        return expression_list