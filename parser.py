from exceptions import InvalidExpressionException
from validate import Validate


class Parser:


    @staticmethod
    def _parse_expression_spaces_tabs(expression: str)  ->str :
        """
        :param expression: string input expression
        :return: expression parsed from spaces and tabs
        """
        expression = expression.replace(" ","")
        expression = expression.replace('\t','')
        return expression


    @staticmethod
    def _parsed_expression_list(expression:str) -> list:
        """
        :param expression: string math expression
        :return: parsed list of operands and operators
        """
        parsed_expression = Parser._parse_expression_spaces_tabs(expression)
        expression_list = []
        operand_flag = False
        operand = 0
        for x in parsed_expression:
            if not Validate.check_char_validation(x):
                raise InvalidExpressionException(f"InvalidExpressionException: a non exists operator {x}")
            if x.isdigit():
                operand = operand * 10 + float(x)
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


    @staticmethod
    def get_parsed_expression(expression:str) -> list:
        parsed_expression = Parser._parsed_expression_list(expression)
        validation = Validate(parsed_expression)
        validation.validate_expression()
        return parsed_expression



