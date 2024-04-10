from firebase import firebase as fb
import time as t
import urllib.request
import urllib.error
import json

class Data:
    def __init__(self, data):
        '''
        Instantiates a new Data object
        '''
        self.data = data 
        self.my_data = dict()
        self.my_data["timestamp"] = {".sv" : "timestamp"}
        
        self.json_data = json.dump(self.data).encode()

    def logData(self,url):
        try:
            loader = urllib.request.urlopen(url, data=self.json_data)
        except urllib.error.URLError as e:
            message = json.load(e.read())
            print(message["error"])
        else:
            print(loader.read())


if __name__ == '__main__':
    d = Data({"temp": 12, "hum": 69})
    d.logData('https://console.firebase.google.com/u/0/project/brewtracker-1fd25/messaging/onboarding')
