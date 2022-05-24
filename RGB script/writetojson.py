#import pip

#pip.main(['install', package])
import config
import json
import mysql.connector


while True:
    mydb = mysql.connector.connect(
    host= config.host,
    user= config.user,
    password= config.password,
    database= config.database,
    auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM currentprofile")
    myresult = mycursor.fetchone()
    json_string = {
        "profile":myresult[0],
        "red": myresult[1],
        "green": myresult[2],
        "blue": myresult[3],
        "scale":myresult[4]
        }

    with open('curprof.json', 'w') as outfile:
        json.dump(json_string, outfile)