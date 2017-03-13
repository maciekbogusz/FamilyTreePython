'''
Created on 13.03.2017

@author: mcbg
'''
from config import config
import psycopg2

def connect(query):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        db_output = cur.fetchall()
        print(db_output)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')

if __name__ == '__main__':
    connect()