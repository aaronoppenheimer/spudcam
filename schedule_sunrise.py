import subprocess
import time
import requests

def get_data():
    ts = t = w = None
    r=requests.get('http://api.wunderground.com/api/6d94041a38d2a909/astronomy/q/us/04548.json')
    if r.status_code==200:
        w = r.json()
	t = w["sun_phase"]["sunrise"]
        ts = "{0}:{1}am".format(t['hour'],int(t['minute'])+7)
    return ts,r.status_code

def main():
    ts,sc=get_data()
    if ts:
        subprocess.call(["at",ts,"-f","/home/pi/src/spudcam/sunrise.sh"])

if __name__ == "__main__":
    main()
