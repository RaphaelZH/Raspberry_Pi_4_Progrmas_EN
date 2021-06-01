import RPi.GPIO as GPIO
import time

LED_1_PIN = 17
LED_2_PIN = 27
LED_3_PIN = 22
BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_1_PIN, GPIO.OUT)
GPIO.setup(LED_2_PIN, GPIO.OUT)
GPIO.setup(LED_3_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

# initialize the state of all three LEDs
GPIO.output(LED_1_PIN, GPIO.LOW)
GPIO.output(LED_2_PIN, GPIO.LOW)
GPIO.output(LED_3_PIN, GPIO.LOW)

# check current button state
previous_button_state = GPIO.input(BUTTON_PIN)
# add the index of one LED
led_index = 0

while True:
    # make this while loop run at 100 Hertz
    # it does not matter that this command to be the beginning of or the end of this loop
    time.sleep(0.01)
    # read the current button state
    button_state = GPIO.input(BUTTON_PIN)
    # compare the new button state with the previous button state
    if button_state != previous_button_state:
        # either this button going from low to high or high to low
        # in other words, either this button be pressed or be released
        # set the previous button state to the current button state
        previous_button_state = button_state
        # each time when this button is pressed, the program executes the inside condition block
        if button_state == GPIO.HIGH:
            if led_index == 0:
                # power on LED 1
                GPIO.output(LED_1_PIN, GPIO.HIGH)
                GPIO.output(LED_2_PIN, GPIO.LOW)
                GPIO.output(LED_3_PIN, GPIO.LOW)
                # set the LED index to the next LED index
                led_index = 1
            elif led_index == 1:
                # power on LED 2
                GPIO.output(LED_1_PIN, GPIO.LOW)
                GPIO.output(LED_2_PIN, GPIO.HIGH)
                GPIO.output(LED_3_PIN, GPIO.LOW)
                # set the LED index to the next LED index
                led_index = 2
            else:
                # power on LED 3
                GPIO.output(LED_1_PIN, GPIO.LOW)
                GPIO.output(LED_2_PIN, GPIO.LOW)
                GPIO.output(LED_3_PIN, GPIO.HIGH)
                # set the LED index to the next LED index
                led_index = 0

GPIO.cleanup()
