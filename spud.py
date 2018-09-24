# import camera
import spudemail
import time
import sys
import datetime
from log import logit
import Adafruit_DHT
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

VERSION = 15

sensor = Adafruit_DHT.DHT22
pin = 23

def main():

    spudemail.sendMail("spud@aoppenheimer.com","started!","spud is up! Version {0}".format(VERSION))
    logit('started at {0}'.format(datetime.datetime.now() - datetime.timedelta(hours=4)))

    def restart(who,subj=''):
        logit('restarting on command from {0}'.format(who))
        return True # quit the program
    
    def heartbeat(who,subj=''):
        logit('heatbeating on command from {0}'.format(who))
        if subj=='':
            subj='Heartbeat'

        spudemail.sendMail(recipient=who, subject=subj, message='Heatbeat!')
        return False

    def picture(who,subj=''):
        logit('sending picture on command from {0}'.format(who))
        if subj=='':
            subj='Picture'

        spudemail.sendMail(recipient=who, subject=subj, message='The Picture!', picture=dir_path+'/pix/pic.jpg')
        return False

    def series(who,subj=''):
        logit('sending series on command from {0}'.format(who))
        if subj=='':
            subj='Series'

        spudemail.sendMail(recipient=who, subject=subj, message='The Picture!', series=dir_path+'/pix/series{0:02}.jpg', seriesRange=range(1,16))
        return False
        
    def log(who,subj=''):
        logit('sending log on command from {0}'.format(who))
        spudemail.sendMail(recipient=who, subject='Log File', file='/home/pi/spudcam/logs/runnerlog.txt')
        spudemail.sendMail(recipient=who, subject='Other Log File', file='/home/pi/spudcam/logs/cronlog')


    def temp(who,subj=''):
        logit('sending temperature on command from {0}'.format(who))
#        f=open('/sys/class/thermal/thermal_zone0/temp')
#        line=f.readline()
#        f.close()
#        temperature=int(line)/1000
#        spudemail.sendMail(recipient=who, subject='Spud Temp', message='Temperature:{0}'.format(temperature))
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        spudemail.sendMail(recipient=who, subject='Spud Temp', message='Temperature:{0}, Humidity:{1}'.format(temperature, humidity))


    accession = 0
    while(True):

        try:
            recd = spudemail.getMail()
        except:
            logit("Unexpected error fetching email: {0}".format(sys.exc_info()[0]))
            recd=[]
    
        quit=False
        
        doit = {'restart': restart,
                'heartbeat': heartbeat,
                'picture': picture,
                'series': series,
                'log': log,
                'temp': temp
                }

        for r in recd:
            cmd = r['subj']
            cmd = cmd.strip().lower()
            accession = accession + 1
            logit('{0} from: {1}   subj: {2}   body: >{3}<'.format(accession, r['from'], cmd, r['body']))
            
            if cmd in doit.keys():
                quit = doit[cmd](r['from'],r['body'])
                
            if quit: # anyone ask us to quit?
                return

        time.sleep(10)


if __name__ == "__main__":
    main()
