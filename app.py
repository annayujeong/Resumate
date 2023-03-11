from flask import Flask
from course import response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return response()

@app.route("/homepage")
def hello_from_home():
    return "Hello from the homepage"

@app.route("/temp", methods=['GET'])
def temp_func(temp):
    print(temp)
    return temp
