import subprocess
import time

def main():
    while(True):
        subprocess.call(["git","pull"])
        subprocess.call(["crontab","-u","pi","/home/pi/src/spudcam/crontab.txt"])
        subprocess.call(["python","/home/pi/src/spudcam/spudlog.py"])
        subprocess.call(["rm","/home/pi/src/spudcam/logs/runnerlog.txt"])
        time.sleep(15)
        with open('/home/pi/src/spudcam/logs/weblog.txt', 'a') as f:
            subprocess.Popen(["python","-u","/home/pi/src/spudcam/app.py"], stdout=f, stderr=f)
        with open('/home/pi/src/spudcam/logs/runnerlog.txt', 'a') as f:
            subprocess.call(["python","-u","/home/pi/src/spudcam/spud.py"], stdout=f, stderr=f)

if __name__ == "__main__":
    main()


