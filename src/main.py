import logging

from flask import Flask

from routes.calculator import CalculatorRoute

app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

calculator_route = CalculatorRoute(app)

if __name__ == "__main__":
    app.run('0.0.0.0', 6000, debug=False)
