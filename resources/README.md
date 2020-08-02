# Resources

We can add a resource to out API with ```add_resource``` method.


In the following example our *resource* is going to be *Car* object.

<br>

## Create the API app

In the ```main``` file add some extra code to make it as the following:

```py
from flask import Flask
from flask_restful import Api
from resources.car_controller import Car

app = Flask(__name__)
app.config["DEBUG"] = True # in Prod env run with debug=False
api = Api(app) # wrapping the app inside the API

if __name__ == "__main__": # execute only if run as the entry point into the program
    app.run() 
```

Here I have imported ```Api``` object from ```flask_restful``` module. Then have wrapped the app in the API object.

<br>

## Create the Controller

Create a new file and name it ```car_controller```. This class should inherit from ```Resource```.

Add this code to the file:

```py
from flask_restful import Resource

class Car(Resource):

    def get(self):
        return { "make": "Nissan" } 
```

In this code, we have imported the ```Resource``` module which will be inherited by our Class.<br>
Then we create a ```get``` method to handle the ```GET``` HTTP requests to this resource.


The information that is returned back should be ```serializable```. That is why we are returning a JSON object.

<br>

## Register the Resource in the app

Back to ```main.py``` file. Use the API object to add *Car* controller as a resource.

```py
api.add_resource(Car, "/car")
```

The first argument is the class name and second one is the route to access the resource.

<br>

## That's it!

Now if we run the program we can access the *Car* resource from the web browser:

```bash
http://127.0.0.1:5000/car # the browser will send a GET request to this resource
```

Will output:

```json
{
    "make": "Nissan"
}
```

But this was just the beginning. We can now add other types of ```REST``` resources and make them accept arguments.