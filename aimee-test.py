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

  query = "SELECT school, state FROM schoolstats ORDER BY school ASC";
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
#------------------------------------------------------------------------
def get_ranking_stats(rate, lowhigh):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
    query = f"SELECT school, state FROM schoolstats ORDER BY {rate} {lowhigh}" 
    cur.execute(query)
    results = cur.fetchall()
    conn.close()
    return results

@app.route('/rankings/<rate>/<lowhigh>')
def displayRanking(rate, lowhigh):
    stats = get_ranking_stats(rate, lowhigh)
    return render_template("rankings2.html", stats=stats)
#------------------------------------------------------------------------


def get_college_stats(income, colleges):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
    query = f"SELECT %s FROM financialaid WHERE school = %s" 
    cur.execute(query, (income, colleges))
    results = cur.fetchall()
    aid = results[0]
    conn.close()
    return aid

@app.route('/financialAid/<income>/<colleges>')
def comparing_stats(income, colleges):
    aid = get_college_stats(income, colleges)
    return render_template("financialAid.html", aid=aid)


def get_major_stats(major):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
    query = f"SELECT school, state FROM schoolstats WHERE popmajor = %s"
    cur.execute(query, (major,))
    results = cur.fetchall()
    conn.close()
    return results

@app.route('/popularMajor/<major>')
def displayMajors(major):
    stats = get_major_stats(major)
    return render_template("popularMajor2.html", stats=stats, major=major)


if __name__ == '__main__':
    my_port = 5223
    app.run(host='0.0.0.0', port = my_port) 
