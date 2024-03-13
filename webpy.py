#!
print("Content-Type:text/html")
print()
import cgi
print("<hr/>")
print("<h1>it's working dude</h1>")

form = cgi.FieldStorage()

pid = form.getValue("id")
no = form.getValue("no")
add = form.getValue("add")

import mysql.connector

con = mysql.connector.connect(user="root",password = "",host="localhost",database="webdb")
cursor= con.cursor()

cursor.execute("insert into webt values(%s,%s,%s)",(pid,no,add))

cursor.close()
con.close()

print("<h1>it's working dude.....</h1>")