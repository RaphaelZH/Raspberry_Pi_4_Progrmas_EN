import os
import time
from picamera import PiCamera

FOLDER_NAME = "/home/pi/Camera"

# check if the target directory exists; if not, create it
if not os.path.exists(FOLDER_NAME):
    os.mkdir(FOLDER_NAME)

camera = PiCamera()
camera.resolution = (1280, 720)
camera.rotation = 180
time.sleep(2)

counter = 1

while True:
    # command Raspberry Pi to take pictures every 5 seconds
    file_name = FOLDER_NAME + "/img" + str(counter) + ".jpg"
    counter += 1
    camera.capture(file_name)
    print("New photo has been taken")
    time.sleep(5)
