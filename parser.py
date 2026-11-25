class Parser:
    @staticmethod
    def parse_expression(expression: str)  ->str :
        """
        :param expression: string input expression
        :return: expression parsed for calculations
        """
        expression = expression.replace(" ","")
        expression = expression.replace('\t','')
        return expression