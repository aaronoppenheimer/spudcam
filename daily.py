import spudemail
import time
import sys
import datetime
from log import logit

def main():
    """ send daily image """
    logit('sending daily picture')
    spudemail.sendMail(recipient='aoppenheimer@gmail.com', subject="Today's Picture", message='Baboom!', picture='/tmp/pic.jpg')
    
if __name__ == "__main__":
    main()    