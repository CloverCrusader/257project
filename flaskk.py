import flask
import psycopg2

app = flask.Flask(__name__)

minTuition = 'ORDER BY tuition'
maxTuition = 'ORDER BY tuition DESC'
minAcceptance = 'ORDER BY acceptrate'
maxAcceptance = 'ORDER BY acceptrate DESC'
minGradrate = 'ORDER BY gradrate'
maxGradrate = 'ORDER BY gradrate DESC'

rankOptions = [maxTuition, minTuition, maxAcceptance, minAcceptance, maxGradrate, minGradrate]

@app.route('/rankings')
def rankings():
    return flask.render_template("ranking-test.html")

@app.route('/rankings/<index>')
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

    rankOrder = rankOptions[int(index)]

    sql = "SELECT * FROM schoolstats WHERE code = %s;"

    query = (rankOrder, )
    cur.execute( sql, query)

    results = cur.fetchall()
    html = ""

    for i in 10:
        if results[i] is not None:
            school = results[i]
            state = school[0]
            name = school[1]
            tuition = school[2]
            acceptance = school[3]
            graduation = school[4]
            major = school[5]
            # I do not know how to make the following fit in 120 columns without breaking it.
            html = html + f'<p> School: {name},Location: {state}, Average Tuition: {tuition}, Acceptance Rate: {acceptance}, Graduation Rate: {graduation}, Largest Major: {major} </p>\n'

    return flask.render_template("", rankedSchools = html)
    


@app.route('/')
def home():
    return flask.render_template("home.html")

if __name__ == '__main__':
    my_port = 5123
    app.run(host = '0.0.0.0', port = my_port)
