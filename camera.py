from log import logit
from picamera import PiCamera
from time import sleep
from datetime import datetime, timedelta

def takePicture(filename):
	camera = PiCamera()
	try:
		camera.rotation = 180
		sleep(4)
		n=datetime.now() - timedelta(hours=4)
		camera.exif_tags['IFD0.DateTime']=n.strftime("%Y:%m:%d %H:%M:%S")
		camera.exif_tags['DateTimeOriginal']=n.strftime("%Y:%m:%d %H:%M:%S")
		camera.exif_tags['CreateDate']=n.strftime("%Y:%m:%d %H:%M:%S")
		camera.capture(filename)
	except Exception as e:
		logit('camera problem: {0}'.format(str(e)))
	finally:
		camera.close()

if __name__ == "__main__":
    takePicture("/tmp/pic.jpg")