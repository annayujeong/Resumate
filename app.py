from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/homepage")
def hello_from_home():
    return "Hello from the homepage"