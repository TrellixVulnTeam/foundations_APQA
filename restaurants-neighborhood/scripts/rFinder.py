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

# select ID column from neighborhoods table where the name has the value 
#from the radio button
db_cursor.execute("SELECT ID FROM neighborhoods WHERE name = \"{}\"".format(n_name))

#saves the id in a variable
#fetch one, instead of all because I expect only one value since the id's are unique
neighborhood_id = db_cursor.fetchone()

#select name colmn from restaurats table where the neigborhood id is 
#same as the id of the user input 
#or in other words neighborgood_id
db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = {}".format(neighborhood_id[0]))

#fetch all because I expect multiple values to appear 
#(multiple restaurants in the same neighborhood)
restaurant_names = db_cursor.fetchall()
# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table

print("Content-type: text/html")
print()
# () shows that the header is over
print("<html>")
print("<body")
print("<ul>")
for name in restaurant_names:
	print("<li>{}</li>".format(name[0]))
print("</ul>")
print("</body>")
print("</html>")