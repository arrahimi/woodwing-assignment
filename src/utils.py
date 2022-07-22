import vars
from enums import ValueTypes
from exceptions import InvalidValueTypeException


def convert_to_value_type(value, value_type_from, value_type_to):
    if value_type_from == ValueTypes.METERS and value_type_to == ValueTypes.YARDS:
        return vars.METER_TO_YARDS * value
    elif value_type_from == ValueTypes.YARDS and value_type_to == ValueTypes.METERS:
        return vars.YARD_TO_METERS * value
    return value


def check_value_type(value_type):
    if value_type != ValueTypes.YARDS and value_type != ValueTypes.METERS:
        raise InvalidValueTypeException
