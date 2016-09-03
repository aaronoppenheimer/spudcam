import subprocess

def main():
    while(True):
        subprocess.call(["git","pull"])
        subprocess.call(["python","spud.py"])

if __name__ == "__main__":
    main()