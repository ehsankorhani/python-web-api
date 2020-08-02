# REST APIs with Python

In this series I'm going to explore exposing and consuming REST APIs along with authentication part of these integrations.

### Required libraries

I will be using these libraries:
* Flask - a micro web framework.
* ...
* Venv - creating lightweight virtual environments.

<br>

## Table of Contents

0. Installation


<br>

## Installation

### Create a development environment

Create the environment inside an appropriate folder:

```bash
$ python3 -m venv api_env
```

and activate it:

```bash
$ source api_env/bin/activate
```

<br>

### Install dependencies

From the provided file:

```bash
$ pip install -r requirements.txt
```

Check for installed packages with:

```bash
$ pip list
```

<br>

### Initialize the App

Create the ```main.py``` file which is the main entry point to the program.

The main modules to import are:

```py
from flask import Flask
from flask_restful import Api, Resource
```

Create the app withing flask:

```py
app = Flask(__name__)
api = Api(app)
```

and run it:

```py
if __name__ == "__main__":
    app.run(debug=True)
```

In Prod environment run with ```debug=False```.

<br>

### Run and Test

```bash
python3 main.py
```

And you should see the following as the result of the running the application:

```bash
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 503-916-359
```

And the app will be accessible from browser (or any api client) from:<br>
```http://127.0.0.1:5000/ ```


<br>

#### Reference

* [Python REST API Tutorial - Building a Flask REST API](https://www.youtube.com/watch?v=GMppyAPbLYk)