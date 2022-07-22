import vars
from enums import ValueTypes, Operators
from exceptions import InvalidValueTypeException, InvalidOperatorException


def convert_to_value_type(value, value_type_from, value_type_to):
    if value_type_from == ValueTypes.METERS and value_type_to == ValueTypes.YARDS:
        return vars.METER_TO_YARDS * value
    elif value_type_from == ValueTypes.YARDS and value_type_to == ValueTypes.METERS:
        return vars.YARD_TO_METERS * value
    return value


def check_value_type(value_type):
    if value_type != ValueTypes.YARDS and value_type != ValueTypes.METERS:
        raise InvalidValueTypeException


def convert_string_to_value_type(value_type_str):
    value_type_str = value_type_str.lower()
    if value_type_str in "meters":
        return ValueTypes.METERS
    elif value_type_str in "yards":
        return ValueTypes.YARDS


def convert_string_to_operator_type(operator_type_str):
    if operator_type_str == "+":
        return Operators.PLUS
    elif operator_type_str == "-":
        return Operators.PLUS
    elif operator_type_str == "*":
        return Operators.PLUS
    elif operator_type_str == "/":
        return Operators.PLUS
    elif operator_type_str == "":
        return None
    raise InvalidOperatorException
