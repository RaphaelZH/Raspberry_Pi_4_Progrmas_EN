from flask import Flask
import os

LOG_FILE_NAME = "/home/pi/camera/photo_logs.txt"
photo_counter = 0

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/check-movement")
def check_movement():
    message = ""
    line_counter = 0
    if os.path.exists(LOG_FILE_NAME):
        with open(LOG_FILE_NAME, "r") as f:
            for line in f:
                line_counter += 1
        global photo_counter
        difference = line_counter - photo_counter
        message = str(difference) + " photos were taken since you last checked."
        photo_counter = line_counter
    else:
        message = "Nothing new"
    return message
        
app.run(host="0.0.0.0")