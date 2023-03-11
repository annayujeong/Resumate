from flask import Flask
from course import response
from resumeRewriter import rewriteResume
from resumeRewriter import highlightDifferences

app = Flask(__name__)

@app.route("/courses")
def hello():
    return response()

@app.route("/homepage")
def hello_from_home():
    return "Hello from the homepage"

@app.route("/resumeResults")
def resume():
    #rewriteResume()
    return highlightDifferences()

@app.route("/")
def temp():
    return ("This is the main page!")