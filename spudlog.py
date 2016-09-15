# simple file to just email the log home
import spudemail

def main():
    spudemail.sendMail(recipient='aoppenheimer@gmail.com', subject='Log', message='Baboom!', file='/home/pi/spudcam/logs/runnerlog.txt')


if __name__ == "__main__":
    main()