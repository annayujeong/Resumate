import ast
from flask import Flask, request
from course import response
from flask_cors import CORS
from resumeRewriter import rewriteResume

app = Flask(__name__)
CORS(app)

@app.route("/courses", methods=['POST'])
def courses():
    data = {}
    data['resume'] = request.form['resume']
    data['job_description'] = request.form['job_description']
    return response(data)

@app.route("/resumeResults")
def resume():
    return rewriteResume()

@app.route("/results", methods=['POST'])
def postResume():
    data = request.form['resume']

    return rewriteResume(data)
