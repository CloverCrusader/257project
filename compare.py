
from flask import Flask
from flask import render_template
import psycopg2;
import json;

app = Flask(__name__)

@app.route('/')

def get_name_options():

  conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")

  cur = conn.cursor()

  query = "SELECT school FROM schoolstats ORDER BY school ASC";
  cur.execute(query)
    
  rows = cur.fetchall()

  html= ""
  for row in rows:
    school = row[0]

    #html = html = f'<option value="{school}">/option'
    html = html + '\n'
  
  return html

#     html = ""
#     for row in rows:
#         last = row[0]
#         first = row[1]

#         #Here is more info on Python's Formatted Strings
#         #    https://docs.python.org/3/tutorial/inputoutput.html
#         html = html + f'<option value="{first} {last}">{last}</option>'

#         #Backslash n in a string means New Line
#         html = html + '\n'
    
#     return html



# @app.route('/')
# def welcome():

#     html_string = get_name_options()


#     # IMPORTANT: The only reason that this works is because
#     #   In the Template, I marked DropdownOptions as "Safe"
#     #   This tells Flasks that it is safe to insert HTML code into that
#     #   location in the template
#     return render_template("homepage.html", DropdownOptions = html_string)


# @app.route('/insert/<first_name>/<last_name>/')
# def insert_name(first_name,last_name):

#     conn = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="mlepinski",
#         user="mlepinski",
#         password="nunuiscute")
    
#     cur = conn.cursor()


if __name__ == '__main__':
    my_port = 5223
    app.run(host='0.0.0.0', port = my_port) 
