'''
Created on 13.03.2017

@author: mcbg
'''
from config import config
import psycopg2

def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
