from flask import Flask
from flask_cors import CORS
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)


os.environ['PGHOST'] = 'abnormally-driven-reptile-pdt.a1.pgedge.io'
os.environ['PGUSER'] = 'app'
os.environ['PGDATABASE'] = 'myfirstdb'
os.environ['PGSSLMODE'] = 'require'
os.environ['PGPASSWORD'] = 'nNhwTq56d5q378Mxq46z28XJ'

conn_string ="postgresql://app:nNhwTq56d5q378Mxq46z28XJ@abnormally-driven-reptile.a1.pgedge.io/myfirstdb?sslmode=require"

app.config["SQLALCHEMY_DATABASE_URI"] = conn_string
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
@app.route('/')
def hello():
    return 'My First API !!'
