import os
import psycopg2
import json
from dotenv import load_dotenv
from flask import Flask

host = os.environ['PGHOST'] = 'abnormally-driven-reptile-pdt.a1.pgedge.io'
username = os.environ['PGUSER'] = 'app'
dbname = os.environ['PGDATABASE'] = 'myfirstdb'
os.environ['PGSSLMODE'] = 'require'
os.environ['PGPASSWORD'] = 'nNhwTq56d5q378Mxq46z28XJ'


#dburl = 'postgres://app:nNhwTq56d5q378Mxq46z28XJ@abnormally-driven-reptile-pdt.a1.pgedge.io/myfirstdb'
load_dotenv()

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)

def main1():
    connection = psycopg2.connect()
    print(connection.ConnStatus)
    cursor = connection.cursor()
    cursor.execute('SELECT node_name FROM spock.node')
    node_names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    print(node_names)



#if __name__ == '__main__':
#main1()

conn = psycopg2.connect(database = dbname,
                        user = username,
                        host= host,
                        password = "nNhwTq56d5q378Mxq46z28XJ",
                        port = 5432)
cursor = conn.cursor()
#cursor.execute('SELECT node_name FROM spock.node')
cursor.execute('SELECT * from orders limit 20')
#node_names = [row[0] for row in cursor.fetchall()]
#print(node_names)
jsonresult = {}
for row in cursor.fetchall():
    print(row)
    #json.dumps(row)
cursor.close()
conn.close()

a= 10
b=16
c=6

while (a>=c) or (b>=c):
    print("yes")
    a = a-4
    b = b-2