from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app) # wrapping the app inside the API

if __name__ == "__main__":
    app.run(debug=True) # in Prod env run with debug=False
