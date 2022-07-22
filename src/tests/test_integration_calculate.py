import pytest

from enums import ValueTypes, Operators, Responses
from tests.base_integration_test import BaseIntegrationTest


class TestIntegrationCalculate(BaseIntegrationTest):

    def test_result_object(self, client):
        """
        tests whether the calculation result is correct or not when math is sent as object
        """
        response = client.post("/api/v1/calculator/calculate", json={
            "operations": [
                {
                    "value": 1,
                    "type": ValueTypes.METER
                },
                {
                    "value": 2,
                    "type": ValueTypes.YARDS,
                    "operator": Operators.PLUS
                }
            ],
            "response_type": ValueTypes.METERS
        })
        assert response.json.get("data", {}).get("result") == 2.83

    def test_result_object_result_type_none(self, client):
        """
        tests whether invalid_value_type is sent when result_value_type is invalid
        """
        response = client.post("/api/v1/calculator/calculate", json={
            "operations": [
                {
                    "value": 1,
                    "type": ValueTypes.METER
                },
                {
                    "value": 2,
                    "type": ValueTypes.YARDS,
                    "operator": Operators.PLUS
                }
            ],
            "response_type": None
        })
        assert response.json.get("data", {}).get("result") == Responses.INVALID_VALUE_TYPE

    def test_result_string(self, client):
        """
        tests whether the calculation result is correct or not when math is sent as string
        """
        response = client.post("/api/v1/calculator/calculate", json={
            "operations": "2 Yards + 1 meterS = meter",
        })
        assert response.json.get("data", {}).get("result") == 2.83

    def test_invalid_value_type(self, client):
        """
        tests if a value_type other than yards or meters is detected
        """
        response = client.post("/api/v1/calculator/calculate", json={
            "operations": [
                {
                    "value": 1,
                    "type": ValueTypes.INVALID
                },
                {
                    "value": 2,
                    "type": ValueTypes.YARDS,
                    "operator": Operators.PLUS
                }
            ],
            "response_type": ValueTypes.METERS
        })
        assert response.json.get("data", {}).get("result") == Responses.INVALID_VALUE_TYPE

    def test_invalid_result_value_type(self, client):
        """
        tests if a value_type other than yards or meters is detected
        """
        response = client.post("/api/v1/calculator/calculate", json={
            "operations": [
                {
                    "value": 1,
                    "type": ValueTypes.METERS
                },
                {
                    "value": 2,
                    "type": ValueTypes.YARDS,
                    "operator": Operators.PLUS
                }
            ],
            "response_type": ValueTypes.INVALID
        })
        assert response.json.get("data", {}).get("result") == Responses.INVALID_VALUE_TYPE

    def test_invalid_operator(self, client):
        """
        tests if an operator other than plus, minus, divide or multiple is detected
        """
        response = client.post("/api/v1/calculator/calculate", json={
            "operations": [
                {
                    "value": 1,
                    "type": ValueTypes.METER
                },
                {
                    "value": 2,
                    "type": ValueTypes.YARDS,
                    "operator": Operators.INVALID
                }
            ],
            "response_type": ValueTypes.METERS
        })
        assert response.json.get("data", {}).get("result") == Responses.INVALID_OPERATOR

    def test_zero_division_error(self, client):
        """
        tests if an operator other than plus, minus, divide or multiple is detected
        """
        response = client.post("/api/v1/calculator/calculate", json={
            "operations": [
                {
                    "value": 1,
                    "type": ValueTypes.METER
                },
                {
                    "value": 2,
                    "type": ValueTypes.YARDS,
                    "operator": Operators.MULTIPLY
                },
                {
                    "value": 0,
                    "type": ValueTypes.YARDS,
                    "operator": Operators.DIVIDE
                }
            ],
            "response_type": ValueTypes.METERS
        })
        assert response.json.get("data", {}).get("result") == Responses.ZERO_DIVISION_ERROR

