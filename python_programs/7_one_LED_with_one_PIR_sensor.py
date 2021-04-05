import RPi.GPIO as GPIO
import time

LED_PIN = 17
PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

while True:
    # be able to read 100 times each second
    time.sleep(0.01)
    # here, this PIR sensor has replaced the button as control this LED
    if GPIO.input(PIR_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
