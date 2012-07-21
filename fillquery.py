#!/usr/bin/python

import re

def fillquery(q, data):
    query = q
    for i in range(0, len(data)):
        query = query.replace("$"+str(i+1), str(data[i]))
    return query
        
