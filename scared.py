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
  return render_template("scared.html", DropdownOptions = html_string)

def get_college_stats(college1, college2):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
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

def get_college_aid(college1, college2):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
    
    query = """
        SELECT * FROM financialaid WHERE school IN (%s, %s)
    """
    cur.execute(query, (college1, college2))
    results = cur.fetchall()
    conn.close()
    return results


@app.route('/comparingStats/<college1>/<college2>')
def comparing_stats(college1, college2):
    stats = get_college_stats(college1, college2)
    aid = get_college_aid(college1, college2)
    return render_template("comparingStats.html", stats=stats, aid=aid)
    

#------------------------------------------------------------------------
def get_ranking_stats(rate, lowhigh):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
    query = f"SELECT school, state, {rate} FROM schoolstats ORDER BY {rate} {lowhigh}" 
    cur.execute(query)
    results = cur.fetchall()
    conn.close()
    return results

@app.route('/rankings/<rate>/<lowhigh>')
def displayRanking(rate, lowhigh):
    stats = get_ranking_stats(rate, lowhigh)
    return render_template("rankings2.html", stats=stats, rate=rate)
#------------------------------------------------------------------------


def get_colleges_stats(income):#colleges
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
def comparing_aidStats(income, colleges): #colleges
    aid = get_colleges_stats(income, colleges) #colleges
    return render_template("financialAid.html", aid=aid, income=income, colleges=colleges)


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