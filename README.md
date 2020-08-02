# REST APIs with Python

In this series I'm going to explore exposing and consuming REST APIs along with authentication part of these integrations.

### Required libraries

I will be using these libraries:
* **flask** - a micro web framework.
* **requests** - allows sending HTTP requests.
* **venv** - creating lightweight virtual environments.

<br>

## Table of Contents

0. Installation
1. Resources
2. Requests

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
$ pip install -r requirements.txt # list of any module required for the project
```

Check for installed packages with:

```bash
$ pip list
```

<br>

### Initialize the App

Create a file called ```main.py```. This is the main entry point to the program.

Add this code to ```main.py```:

```py
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True # in Prod env run with debug=False

if __name__ == "__main__":
    app.run()
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

#### References

* [Python REST API Tutorial - Building a Flask REST API](https://www.youtube.com/watch?v=GMppyAPbLYk)
