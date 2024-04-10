import firebase_admin as fb
# import serial as s
import sys
import json
try:
    URL = sys.argv[1]
except IndexError as e:
    f = open("default.json", "r")
    URL = json.load(f)["url"]["default"]


def setup():
    bj = fb.credentials.Certificate('google-services.json')
    default_app = fb.initialize_app(cred_object, {
            'https://console.firebase.google.com/project/brewtracker-278df/firestore/databases/-default-/data/~2F':databaseURL
                })
    port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

def loop():
    while(1):
        d_in = port.read()
        d_out = Data(d_in)
        d_out.logData(URL)


def main():
    # setup()
    print(URL)

if __name__ == "__main__":
    main()
