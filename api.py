from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

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

        prediction = predict([[
                args['slength'], 
                args['swidth'], 
                args['plength'], 
                args['pwidth']
            ]])

        return {
                'slength': args['slength'],
                'swidth': args['swidth'],
                'plength': args['plength'],
                'pwidth': args['pwidth'],
                'species': prediction
               }

def predict(inputFeatures):

    iris = datasets.load_iris()

    knn = KNeighborsClassifier()
    knn.fit(iris.data, iris.target)

    predictInt = knn.predict(inputFeatures)
    if predictInt[0] == 0:
        predictString = 'setosa'
    elif predictInt[0] == 1:
        predictString = 'versicolor'
    elif predictInt[0] == 2:
        predictString = 'virginica'
    else:
        predictString = 'null'

    return predictString

api.add_resource(Prediction, '/prediction')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
