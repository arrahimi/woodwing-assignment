import pytest

from app import create_app


class BaseIntegrationTest:

    @pytest.fixture()
    def app(self):
        app = create_app()
        app.config.update({"TESTING": True})
        yield app

    @pytest.fixture()
    def client(self, app):
        return app.test_client()
