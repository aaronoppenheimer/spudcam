# import camera
import spudemail
import time
import sys
import datetime

VERSION = 4

def main():

    spudemail.sendMail("aoppenheimer@gmail.com","started!","spud is up! Version {0}".format(VERSION))
    print('started at {0}'.format(datetime.datetime.now()))

    def restart(who):
        print('restarting on command')
        return True # quit the program
    
    def heartbeat(who):
        print('heatbeating on command')
        spudemail.sendMail(recipient=r['from'], subject='Heartbeat', message='Baboom!')
        return False

    def picture(who):
        print('sending picture on command')
        spudemail.sendMail(recipient=r['from'], subject='Picture', message='Baboom!', picture='/tmp/pic.jpg')
        return False
        
    def log(who):
        print('sending log on command')
        spudemail.sendMail(recipient=r['from'], subject='Picture', message='Baboom!', file='/home/pi/spudcam/logs/runnerlog.txt')

    while(True):
        try:
            recd = spudemail.getMail()
        except:
            print "Unexpected error:", sys.exc_info()[0]
            recd=[]
    
        quit=False
        
        doit = {'restart': restart,
                'heartbeat': heartbeat,
                'picture': picture,
                'log': log
                }

        for r in recd:
            cmd = r['subj']
            cmd = cmd.strip().lower()
            print('from: {0}   subj: {1}'.format(r['from'], cmd))
            
            if cmd in doit.keys():
                quit = doit[cmd](r['from'])
                
            if quit: # anyone ask us to quit?
                return

        time.sleep(10)


if __name__ == "__main__":
    main()