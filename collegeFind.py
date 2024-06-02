import flask
import psycopg2

app = flask.Flask(__name__)


'''
Executes a pqsl query to a database.
Returns an array of school names.
'''
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


'''
Runs homepage.
'''
@app.route('/')
def home():
    return flask.render_template("finalhome.html")


'''
Executes a pqsl query to a database.
'rate' - specifies statistic of interest
'lowhigh' - designates ascending of descending sort order
Returns an array of sorted schools.
'''
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


'''
Displays results of a ranking query.
'''
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


'''
Runs Rankings query page.
'''
@app.route('/rankings')
def rankings():
    return flask.render_template("finalrankings.html")


# Compare functionality
'''
Executes a pqsl query to a database.
'college2' - designates first college
'college1' - designates second college
Returns an array of two schools' data.
'''
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


'''
Displays results of a comparison query.
'''
@app.route('/compare/<college1>/<college2>')
def comparing_stats(college1, college2):
    stats = get_college_stats(college1, college2)
    return flask.render_template("display-compare.html", stats=stats)


'''
Runs Compare query page.
'''
@app.route('/compare')
def compare():
    dropdownOptions = get_name_options()
    return flask.render_template("finalcompare.html", DropdownOptions = dropdownOptions)


# Financial Aid functionality

'''
Executes a pqsl query to a database.
'income' - specifies income bracket
'colleges' - specifies college to query financial aid
Returns a single monetary value.
'''
def get_aid_stats(income, colleges):#colleges
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


'''
Displays the results of a financial aid query.
'''
@app.route('/financialaid/<income>/<colleges>')
def comparing_aidStats(income, colleges):
    aid = get_aid_stats(income, colleges) #colleges
    
    return flask.render_template("display-aid.html", aid=aid, colleges=colleges)


'''
Runs Financial Aid query page.
'''
@app.route('/financialaid')
def financialAid():
    dropdownOptions = get_name_options()
    return flask.render_template("finalfinancial-aid.html",  DropdownOptions = dropdownOptions)



# Popular Major functionality
'''
Executes a pqsl query to a database.
'major' - specifies value to search for matches
Returns an array of schools with compatible popular major.
'''
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


'''
Displays the results of a popular major query
'''
@app.route('/popularmajor/<major>')
def displayMajors(major):
    stats = get_major_stats(major)
    return flask.render_template("display-major.html", stats=stats, major=major)


'''
Runs Popular Major query page.
'''
@app.route('/popularmajor')
def popMajor():
    return flask.render_template("finalpopular-major.html")

'''
Runs map page.
'''
@app.route('/map')
def map():
    return flask.render_template("display-map.html")


if __name__ == '__main__':
    my_port = 5223
    app.run(host = '0.0.0.0', port = my_port)
