import mysql.connector
import json

f = open("local.json")
credentials = json.load(f)["cred"]
local = credentials["localhost"]
user = credentials["username"]
passwd = credentials["password"]
print(user + passwd)
mydb = mysql.connector.connect(
        host=local,
        user=user,
        password=passwd
        )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE localdb")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
