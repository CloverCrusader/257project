import flask
import psycopg2

app = flask.Flask(__name__)

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


# Home functionality

@app.route('/')
def home():

    return flask.render_template("finalhome.html")


# Ranking functionality

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

    titleOptions = {'acceptrate' : 'Acceptance Rate:', 'gradrate' : 'Graduation Rate:', 'tuition' : 'Average Tuition:'}

    head = ""
    tail = ""
    if rate == 'tuition':
      head = head + "$"
    else:
      tail = tail + "%"

    stats = get_ranking_stats(rate, lowhigh)

    return flask.render_template("display-rankings.html", stats=stats, rate=rate, title=titleOptions[rate], head=head, tail=tail)

@app.route('/rankings')
def rankings():

    return flask.render_template("finalrankings.html")


# Compare functionality
    
@app.route('/compare')
def compare():

  return flask.render_template("finalcompare.html")


# Financial Aid functionality

def get_colleges_stats(income, colleges):#colleges
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="rapaczs",
        user="rapaczs",
        password="chip979bond")
    cur = conn.cursor()
    query = f"SELECT {income} FROM financialaid WHERE school = \'{colleges}\'" 
    cur.execute(query)
    results = cur.fetchone()
    aid = results[0]
    conn.close()
    return aid

@app.route('/financialid/<income>/<colleges>')
def comparing_aidStats(income, colleges):
    
    aid = get_colleges_stats(income, colleges) #colleges
    print(aid) # debug
    return flask.render_template("display-aid.html", aid=aid, colleges=colleges)

@app.route('/financialaid')
def financialAid():

    dropdownOptions = get_name_options()

    return flask.render_template("finalfinancial-aid.html",  DropdownOptions = dropdownOptions)


# Popular Major functionality

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

@app.route('/popularmajor/<major>')
def displayMajors(major):
    stats = get_major_stats(major)
    return flask.render_template("display-major.html", stats=stats, major=major) # rename 

@app.route('/popularmajor')
def popMajor():

    return flask.render_template("finalpopular-major.html")

if __name__ == '__main__':
    my_port = 5123
    app.run(host = '0.0.0.0', port = my_port)
