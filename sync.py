#!/usr/bin/python

import cfg
from optparse import OptionParser

import pgsql
import mysql

def fetch(dbopt):
    if dbopt.engine == "postgres":
        return pgsql.fetch_data(dbopt)
    elif dbopt.engine == "mysql":
        return mysql.fetch_data(dbopt)
    else:
        return None

def execute(dbopt, query, data):
    if dbopt.engine == "postgres":
        pgsql.execute(dbopt, query, data)
    elif dbopt.engine == "mysql":
        mysql.execute(dbopt, query, data)

def arrayToHash(ary):
    ret = {}
    for i in ary:
        id = i[0]
        new_ary = i[1:]
        ret[id] = new_ary
    return ret

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="Read configuration from FILE", metavar="FILE")

(options, args) = parser.parse_args()

p = cfg.parse(options.filename)

print p

data = {}
data["source"] = arrayToHash(fetch(p["source"]))
data["dest"] = []
for dbopt in p["dest"]:
    data["dest"].append(arrayToHash(fetch(dbopt)))

index = 0
for dest in data["dest"]:
    update = []
    insert = []
    for i in data["source"].keys():
        if i in dest.keys():
            # update smth
            if dest[i] != data["source"][i]:
                update.append(i)
        else:
            insert.append(i)

    print "Update: " + str(update)
    print "Insert: " + str(insert)

    dbopt = p["dest"][index]

    for i in update:
        d = [i] + list(data["source"][i])
        execute(dbopt, dbopt.update, d)

    for i in insert:
        d = [i] + list(data["source"][i])
        execute(dbopt, dbopt.insert, d)

    index = index + 1

print data

