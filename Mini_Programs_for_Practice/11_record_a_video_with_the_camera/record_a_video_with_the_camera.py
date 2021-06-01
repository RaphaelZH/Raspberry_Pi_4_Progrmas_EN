from picamera import PiCamera
import time

camera = PiCamera()
# set resolution for the camera
# this setting is requiring a tuple
camera.resolution = (1280, 720)
# set rotation for the camera
camera.rotation = 180
time.sleep(2)

# set the directory to stock the videos recorded by the camera
file_name = "/home/pi/Camera/video.h264"
camera.start_recording(file_name)
# different from the command in the Terminal,
# the unit in here is not millisecond but second
camera.wait_recording(10)
camera.stop_recording()
print("Done.")
