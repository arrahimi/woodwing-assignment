import json


class BaseRoute:
    name = ''
    controller = None

    def __init__(self, app):
        self.app = app
        self.initiate()

    def initiate(self):
        raise NotImplementedError

    def add_route(self, path, func, name, methods=None):
        if methods is None:
            methods = []
        self.app.add_url_rule(path, name, func, methods=methods)

    @staticmethod
    def generate_response(code, message, success, data=None):
        return json.dumps({'success': success, 'message': message, 'data': data}), code,\
               {'ContentType': 'application/json'}
