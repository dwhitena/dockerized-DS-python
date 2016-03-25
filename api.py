from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from utils import makeprediction

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('slength', type=float, help='slength cannot be converted')
        parser.add_argument('swidth', type=float, help='swidth cannot be converted')
        parser.add_argument('plength', type=float, help='plength cannot be converted')
        parser.add_argument('pwidth', type=float, help='pwidth cannot be converted')
        args = parser.parse_args()

        prediction = makeprediction.predict([
                args['slength'], 
                args['swidth'], 
                args['plength'], 
                args['pwidth']
            ])

        print "THE PREDICTION IS: " + str(prediction)

        return {
                'slength': args['slength'],
                'swidth': args['swidth'],
                'plength': args['plength'],
                'pwidth': args['pwidth'],
                'species': prediction
               }

api.add_resource(Prediction, '/prediction')

if __name__ == '__main__':
    app.run(debug=False)
