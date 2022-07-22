import logging

from flask import Flask

from routes.calculator import CalculatorRoute


def create_app():
    app = Flask(__name__)

    gunicorn_error_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers.extend(gunicorn_error_logger.handlers)
    app.logger.setLevel(logging.DEBUG)

    calculator_route = CalculatorRoute(app)
    return app