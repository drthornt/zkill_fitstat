#!/usr/bin/env python

import urllib2
import json
import pprint
import ConfigParser
from datetime import datetime
#from elasticsearch import Elasticsearch
import elasticsearch


# response = urllib2.urlopen('https://zkillboard.com/api/kills/shipID/644,638/orderDirection/asc/')

# response = urllib2.urlopen('https://zkillboard.com/api/kills/shipID/11202/orderDirection/asc/limit/10/')
#                             https://zkillboard.com/api/kills/shipID/644/limit/10/
# html = response.read()

# wget -O ares.raw https://zkillboard.com/api/losses/shipID/11202/limit/10/
response = urllib2.urlopen('https://zkillboard.com/api/losses/shipID/11202/limit/10/')
html = response.read()

Config = ConfigParser.ConfigParser()
Config.read("./fitstat.ini")
print "config is "
print Config.sections()
es = elasticsearch.Elasticsearch()

# myconfig("es")['prefix'] = Config.get("es", "prefix")

fitstat_index = Config.get("es", "index")

# print "Elastic search prefix is %s % Config.get("es", "prefix")

# f = open('ares.raw', 'r')
# json_object = json.load(f)

json_object = json.loads(html)

pp = pprint.PrettyPrinter(indent=4)

for kill in json_object:
    # pp.pprint(kill)
    print "KILL"
    #print "\ttype of kill is %s" % type(kill)
    print "\t %s" % kill['killID']
    f = json.dumps(kill)
    # res = es.search(index=fitstat_index, id=kill['killID'])
    try:
        res = es.get(index=fitstat_index, doc_type='kill', id=kill['killID'])
    except elasticsearch.NotFoundError as notfound:
        print 'not found'
        found = 'False'
    except elasticsearch.Elasticsearch.ElasticsearchException as exp:
        print "not found error"
        exit(1)

    # print "%s" % res['found']
    # pp.pprint(res)
    # if res['found'] == 'False':
    if found == 'False':
        print "hits zero , inserting"
        #res = es.index(index="fitstat_v1", doc_type='kill', id=kill['killID'], body=f)
        #print(res['created'])
    else:
        print "Hits > 0 skipping"


