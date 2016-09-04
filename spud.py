# import camera
import spudemail
import time


def main():

    spudemail.sendMail("aoppenheimer@gmail.com","started!","spud is up!")


    def restart(who):
        return True # quit the program
    
    def heartbeat(who):
        spudemail.sendMail(r['from'], 'Heartbeat', 'Baboom!')
        return False

    def picture(who):
        spudemail.sendMail(r['from'], 'Picture', 'Baboom!', 'pic.jpg')
        return False

    while(True):
        print('checking...')
        recd = spudemail.getMail()
    
        quit=False
        
        doit = {'restart': restart,
                'heartbeat': heartbeat,
                'picture': picture
                }

        for r in recd:
            print('from: {0}   subj: {1}'.format(r['from'], r['subj']))
            
            if r['subj'] in doit.keys():
                quit = doit[r['subj']](r['from'])
                
            if quit: # anyone ask us to quit?
                return

        time.sleep(10)


if __name__ == "__main__":
    main()