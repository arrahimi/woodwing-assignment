import re

import utils
from enums import Operators
from exceptions import InvalidOperatorException, InvalidValueTypeException


class Operations:

    re_operations = re.compile("(?P<operation>\s*(?P<operator>\*|\+|\-|\/)?\s*(?P<value>\d+)\s*(?P<value_type>yards?|meters?))")
    re_result = re.compile("=\s*(?P<result_type>meters?|yards?)")

    def __init__(self, raw_operations, result_value_type):
        if isinstance(raw_operations, list):
            self.result_value_type, self.operations = self.get_operations_dict(result_value_type, raw_operations)
        elif isinstance(raw_operations, str):
            self.result_value_type, self.operations = self.get_operations_str(raw_operations)

    def get_operations_dict(self, result_value_type, raw_operations):
        utils.check_value_type(result_value_type)
        return result_value_type, [Operation(result_value_type, op.get("value"), op.get("type"), op.get("operator")) for op in raw_operations]

    def get_operations_str(self, raw_operations):
        raw_operations = raw_operations.lower()
        res = self.re_result.findall(raw_operations)
        if len(res) == 0:
            raise InvalidValueTypeException
        result_value_type = utils.convert_string_to_value_type(res[0])
        if result_value_type is None:
            raise InvalidValueTypeException

        raw_operations_proc = self.re_operations.findall(raw_operations)
        operations = []
        for group in raw_operations_proc:
            value = int(group[2])
            value_type = utils.convert_string_to_value_type(group[3])
            operator = utils.convert_string_to_operator_type(group[1])
            operations.append(Operation(result_value_type, value, value_type, operator))
        return result_value_type, operations

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
