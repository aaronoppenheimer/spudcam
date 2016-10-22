# import camera
import spudemail
import time
import sys
import datetime
from log import logit

VERSION = 8

def main():

    spudemail.sendMail("aoppenheimer@gmail.com","started!","spud is up! Version {0}".format(VERSION))
    logit('started at {0}'.format(datetime.datetime.now()))

    def restart(who):
        logit('restarting on command from {0}'.format(who))
        return True # quit the program
    
    def heartbeat(who):
        logit('heatbeating on command from {0}'.format(who))
        spudemail.sendMail(recipient=r['from'], subject='Heartbeat', message='Baboom!')
        return False

    def picture(who):
        logit('sending picture on command from {0}'.format(who))
        spudemail.sendMail(recipient=r['from'], subject='Picture', message='Baboom!', picture='/tmp/pic.jpg')
        return False
        
    def log(who):
        logit('sending log on command from {0}'.format(who))
        spudemail.sendMail(recipient=r['from'], subject='Log File', file='/home/pi/spudcam/logs/runnerlog.txt')

    def temp(who):
        logit('sending temperature on command from {0}'.format(who))
        f=open('/sys/class/thermal/thermal_zone0/temp')
        line=f.readline()
        f.close()
        temperature=int(line)/1000
        spudemail.sendMail(recipient=r['from'], subject='Spud Temp', message='Temperature:{0}'.format(temperature))

    accession = 0
    while(True):

        try:
            recd = spudemail.getMail()
        except:
            logit("Unexpected error: {0}".format(sys.exc_info()[0]))
            recd=[]
    
        quit=False
        
        doit = {'restart': restart,
                'heartbeat': heartbeat,
                'picture': picture,
                'log': log,
                'temp': temp
                }

        for r in recd:
            cmd = r['subj']
            cmd = cmd.strip().lower()
            accession = accession + 1
            logit('{0} from: {1}   subj: {2}'.format(accession, r['from'], cmd))
            
            if cmd in doit.keys():
                quit = doit[cmd](r['from'])
                
            if quit: # anyone ask us to quit?
                return

        time.sleep(10)


if __name__ == "__main__":
    main()