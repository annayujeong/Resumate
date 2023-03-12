import ast
from flask import Flask, request
from course import response
from flask_cors import CORS

from resumeRewriter import rewriteResume
# from resumeRewriter import highlightDifferences

app = Flask(__name__)
CORS(app)

@app.route("/job_resume/", methods=['POST'])
def job_resume():
    return request.data

@app.route("/courses", methods=['POST'])
def courses():
    data = {}
    data['resume'] = request.form['resume']
    data['job_description'] = request.form['job_description']
    return response(data)

@app.route("/homepage")
def hello_from_home():
    return "Hello from the homepage"

@app.route("/stuff", methods=['POST'])
def stuff():
    return 

@app.route("/resumeResults")
def resume():
    #rewriteResume()
    #return highlightDifferences()
    return rewriteResume()

# POSTing data from the front end
@app.route("/results", methods=['POST'])
def postResume():
    data = request.form['resume']

    return rewriteResume(data)
    # return data
    # return request.form['resume']
