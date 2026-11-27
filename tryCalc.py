from parser import Parser
from exceptions import InvalidExpressionException

while True:
    try:
        expression = Parser.get_parsed_expression(input("Enter Expression: "))
        print(expression)
    except InvalidExpressionException as e:
        print(e.get_message())