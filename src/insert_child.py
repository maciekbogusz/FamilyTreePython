'''
Created on 13.03.2017

@author: mcbg
'''
from family_member import family_member
from connect import connect


def insert_child(family_member):
    conn = connect()
    cursor = conn.cursor()
        