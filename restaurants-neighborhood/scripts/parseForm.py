#!/usr/local/bin/python3

import cgi
import sqlite3

db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT name from neighborhoods")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_neighborhoods = db_cursor.fetchall()


print("Content-type: text/html")
print()

print("<html><body>")
#inform the browser what page (or script) to call once the "submit" button is pressed
print("<form action=\"/scripts/rFinder.py\">")
for neighborhood in list_neighborhoods:
	print("<input type=\"radio\" name=\"name\" value=\"{}\">{}<br>".format(neighborhood[0],neighborhood[0]))
print("<input type=\"submit\" value=\"Submit\">")
print("</form>")
print("</body></html>")
db_connection.close()


