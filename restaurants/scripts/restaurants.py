#!/usr/local/bin/python3

import cgi
import sqlite3

db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT name from restaurants")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()


print("Content-type: text/html")
print()

print("<html><body>")
print("<ul>")
for restaurant in list_restaurants:
	#restaurant_name = restaurant
	print("<li>{}</li>".format(restaurant[0]))
print("</ul>")
print("</body></html>")

