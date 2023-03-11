from flask import Flask
from course import response


app = Flask(__name__)

@app.route("/")
def hello():
    return response()

@app.route("/homepage")
def hello_from_home():
    return "Hello from the homepage"