#!/usr/bin/python

import ConfigParser

class DBParams:
    engine = ""
    host = ""
    port = 0
    database = ""
    username = ""
    password = ""
    select = ""
    check = ""
    update = ""
    insert = ""

    def __repr__(self):
        return "DBParams: engine: " + self.engine + ", host: " + self.host + ", port: " + str(self.port) + ", dbname: " + self.database + ", username: " + self.username + ", passwd: " + self.password 

def getDatabaseParams(cfg, section):
    ret = DBParams()
    ret.engine = cfg.get(section, "engine")
    ret.host = cfg.get(section, "host")
    ret.port = cfg.getint(section, "port")
    ret.database = cfg.get(section, "database")
    ret.username = cfg.get(section, "username")
    ret.password = cfg.get(section, "password")
    if cfg.has_option(section, "select"):
        ret.select = cfg.get(section, "select")
    if cfg.has_option(section, "check"):
        ret.check = cfg.get(section, "check")
    if cfg.has_option(section, "update"):
        ret.update = cfg.get(section, "update")
    if cfg.has_option(section, "insert"):
        ret.insert = cfg.get(section, "insert")

    return ret

def parse(cfg):
    config = ConfigParser.RawConfigParser()
    config.read(cfg)
    
    source = getDatabaseParams(config, 'source')
    dest = []
    i = 1
    while True:
        section = 'dest' + str(i)
        if not config.has_section(section):
            break
        print section
        
        d = getDatabaseParams(config, section)
        dest.append(d)
        i = i + 1
    
    ret = {}
    ret["source"] = source
    ret["dest"] = dest
    return ret

#parser = OptionParser()
#parser.add_option("-f", "--file", dest="filename", help="Read configuration from FILE", metavar="FILE")

#(options, args) = parser.parse_args()

#p = parse(options.filename)

#print p
