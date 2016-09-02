from picamera import PiCamera
from time import sleep

def takePicture(filename):
    camera = PiCamera()
    camera.rotation = 180
    sleep(4)
    camera.capture(filename)
