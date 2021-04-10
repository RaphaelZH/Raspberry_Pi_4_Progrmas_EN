from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
app = Flask(__name__)


# create some routes
# create the route of the home page
@app.route("/")
def index():
    return "Hello from Flask"


# create a new route for push button
@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Button is pressed"
    # here, the condition of else could be omitted because it is kind of implied
    # else:
    #     return "Button is not pressed"
    return "Button is not pressed"


# the port default is 5000
# this application is running on 0.0.0.0:5000, 127.0.0.1:5000, localhost:5000, and (the IP address of the Raspberry Pi):5000
app.run(host="0.0.0.0")
