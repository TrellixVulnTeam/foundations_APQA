import cgi
import sqlite3

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
n_name = form.getvalue('name')


db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT ID FROM neighborhoods WHERE name = \"{}\"".format(n_name))
neighborhood_id = db_cursor.fetchone()


db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = {}".format(neighborhood_id[0]))
restaurant_names = db_cursor.fetchall()
# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table


print("Content-type: text/html")
print()
print("<html>")
print("<body")
print("<ul>")
for name in restaurant_names:
	print("<li>{}</li>".format(name[0]))
print("</ul>")
print("</body>")
print("</html>")