from flask import Flask
from flask_restful import Resource, Api

class Div(Resource):
    def get(self, a, b):
        try:
            return {'result': int(a) / int(b)}
        except:
            return {'result': 'Error'}

app = Flask(__name__)
api = Api(app)

api.add_resource(Div, '/<a>/<b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )