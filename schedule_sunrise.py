import subprocess
import time
import requests
import dateutil.parser

lat = 43.756609
lon = -69.7732962

def get_data():
    ts = t = w = None
#    r=requests.get('http://api.wunderground.com/api/6d94041a38d2a909/astronomy/q/us/04548.json')
    r = requests.get('http://api.sunrise-sunset.org/json?lat='+str(lat)+'&lng='+str(lon)+'&formatted=0')
    print r.json()
    if r.status_code==200:
        w = r.json()
	t = dateutil.parser.parse(w["results"]["sunrise"])

        h1 = t.hour - 4
        m1 = t.minute + 7
        if m1 >= 60:
            m1 = m1 - 60
            h1= h1 + 1

        h2 = t.hour - 4
        m2 = t.minute + 23
        if m2 >= 60:
            m2 = m2 - 60
            h2 = h2 + 1


        ts1 = "{0}:{1:02d}am".format(h1,m1)
        ts2 = "{0}:{1:02d}am".format(h2,m2)
        print("{0} {1}".format(ts1,ts2))
    else:
        print("Error code: ",status_code)
        ts1 = None
        ts2 = None

    return ts1, ts2 ,r.status_code

def main():
    ts1,ts2,sc=get_data()
    if sc == 200:
        if ts1:
            subprocess.call(["at",ts1,"-f","/home/pi/src/spudcam/sunrise.sh"])
            subprocess.call(["at",ts2,"-f","/home/pi/src/spudcam/sunrise.sh"])
        
if __name__ == "__main__":
    main()
