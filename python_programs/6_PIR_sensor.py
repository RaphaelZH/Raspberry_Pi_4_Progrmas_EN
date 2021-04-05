import RPi.GPIO as GPIO
import time

LED_PIN = 17
PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
# using an internal pull-down resistor to set that the default value for the data is zero, which is simply low and close to the ground
# if not, will have a floating value that the result quite not reliable
# pull down here will make sure that the default signal is stable, reliable, and low
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

while True:
    time.sleep(0.01)
    print(GPIO.input(PIR_PIN))

GPIO.cleanup()
