#!/usr/bin/python
# -*- coding: utf-8

import MySQLdb
from fillquery import fillquery

def fetch_data(dbopt):
    conn = MySQLdb.connect(host=dbopt.host, port=dbopt.port, user=dbopt.username, passwd=dbopt.password, db=dbopt.database, charset='utf8', use_unicode = True)
    conn.set_character_set('utf8')

    cur = conn.cursor()
    cur.execute('SET NAMES utf8;')
    cur.execute(dbopt.select)
    ret = cur.fetchall()

    cur.close()
    conn.close()
    return ret

def execute(dbopt, q, data):
    conn = MySQLdb.connect(host=dbopt.host, port=dbopt.port, user=dbopt.username, passwd=dbopt.password, db=dbopt.database, charset='utf8', use_unicode = True)
    cur = conn.cursor()
    
    query = fillquery(q, data)

    print query
    cur.execute(query)

    cur.execute("COMMIT")
    
    cur.close()
    conn.close()

