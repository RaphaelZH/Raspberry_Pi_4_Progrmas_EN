from flask import Flask

app = Flask(__name__)

# create some routes
@app.route("/")
def index():
    return "Hello from Flask"

# 500
app.run(host="0.0.0.0")
