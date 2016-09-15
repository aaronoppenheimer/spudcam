import subprocess

def main():
    while(True):
        subprocess.call(["git","pull"])
        subprocess.call(["crontab","-u","pi","/home/pi/spudcam/crontab.txt"])
        subprocess.call(["python","/home/pi/spudcam/spudlog.py"])
        subprocess.call(["rm","/home/pi/spudcam/logs/runnerlog.txt"])
        with open('/home/pi/spudcam/logs/runnerlog.txt', 'a') as f:
            subprocess.call(["python","-u","/home/pi/spudcam/spud.py"], stdout=f, stderr=f)

if __name__ == "__main__":
    main()