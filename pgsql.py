#!/usr/bin/python
# -*- coding: utf-8

import psycopg2
from fillquery import fillquery

def fetch_data(dbopt):
    conn = psycopg2.connect("host="+dbopt.host+" port="+str(dbopt.port)+" dbname="+dbopt.database+" user="+dbopt.username+" password="+dbopt.password)
    
    cur = conn.cursor()
    cur.execute(dbopt.select)
    ret = cur.fetchall()
    
    cur.close()
    conn.close()
    return ret

def execute(dbopt, q, data):
    conn = psycopg2.connect("host="+dbopt.host+" port="+str(dbopt.port)+" dbname="+dbopt.database+" user="+dbopt.username+" password="+dbopt.password)
    
    cur = conn.cursor()
    
    query = dbopt.update
    query = fillquery(q, data)
    
    cur.execute(query)
    
    cur.close()
    conn.close()

