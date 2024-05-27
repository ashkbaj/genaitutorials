import json
import os
import psycopg2

os.environ['PGHOST'] = 'abnormally-driven-reptile-pdt.a1.pgedge.io'
os.environ['PGUSER'] = 'app'
os.environ['PGDATABASE'] = 'myfirstdb'
os.environ['PGSSLMODE'] = 'require'
os.environ['PGPASSWORD'] = 'nNhwTq56d5q378Mxq46z28XJ'

conn_string ="postgresql://app:nNhwTq56d5q378Mxq46z28XJ@abnormally-driven-reptile.a1.pgedge.io/myfirstdb?sslmode=require"
def main():
    connection = psycopg2.connect()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM customers')
    #node_names = [row[0] for row in cursor.fetchall()]
    node_names = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    print(json.dumps(node_names))
    #print(node_names)

if __name__ == '__main__':
    main()
