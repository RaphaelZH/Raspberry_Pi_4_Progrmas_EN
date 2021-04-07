import RPi.GPIO as GPIO
import time

# use a list can replace the following code
# LED_1_PIN = 17
# LED_2_PIN = 27
# LED_3_PIN = 22
LED_PIN_LIST = [17, 27, 22]
# a simple modification here can be instead of a full change of code
# LED_PIN_LIST = [17, 27]

BUTTON_PIN = 26


def power_on_selected_led_only(selected_led_pin):
    # data validation for avoiding the data out of the target list
    if selected_led_pin not in LED_PIN_LIST:
        # return here from the current function
        return
    # use for loop can replace the following code
    # if led_index == 0:
    #     GPIO.output(LED_1_PIN, GPIO.HIGH)
    #     GPIO.output(LED_2_PIN, GPIO.LOW)
    #     GPIO.output(LED_3_PIN, GPIO.LOW)
    #     led_index = 1
    # elif led_index == 1:
    #     GPIO.output(LED_1_PIN, GPIO.LOW)
    #     GPIO.output(LED_2_PIN, GPIO.HIGH)
    #     GPIO.output(LED_3_PIN, GPIO.LOW)
    #     led_index = 2
    # else:
    #     GPIO.output(LED_1_PIN, GPIO.LOW)
    #     GPIO.output(LED_2_PIN, GPIO.LOW)
    #     GPIO.output(LED_3_PIN, GPIO.HIGH)
    #     led_index = 0
    for pin in LED_PIN_LIST:
        if pin == selected_led_pin:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)


GPIO.setmode(GPIO.BCM)
# use for loop can replace the following code
# GPIO.setup(LED_1_PIN, GPIO.OUT)
# GPIO.setup(LED_2_PIN, GPIO.OUT)
# GPIO.setup(LED_3_PIN, GPIO.OUT)
for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

# use for loop can replace the following code
# GPIO.output(LED_1_PIN, GPIO.LOW)
# GPIO.output(LED_2_PIN, GPIO.LOW)
# GPIO.output(LED_3_PIN, GPIO.LOW)
for pin in LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)

previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0

while True:
    time.sleep(0.01)
    button_state = GPIO.input(BUTTON_PIN)
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == GPIO.HIGH:
            power_on_selected_led_only(LED_PIN_LIST[led_index])
            # pass to the next LED index
            led_index += 1
            # add a verification for avoiding the index exceeds the largest index of this list
            # if led_index > len(LED_PIN_LIST) - 1:
            if led_index >= len(LED_PIN_LIST):
                led_index = 0

GPIO.cleanup()
