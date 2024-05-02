import mysql.connector
from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor',
    database='AgendaFecaf'
)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"