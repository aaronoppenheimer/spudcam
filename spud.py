# import camera
import spudemail

def main():

#     spudemail.sendMail(
#         "aoppenheimer@gmail.com",
#         "test",
#         "this is a test email!")
    recd = spudemail.getMail()
    
    for r in recd:
        print('from: {0}   subj: {1}'.format(r['from'], r['subj']))
        spudemail.sendMail(r['from'], 'regarding {0}'.format(r['subj']), 'thanks!')

if __name__ == "__main__":
    main()