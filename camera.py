from picamera import PiCamera
from time import sleep
from DateTime import DateTime

def takePicture(filename):
    camera = PiCamera()
    try:
	    camera.rotation = 180
	    sleep(4)
	    n=DateTime.now()
	    camera.exif_tags['IFD0.DateTime']=n.strftime("%Y:%m:%d %H:%M:%S")
	    camera.capture(filename)
    finally:
        camera.close()

if __name__ == "__main__":
    takePicture("/tmp/pic.jpg")