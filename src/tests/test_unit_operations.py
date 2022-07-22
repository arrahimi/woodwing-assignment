import pytest

from enums import ValueTypes, Operators
from operations import Operation


class TestUnitOperations:

    def test_division_by_zero(self):
        """
        tests if division by zero is raised
        """
        total_meters = 2
        op = Operation(ValueTypes.METERS, 0, _type=ValueTypes.YARDS, operator=Operators.DIVIDE)
        with pytest.raises(ZeroDivisionError):
            op.exec(total_meters)

    def test_add(self):
        """
        tests adding values
        """
        total = 0
        result_type = ValueTypes.METERS
        op1 = Operation(result_type, 3, _type=ValueTypes.YARDS, operator=Operators.PLUS)
        op2 = Operation(result_type, 1, _type=ValueTypes.METERS, operator=Operators.PLUS)
        total = op1.exec(total)
        total = op2.exec(total)
        assert total == 3.74

    def test_subtract(self):
        """
        tests subtracting value
        """
        total = 0
        result_type = ValueTypes.YARDS
        op1 = Operation(result_type, 5, _type=ValueTypes.YARDS, operator=Operators.PLUS)
        op2 = Operation(result_type, 3, _type=ValueTypes.METERS, operator=Operators.MINUS)
        total = op1.exec(total)
        total = op2.exec(total)
        assert total == 1.72

    def test_divide(self):
        """
        tests dividing value
        """
        total = 0
        result_type = ValueTypes.YARDS
        op1 = Operation(result_type, 5, _type=ValueTypes.YARDS, operator=Operators.PLUS)
        op2 = Operation(result_type, 3, _type=ValueTypes.METERS, operator=Operators.DIVIDE)
        total = op1.exec(total)
        total = op2.exec(total)
        assert total == 1.52

    def test_multiply(self):
        """
        tests multiplying value
        """
        total = 0
        result_type = ValueTypes.METERS
        op1 = Operation(result_type, 5, _type=ValueTypes.YARDS, operator=Operators.PLUS)
        op2 = Operation(result_type, 3, _type=ValueTypes.YARDS, operator=Operators.MULTIPLY)
        total = op1.exec(total)
        total = op2.exec(total)
        assert total == 12.54
