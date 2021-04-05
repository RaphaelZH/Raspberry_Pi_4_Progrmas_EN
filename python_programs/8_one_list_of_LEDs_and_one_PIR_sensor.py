import RPi.GPIO as GPIO
import time

LED_PIN_LIST = [17, 27, 22]
PIR_PIN = 4


def power_on_selected_led_only(selected_led_pin):
    if selected_led_pin not in LED_PIN_LIST:
        return
    for pin in LED_PIN_LIST:
        if pin == selected_led_pin:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)


GPIO.setmode(GPIO.BCM)
for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for pin in LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)

# here, this PIR sensor has replaced the button as control this LED
previous_pir_state = GPIO.input(PIR_PIN)
led_index = 0

while True:
    time.sleep(0.01)
    # here, this PIR sensor has replaced the button as control this LED
    pir_state = GPIO.input(PIR_PIN)
    if pir_state != previous_pir_state:
        previous_pir_state = pir_state
        if pir_state == GPIO.HIGH:
            power_on_selected_led_only(LED_PIN_LIST[led_index])
            led_index += 1
            if led_index >= len(LED_PIN_LIST):
                led_index = 0

GPIO.cleanup()
