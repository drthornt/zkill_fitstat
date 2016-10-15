#!/usr/bin/env python

import urllib2
import json
import pprint
import ConfigParser
from datetime import datetime
from elasticsearch import Elasticsearch


# response = urllib2.urlopen('https://zkillboard.com/api/kills/shipID/644,638/orderDirection/asc/')

# response = urllib2.urlopen('https://zkillboard.com/api/kills/shipID/11202/orderDirection/asc/limit/10/')
#                             https://zkillboard.com/api/kills/shipID/644/limit/10/
# html = response.read()

# wget -O ares.raw https://zkillboard.com/api/losses/shipID/11202/limit/10/


Config = ConfigParser.ConfigParser()
Config.read("./fitstat.ini")
print "config is "
print Config.sections()
es = Elasticsearch()

# myconfig("es")['prefix'] = Config.get("es", "prefix")

# print "Elastic search prefix is %s % Config.get("es", "prefix")

f = open('ares.raw', 'r')

json_object = json.load(f)

pp = pprint.PrettyPrinter(indent=4)

for kill in json_object:
    # pp.pprint(kill)
    print "KILL"
    #print "\ttype of kill is %s" % type(kill)
    print "\t %s" % kill['killID']
    # for thing in kill:
    #    print "type of thing is %s" % type(thing)
    f = json.dumps(kill)
    res = es.index(index="fitstat_v1", doc_type='kill', id=kill['killID'], body=f)
    print(res['created'])
    


