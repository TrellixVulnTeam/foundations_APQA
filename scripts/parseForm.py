#!/usr/local/bin/python3

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi
import csv

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
csv_list = []
v_name = form.getvalue('color').lower()

with open('scripts/colors.csv', 'r') as csv_file:
 csv_reader = csv.reader(csv_file, delimiter=',')

 for row in csv_reader:
   csv_list.append(row)


for row in csv_list:

 rgb = '_'.join(row[-3:])
 del row[-3:]
 row.append(rgb)


if ' ' in v_name:
 v_name = v_name.replace(' ', '_')

for list in csv_list:
  if v_name in list:
      print("""
          <html>
          <body>
          <p>
          {} is a color
          </p>
          </body>
     <div style='background-color:{}; width:50px; height:50px'>
     </div></html>""".format(v_name, list[2]))
