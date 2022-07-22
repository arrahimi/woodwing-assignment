import pytest

from enums import ValueTypes, Operators
from tests.base_test import BaseTest
from vars import VALUE_TYPE_TO_INT, OPERATOR_TO_INT


class TestRequest(BaseTest):

    @pytest.mark.usefixtures("client")
    def test_request(self, client):
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
            "response_type": VALUE_TYPE_TO_INT["meter"]
        })
        assert response.json.get("data", {}).get("result") == 2.8288
