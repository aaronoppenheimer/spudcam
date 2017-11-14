import spudemail
import time
import sys
import datetime
from log import logit
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    """ send daily image """
    logit('sending daily picture')
    spudemail.sendMail(recipient='aoppenheimer@gmail.com', subject="Today's Picture", message='Baboom!', picture=dir_path+'/pix/pic.jpg')
    
if __name__ == "__main__":
    main()    
