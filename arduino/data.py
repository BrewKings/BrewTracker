from firebase import firebase as fb
import time as t
import urllib.request
import urllib.error
import json

TIME_YEAR = 0
TIME_HOUR = 3
TIME_MINUTE = 4 
TIME_SEC = 5
TIME_YDAY = 7

class Data:
    def __init__(self, data):
        '''
        Instantiates a new Data object
        '''
        self.data = data 
        self.my_data = dict()
        # self.my_data["timestamp"] = {".sv" : "timestamp"}
        lt = t.localtime()
        self.my_data["timestamp"] = {"year": lt[TIME_YEAR], 
                                     "day": lt[TIME_YDAY],
                                     "hour":lt[TIME_HOUR],
                                     "minute":lt[TIME_MINUTE],
                                     "second":lt[TIME_SEC]}
        
        self.json_data = json.dumps(self.data).encode()

    def logData(self,url):
        try:
            loader = urllib.request.urlopen(url, data=self.json_data)
        except urllib.error.URLError as e:
            message = json.load(e.read())
            print(message["error"])
        else:
            print(loader.read())

    def __repr__(self):
        s = str()
        s += "Data:\n"
        s += f"\ttemperature: {self.data['temp']:.2f}"
        return s


if __name__ == '__main__':
    d = Data({"temp": 12.0,"hum": 69})
    # d.logData('https://console.firebase.google.com/u/0/project/brewtracker-1fd25/messaging/onboarding')
    lt = t.localtime()
    print(lt)
    print(lt[0])
    print(lt[1])
    print(lt[7])
    print(d)
