import flask
import psycopg2

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template("home.html")

if __name__ == '__main__':
    my_port = 5123
    app.run(host = '0.0.0.0', port = my_port)