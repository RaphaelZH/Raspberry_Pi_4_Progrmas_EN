import RPi.GPIO as GPIO
import time

PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
# using an internal pull-down resistor to set that the default value for the data is zero, which is simply low and close to the ground
# if not, will have a floating value that the result quite not reliable
# pull down here will make sure that the default signal is stable, reliable, and low
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    # be able to read 10 times each second
    time.sleep(0.1)
    print(GPIO.input(PIR_PIN))

GPIO.cleanup()
