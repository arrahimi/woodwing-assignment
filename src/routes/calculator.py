from routes.base_route import BaseRoute


class CalculatorRoute(BaseRoute):
    name = 'calculator'

    def initiate(self):
        self.add_route('/api/v1/{}/calculate'.format(self.name), CalculatorRoute.calculate, 'calculate',
                       ['POST'])

    @staticmethod
    def calculate():
        return CalculatorRoute.generate_response(200, "success", True)
