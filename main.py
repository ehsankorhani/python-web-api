from flask import Flask
from flask_restful import Api
from resources.car_controller import Car

app = Flask(__name__)
app.config["DEBUG"] = True # in Prod env run with debug=False
api = Api(app) # wrapping the app inside the API

api.add_resource(Car, "/car")

if __name__ == "__main__": # execute only if run as the entry point into the program
    app.run() 