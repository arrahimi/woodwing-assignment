import utils
from enums import Operators
from exceptions import InvalidOperatorException


class Operations:

    def __init__(self, raw_operations, result_value_type):
        self.result_value_type = result_value_type
        utils.check_value_type(result_value_type)
        self.operations = [Operation(result_value_type, op.get("value"), op.get("type"), op.get("operator")) for op in raw_operations]

    def calculate(self):
        """
        execute all operations
        :return: the total value with the expected value type when all operations are executed
        """
        result = 0
        for operation in self.operations:
            result = operation.exec(result)
        return result


class Operation:

    def __init__(self, normalized_value_type, value, _type, operator=None):
        utils.check_value_type(_type)
        self.value = value
        self.type = _type
        self.operator = operator
        self.normalized_value = utils.convert_to_value_type(value, self.type, normalized_value_type)

    def exec(self, total_value):
        """
        executed this operation by using the value and operator
        :param total_value: the total value that has been calculated before this operation is executed
        :return: the total value after this operation is executed
        """
        if self.operator == Operators.PLUS:
            total_value += self.normalized_value
        elif self.operator == Operators.MINUS:
            total_value -= self.normalized_value
        elif self.operator == Operators.MULTIPLY:
            total_value *= self.normalized_value
        elif self.operator == Operators.DIVIDE:
            total_value /= self.normalized_value
        elif self.operator is None:
            total_value = self.normalized_value
        else:
            raise InvalidOperatorException
        return round(total_value, 2)
