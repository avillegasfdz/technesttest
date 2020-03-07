class OddException(Exception):
    """ Exception class for odd numbers"""


class OddSum:
    """ Static class to implement the sum of two odd numbers"""

    @staticmethod
    def sum(number1, number2):
        """
        Adds two odd numbers
        :param number1: first number to add. Must be int.
        :param number2: second number to add. Must be int.
        :return: The sum or raises OddException
        """

        error_string = ""
        if number1 % 2 == 0:
            error_string += str(number1) + " is even. "
        if number2 % 2 == 0:
            error_string += str(number2) + " is even. "
        if error_string != "":
            raise OddException(error_string)
        else:
           return number1 + number2
