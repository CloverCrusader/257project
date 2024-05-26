import flask
import psycopg2

app = flask.Flask(__name__)

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

    titleOptions = {'acceptrate' : 'Acceptance Rate:', 'gradrate' : 'Graduation Rate:', 'tuition' : 'Average Tuition:'}

    head = ""
    tail = ""
    if rate == 'tuition':
      head = head + "$"
    else:
      tail = tail + "%"

    stats = get_ranking_stats(rate, lowhigh)

    return render_template("display-rankings.html", stats=stats, rate=rate, title=titleOptions[rate], head=head, tail=tail)

@app.route('/rankings')
def rankings():

    return flask.render_template("finalrankings.html")
    
@app.route('/compare')
def compare():

  return flask.render_template("finalcompare.html")

@app.route('/financialaid')
def financialAid():
    return flask.render_template("finalfinancial-aid.html")

@app.route('/popularmajor')
def popMajor():

    return flask.render_template("finalpopular-major.html")

if __name__ == '__main__':
    my_port = 5123
    app.run(host = '0.0.0.0', port = my_port)
