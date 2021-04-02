import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
# LED default setting
# GPIO.output(LED_PIN, GPIO.HIGH)

# state = int(input(""))
state = int(input("Enter 0 to power off the LED, 1 to power on the LED: "))

# 0 --> power off
if state == 0:
    GPIO.output(LED_PIN, GPIO.LOW)
# 1 --> power on
elif state == 1:
    GPIO.output(LED_PIN, GPIO.HIGH)
else:
    print("Wrong state value : " + str(state))
    GPIO.cleanup()
    # exit
    exit

time.sleep(2)
GPIO.cleanup()
