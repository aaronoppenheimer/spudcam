import subprocess
import time

def main():
    while(True):
        subprocess.call(["git","pull"])
        subprocess.call(["crontab","-u","pi","/home/pi/spudcam/crontab.txt"])
        subprocess.call(["python","/home/pi/spudcam/spudlog.py"])
        subprocess.call(["rm","/home/pi/spudcam/logs/runnerlog.txt"])
        time.sleep(15)
        with open('/home/pi/spudcam/logs/weblog.txt', 'a') as f:
            subprocess.Popen(["python","-u","/home/pi/spudcam/web/app.py"], stdout=f, stderr=f)
        with open('/home/pi/spudcam/logs/runnerlog.txt', 'a') as f:
            subprocess.call(["python","-u","/home/pi/spudcam/spud.py"], stdout=f, stderr=f)

if __name__ == "__main__":
    main()


