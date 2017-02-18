from log import logit
from picamera import PiCamera
from time import sleep
from datetime import datetime, timedelta
import os
from shutil import copyfile

def takePicture(filename):
    camera = PiCamera()
    try:
        camera.rotation = 180
        sleep(4)
        n=datetime.now() - timedelta(hours=4)
        camera.exif_tags['IFD0.DateTime']=n.strftime("%Y:%m:%d %H:%M:%S")
        camera.capture(filename)
    except Exception as e:
        logit('camera problem: {0}'.format(str(e)))
    finally:
        camera.close()

def rename_pics():
    """ after we take a picture, rename the current one so we can send back a series """
    for i in range(2,16):
        thefile="/tmp/series{0:02}.jpg".format(i)
        if os.path.exists(thefile):
            thenewfile="/tmp/series{0:02}.jpg".format(i-1)
            os.rename(thefile,thenewfile)            

    if os.path.exists("/tmp/pic.jpg"):
        copyfile("/tmp/pic.jpg","/tmp/series15.jpg")


if __name__ == "__main__":
    # takePicture("/tmp/pic.jpg")
    rename_pics()