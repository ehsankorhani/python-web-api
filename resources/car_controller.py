from flask_restful import Resource

class Car(Resource):

    def get(self):
        return { "make": "Nissan" } 

