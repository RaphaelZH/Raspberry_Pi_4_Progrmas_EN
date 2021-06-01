import RPi.GPIO as GPIO
import time
from picamera import PiCamera

FOLDER_NAME = "/home/pi/Camera"


def take_photo(camera):
    # name the photo by using Unix time
    file_name = FOLDER_NAME + "/img_" + str(time.time()) + ".jpg"
    camera.capture(file_name)
    return file_name


PIR_PIN = 4
LED_PIN = 17

# setup camera
camera = PiCamera()
camera.resolution = (720, 480)
camera.rotation = 180
# the camera needs at least 2 seconds to be initialized
print("Waiting 2 seconds to init the camera...")
time.sleep(2)
print("Camera setup OK.")

# setup GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
print("GPIOs setup.")

# set last PIR state
last_pir_state = GPIO.input(PIR_PIN)

# set the default time of each function
movement_timer = time.time()
last_time_photo_taken = 0

# setup some default values
MOV_DETECT_TRESHOLD = 3.0
MIN_DURATION_BETWEEN_2_PHOTOS = 60.0

print("Everything has been setup.")

try:
    while True:
        time.sleep(0.01)
        pir_state = GPIO.input(PIR_PIN)

        # set a rule for the LED
        if pir_state == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        # if GPIO.LOW --> GPIO.HIGH
        # renew the PIR time record
        if last_pir_state == GPIO.LOW and pir_state == GPIO.HIGH:
            movement_timer = time.time()

        # if GPIO.HIGH --> GPIO.HIGH
        # and if the duration of the state exceeds MOV_DETECT_TRESHOLD
        # and if the time between two shots exceeds MIN_DURATION_BETWEEN_2_PHOTOS
        # renew the shooting time record
        if last_pir_state == GPIO.HIGH and pir_state == GPIO.HIGH:
            if time.time() - movement_timer > MOV_DETECT_TRESHOLD:
                if time.time() - last_time_photo_taken > MIN_DURATION_BETWEEN_2_PHOTOS:
                    print("Take photo and send it by email")
                    take_photo(camera)
                    last_time_photo_taken = time.time()

        # renew the PIR state
        last_pir_state = pir_state
except KeyboardInterrupt:
    GPIO.cleanup()
