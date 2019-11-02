import spudemail
import time
import sys
import datetime
from log import logit
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    """ send daily image """
    logit('sending series')
    spudemail.sendMail(recipient='spud@aoppenheimer.com', subject="Sunrise", message='The Pictures!', series=dir_path+'/pix/series{0:02}.jpg', seriesRange=range(1,31))
    
if __name__ == "__main__":
    main()    
