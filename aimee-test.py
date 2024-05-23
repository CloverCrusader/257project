from flask import Flask, session
from flask import render_template, request
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

  html= ""
  for row in rows:
    school = row[0]

    html = html + f'<option value="{school}">{school}</option>'
    html = html + '\n'
  return html

@app.route('/')
def compare_pg():
  html_string = get_name_options()
  return render_template("aimee-test.html", DropdownOptions = html_string)


def get_college_stats(income, colleges):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
  
query = f"SELECT {income} FROM financialaid WHERE school = %s" 
    cur.execute(query, (colleges,))

    results = cur.fetchall()
    aid = results[1]
    conn.close()
    return aid

@app.route('/financialAid/<income>/<colleges>')
def comparing_stats(income, colleges):
    stats = get_college_stats(income, colleges)
    return render_template("aimee-display-test.html", stats=stats)

if __name__ == '__main__':
    my_port = 5223
    app.run(host='0.0.0.0', port = my_port) 