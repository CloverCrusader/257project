from flask import Flask
from flask import render_template
import psycopg2;
import json;

app = Flask(__name__)


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

    html = ""
    for row in rows:
        last = row[0]
        first = row[1]
        
        html = html + f'<option value="{first} {last}">{last}</option>'
        html = html + '\n'
    
    return html



@app.route('/')
def welcome():

    html_string = get_name_options()

    return render_template("homepage.html", DropdownOptions = html_string)


if __name__ == '__main__':
    my_port = 5432
    app.run(host='0.0.0.0', port = my_port) 
