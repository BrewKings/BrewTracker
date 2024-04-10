import firebase_admin as fb

def setup():
    bj = fb.credentials.Certificate('google-services.json')
    default_app = fb.initialize_app(cred_object, {
            'https://console.firebase.google.com/project/brewtracker-278df/firestore/databases/-default-/data/~2F':databaseURL
                })

def main():
    setup()

if __name__ == "__main__":
    main()
