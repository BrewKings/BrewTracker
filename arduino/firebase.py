import firebase_admin as fb
import serial
def setup():
    bj = fb.credentials.Certificate('google-services.json')
    default_app = fb.initialize_app(cred_object, {
            'https://console.firebase.google.com/project/brewtracker-278df/firestore/databases/-default-/data/~2F':databaseURL
                })
    port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

def main():
    setup()


if __name__ == "__main__":
    main()
