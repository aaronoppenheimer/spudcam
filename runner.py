import subprocess

def main():
    while(True):
        subprocess.call(["git","pull"])
        subprocess.call(["crontab","-u","pi","/home/pi/spudcam/crontab.txt"])
        subprocess.call(["python","/home/pi/spud.py"])

if __name__ == "__main__":
    main()