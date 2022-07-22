from flask import request

from enums import Responses
from exceptions import InvalidOperatorException, InvalidValueTypeException
from operations import Operations
from routes.base_route import BaseRoute


class CalculatorRoute(BaseRoute):
    name = 'calculator'

    def initiate(self):
        self.add_route('/api/v1/{}/calculate'.format(self.name), CalculatorRoute.calculate, 'calculate',
                       ['POST'])

    @staticmethod
    def calculate():
        """
        this route will use the operations class to execute the requested operations
        :return: response with an error or total_value after the operations are executed
        """
        raw_operations = request.json.get('operations', [])
        response_type = request.json['response_type']
        try:
            operations = Operations(raw_operations, response_type)
            result = operations.calculate()
        except InvalidOperatorException:
            return CalculatorRoute.generate_response(200, "success", False, {"result": Responses.INVALID_OPERATOR})
        except InvalidValueTypeException:
            return CalculatorRoute.generate_response(200, "success", False, {"result": Responses.INVALID_VALUE_TYPE})
        except ZeroDivisionError:
            return CalculatorRoute.generate_response(200, "success", False, {"result": Responses.ZERO_DIVISION_ERROR})
        return CalculatorRoute.generate_response(200, "success", True, {"result": result})
