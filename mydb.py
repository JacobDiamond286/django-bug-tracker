import mysql.connector

# Data Base

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Deeznuts1!'

    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE bugtracker")

print("All Done")