
import mysql.connector
con = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'challange1',
    password = 'root'
)
print(con)