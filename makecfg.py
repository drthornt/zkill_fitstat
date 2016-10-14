#!/usr/bin/env python

import ConfigParser

# lets create that config file for next time...
cfgfile = open("newcfg.ini",'w')

Config = ConfigParser.ConfigParser()

# add the settings to the structure of the file, and lets write it out...
Config.add_section('es')
Config.set('es','prefix','fitstat')
Config.set('es','server', '127.0.0.1')
Config.write(cfgfile)
cfgfile.close()
