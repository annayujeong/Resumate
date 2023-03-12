from flask import Flask, request
from course import response
from flask_cors import CORS

from resumeRewriter import rewriteResume
from resumeRewriter import highlightDifferences

app = Flask(__name__)
CORS(app)

@app.route("/courses")
def hello():
    return response()

@app.route("/homepage")
def hello_from_home():
    return "Hello from the homepage"

@app.route("/temp", methods=['POST'])
def temp_func():
    # print(temp)
    return request.data

@app.route("/resumeResults")
def resume():
    #rewriteResume()
    return highlightDifferences()

@app.route("/")
def temp():
    return ("This is the main page!")
