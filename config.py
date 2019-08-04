#!/usr/bin/python
from configparser import ConfigParser
from pathlib import Path
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db
def emailconfig(filename='database.ini', section='mail'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    emailinfo = []
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            emailinfo.append(param[1])
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return emailinfo
def responseconfig(filename='database.ini', section='responsebot'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    botinfo = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            botinfo[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return botinfo
def scannerconfig(filename='database.ini', section='scannerbot'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    botinfo = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            botinfo[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return botinfo