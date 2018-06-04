from log import logit
from picamera import PiCamera
from PIL import Image, ImageDraw, ImageFont
from time import sleep
from datetime import datetime, timedelta
import os
from shutil import copyfile
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def takePicture(filename):
    camera = PiCamera()
    try:
#        camera.rotation = 180
        camera.rotation = 0
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
        thefile=dir_path+"/pix/series{0:02}.jpg".format(i)
        if os.path.exists(thefile):
            thenewfile=dir_path+"/pix/series{0:02}.jpg".format(i-1)
            os.rename(thefile,thenewfile)            

    if os.path.exists(dir_path+"/pix/pic.jpg"):
        copyfile(dir_path+"/pix/pic.jpg",dir_path+"/pix/series15.jpg")

def annotate_pix():
    # get an image
    base = Image.open(dir_path+'/pix/pic.jpg').convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype('Pillow/Tests/fonts/DejaVuSans.ttf', 28)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, full opacity
    dt = str(datetime.now())
    d.text((10,60), dt, font=fnt, fill=(255,0,0,255))

    out = Image.alpha_composite(base, txt)
    out.convert('RGB').save(dir_path+"/pix/pic_date.jpg")

def doPicture():
    takePicture(dir_path+"/pix/pic.jpg")
    rename_pics()
#    annotate_pix()
    

if __name__ == "__main__":
    doPicture()
