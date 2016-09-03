# import camera
import spudemail
import time


def main():

#     spudemail.sendMail(
#         "aoppenheimer@gmail.com",
#         "test",
#         "this is a test email!")


    def restart(who):
        return True # quit the program
    
    def picture(who):
        spudemail.sendMail(r['from'], 'your picture', 'thanks!')
        return False



    while(True):
        print('fetching...')
        recd = spudemail.getMail()
    
        quit=False
        
        doit = {'restart': restart,
                'picture': picture
                }

        for r in recd:
            print('from: {0}   subj: {1}'.format(r['from'], r['subj']))
            
            if r['subj'] in doit.keys():
                quit = doit[r['subj']](r['from'])
                
            if quit:
                return

        print('sleeping...')
        time.sleep(5)


if __name__ == "__main__":
    main()