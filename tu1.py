from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"\

@app.route("/sahil")
def sah():
    return "Hello sahil bro 2"

app.run(debug=True)