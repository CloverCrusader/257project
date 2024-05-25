import flask
import psycopg2

app = flask.Flask(__name__)


@app.route('/rankings')
def rankings():

    return flask.render_template("ranking-test.html")

@app.route('/rankings/<rate>/<ascdesc>')
def rankQuery():

    conn = psycopg2.connect(
                host="localhost",
                port=5432,   
                database="rapaczs",
                user="rapaczs",
                password="chip979bond")
        
    if conn is None:
        conn.close()
        return None
            
    cur = conn.cursor()

    rateOptions = { 'acceptrate' : 'ORDER BY acceptrate' , 'gradrate' : 'ORDER BY gradrate' , 'tuition' : 'ORDER BY tuition' }
    titleOptions = { 'accceptrate' : 'Acceptance Rate:' , 'gradrate' : 'Graduation Rate:' , 'tuition' : 'Average Tuition:' }
    rankOptions = {'desc' : 'DESC' , 'asc' : 'ASC' }

    order = rateOptions[rate] + rankOptions[ascdesc]

    sql = f'SELECT state, school, {rate} FROM schoolstats {order};'

    cur.execute( sql )

    results = cur.fetchall()
    html = ""
    title = titleOptions[rate]

    for i in 10:
        if results[i] is not None:
            rankValue = results[i][2]
            html = html + f'<p> School: {name}, Location: {state}, {title} {rankvalue} </p>\n'

    return flask.render_template("rankings.html", rankedSchools = html)
    
@app.route('/compare')
def compare():

  html_string = get_name_options()
  return flask.render_template("compare.html", DropdownOptions = html_string)

@app.route('/comparingStats') # update naming conventions throughout files to be in line with convention
def comparingStats():

  return flask.render_template("comparingStats.html")

@app.route('/')
def home():

    return flask.render_template("home.html")

if __name__ == '__main__':
    my_port = 5123
    app.run(host = '0.0.0.0', port = my_port)
