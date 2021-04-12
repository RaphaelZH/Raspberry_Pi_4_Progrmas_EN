from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26
LED_PIN_LIST = [17, 27, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
app = Flask(__name__)

for pin in LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)


# create some routes
# create the route of the home page
@app.route("/")
def index():
    return "Hello from Flask"


# create a new route to check the state of the push button
@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Button is pressed"
    return "Button is not pressed"


# create some new routes to trigger LED
# here, <int:led_pin> will give the pin number of LED, such as 17, 27 or 22
# here, <int:led_state> will give the states of LED by number, basically, 0 for GPIO low, 1 for GPIO high
@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    # check if the input LED pin is inside of the LED pins list given
    if not led_pin in LED_PIN_LIST:
        return "Wrong GPIO number: " + str(led_pin)
    # now, check what the input LED state is, and if it is correct
    if led_state == 0:
        GPIO.output(led_pin, GPIO.LOW)
    elif led_state == 1:
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        return "State must be 0 or 1"
    # if the LED pin and the LED state is correctly set, this application will return OK
    return "OK"


app.run(host="0.0.0.0")
