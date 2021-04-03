import RPi.GPIO as GPIO
import time

BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
# set this button as an input
GPIO.setup(BUTTON_PIN, GPIO.IN)

while True:
    # read from this button and see the result
    print(GPIO.input(BUTTON_PIN))
    time.sleep(1)


GPIO.cleanup()
