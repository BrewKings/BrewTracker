from firebase import firebase
import serial as s
import sys
import json
import queue
import time
from data import Data

TIME_HOUR = 3
TIME_MINUTE = 4 
TIME_SEC = 5
TIME_YDAY = 7

th_data = list()

try:
    URL = sys.argv[1]
except IndexError as e:
    f = open("default.json", "r")
    URL = json.load(f)["url"]["default"]

def db_setup():
    fb = firebase.FirebaseApplication("https://console.firebase.google.com/project/brewtracker-1fd25/firestore/databases/-default-", None)
    result = fb.get("/data", None)
    print(result)
    return fb
    
def port_setup():
    port = s.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
    return port 

def read_port(port):
    if port.in_waiting > 0:
        ln = port.readline().decode('utf-8').rstrip()
        bundle = ln.split("-")
        temp = float(a[0])
        humid = float(a[1])
        return (temp, humid)
    return None

def ave(l):
    t_ave = 0
    h_ave = 0
    for i in range(len(l)):
        t_ave += l[0]
        h_ave += l[1]
    t_ave /= len(l)
    h_ave /= len(l)
    return {"temperature":t_ave,"humidity":h_ave}

def loop(q, port):
    while(1):
        lt = time.localtime()
        d_in = read_port(port)
        if d_in != None:
            th_data.append(d_in)
        if lt[TIME_MINUTE] == 0 and lt[TIME_SEC]: 
            ave_temp_humid = ave(th_data)
            d_out = Data(ave_temp_humid)
            q.put(d_out)
            try:
                q.dequeue().logData(URL)
            except Exception as e:
                q.put(d_out)
                print("log failed")
            else:
                q.dequeue()
                time.sleep(2)

def main():
    q = queue.Queue()
    #fb = db_setup()
    port = port_setup()
    #loop(q)
    d = Data({"temp":12,"hum":44})
    q.put(d)
    print(str(q))
    #setup()
    print(URL)

if __name__ == "__main__":
    main()
