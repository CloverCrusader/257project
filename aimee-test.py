from flask import Flask, session
from flask import render_template, request
import psycopg2;
import json;
app = Flask(__name__)

@app.route('/aimee')
def aimee_test_pg():
  html_string = get_name_options()
  return render_template("aimee-test.html", DropdownOptions = html_string)

@app.route('/aimeeStats')
def aimee_stats():
    income = request.args.get('income')
    colleges = request.args.get('colleges')
  
    stats = get_college_stats(income, colleges)
    return render_template("aimee-test.html", stats=stats)
    
def get_name_options():

  conn = psycopg2.connect(
        host="localhost",
        port=5232,
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
  return render_template("compare.html", DropdownOptions = html_string)

def get_college_stats(college1, college2):
    conn = psycopg2.connect(
        host="localhost",
        port=5232,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
    
    query = """
        SELECT * FROM schoolstats WHERE school IN (%s, %s)
    """
    cur.execute(query, (college1, college2))
    results = cur.fetchall()
    conn.close()
    return results

@app.route('/comparingStats')
def comparing_stats():
    college1 = request.args.get('college1')
    college2 = request.args.get('college2')
  
    stats = get_college_stats(college1, college2)
    return render_template("comparingStats.html", stats=stats)

if __name__ == '__main__':
    my_port = 5232
    app.run(host='0.0.0.0', port = my_port)
