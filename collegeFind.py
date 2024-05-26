import flask
import psycopg2

app = flask.Flask(__name__)


@app.route('/rankings')
def rankings():

    return flask.render_template("finalrankings.html")

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

  return flask.render_template("finalcompare.html")

@app.route('/financialaid')
def financialAid():
    return flask.render_template("finalfinancial-aid.html")

@app.route('/popmajor')
def popMajor():

    return flask.render_template("finalpopular-major.html")

@app.route('/')
def home():

    return flask.render_template("finalhome.html")

if __name__ == '__main__':
    my_port = 5123
    app.run(host = '0.0.0.0', port = my_port)
