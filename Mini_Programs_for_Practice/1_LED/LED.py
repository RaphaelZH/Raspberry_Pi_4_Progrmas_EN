import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
# turn on this LED before making any input
# GPIO.output(LED_PIN, GPIO.HIGH)

# state = int(input(""))
state = int(input("Enter 0 to power off the LED, 1 to power on the LED: "))

# if the state is 0 --> power off the LED
if state == 0:
    GPIO.output(LED_PIN, GPIO.LOW)
# if the state is 1 --> power on the LED
elif state == 1:
    GPIO.output(LED_PIN, GPIO.HIGH)
else:
    print("Wrong state value : " + str(state))
    # otherwise --> cleanup GPIOs and exit
    GPIO.cleanup()
    exit

time.sleep(2)
GPIO.cleanup()
