import flask
import psycopg2
from flask import jsonify

app = flask.Flask(__name__)

def get_name_options():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()

    query = "SELECT school FROM schoolstats ORDER BY school ASC"
    cur.execute(query)
    rows = cur.fetchall()

    html = ""
    for row in rows:
        school = row[0]
        html += f'<option value="{school}">{school}</option>\n'
    return html

@app.route('/')
def home():
    return flask.render_template("finalhome.html")

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
    titleOptions = {'acceptrate': 'Acceptance Rate:', 'gradrate': 'Graduation Rate:', 'tuition': 'Average Tuition:'}

    head = ""
    tail = ""
    if rate == 'tuition':
        head += "$"
    else:
        tail += "%"

    stats = get_ranking_stats(rate, lowhigh)
    return flask.render_template("display-rankings.html", stats=stats, rate=rate, title=titleOptions[rate], head=head, tail=tail)

@app.route('/rankings')
def rankings():
    return flask.render_template("finalrankings.html")

def get_college_stats(college1, college2):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
    
    query = "SELECT * FROM schoolstats WHERE school IN (%s, %s)"
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
    
    query = "SELECT * FROM financialaid WHERE school IN (%s, %s)"
    cur.execute(query, (college1, college2))
    results = cur.fetchall()
    conn.close()
    return results

@app.route('/compare/<college1>/<college2>')
def comparing_stats(college1, college2):
    stats = get_college_stats(college1, college2)
    aid = get_college_aid(college1, college2)
    return flask.render_template("display-compare.html", stats=stats, aid=aid)

@app.route('/compare')
def compare():
    dropdownOptions = get_name_options()
    return flask.render_template("finalcompare.html", DropdownOptions=dropdownOptions)

@app.route('/data/<college1>/<college2>')
def get_data(college1, college2):
    stats = get_college_stats(college1, college2)
    return jsonify(stats)

def get_colleges_stats(income, colleges):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()

    query = f"SELECT {income} FROM financialaid WHERE school = %s"
    cur.execute(query, (colleges,))
    results = cur.fetchone()
    aid = results[0]
    conn.close()
    return aid

@app.route('/financialaid/<income>/<colleges>')
def comparing_aidStats(income, colleges):
    aid = get_colleges_stats(income, colleges)
    return flask.render_template("display-aid.html", aid=aid, colleges=colleges)

@app.route('/financialaid')
def financialAid():
    dropdownOptions = get_name_options()
    return flask.render_template("finalfinancial-aid.html", DropdownOptions=dropdownOptions)

def get_major_stats(major):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()

    query = "SELECT school, state FROM schoolstats WHERE popmajor = %s"
    cur.execute(query, (major,))
    results = cur.fetchall()
    conn.close()
    return results

@app.route('/popularmajor/<major>')
def displayMajors(major):
    stats = get_major_stats(major)
    return flask.render_template("display-major.html", stats=stats, major=major)

@app.route('/popularmajor')
def popMajor():
    return flask.render_template("finalpopular-major.html")

@app.route('/map')
def map():
    return flask.render_template("test-map.html")

if __name__ == '__main__':
    my_port = 5123
    app.run(host='0.0.0.0', port=my_port)
