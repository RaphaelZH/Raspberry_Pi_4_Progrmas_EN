# import picamera
from picamera import PiCamera
import time

# camera = picamera.PiCamera()
camera = PiCamera()
# setting resolution for the camera
# this setting is requiring a tuple
camera.resolution = (1280, 720)
# setting rotation for the camera
camera.rotation = 180
time.sleep(2)

# setting the directory to stock the photo taken by the camera
file_name = "/home/pi/Camera/image.jpg"
camera.capture(file_name)
print("Done.")
