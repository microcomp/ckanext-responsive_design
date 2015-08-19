import urllib
 # -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid
import datetime

import ckan.model as model
import ckan.logic as logic
import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.lib.navl.dictization_functions as df
import ckan.plugins as p
from ckan.common import _, c
import ckan.plugins.toolkit as toolkit
import urllib2
import logging
import ckan.logic
import __builtin__
from ckan.model.package import Package
from pylons import config

import json
def uv_url():
    uv_url = config.get('odn.uv.url', None)
    if uv_url == None or uv_url == "":
        uv_url = 'http://www.unifiedviews.eu/'
    return uv_url

def get_urls(text):
    _list =sorted([x for x in set( x.split('.')[2] for x in [x for x in config.keys() if text in x])])
    result = []
    for i in _list:
        result.append({'name':config.get(text+i+'.name').decode('utf8'), 
                       'url':config.get(text+i+'.url'), 
                       'role':config.get(text+i+'.role'), 
                       'popis':config.get(text+i+'.title').decode('utf8')})
    return result

def onto_editor():
    onto_editor = config.get('ckan.onto_url', None)
    if onto_editor == None or onto_editor == "":
        onto_editor = '#'
    return onto_editor

def geomodul_url():
    geomodul_url = config.get('ckan.geomodul.url', None)
    if geomodul_url == None or geomodul_url == "":
        geomodul_url = '/dashboard'
    return geomodul_url
def xwiki():
    xwiki_url = config.get('ckan.xwiki.url', None)
    if xwiki_url == None or xwiki_url == "":
        xwiki_url = 'http://xwiki.org'
    return xwiki_url

def recent_datasets():
    context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author,
                   'auth_user_obj': c.userobj,
                   'for_view': True}
    
    res = []
    result= []
    data_dict= {'limit':10, 'offset':0, 'page':1}
    resp = toolkit.get_action('current_package_list_with_resources')(context, data_dict)
    for i in resp:
        notes = i['notes']
        if  i['notes'] != None:
            if len(i['notes']) > 300:
                notes = i['notes'][:300]+'...'
        else:
            notes = ""
        res= []
        for r in i['resources']:
            res.append(r['format'])
        result.append({'title':i['title'], 'text': notes, 'url':i['name'], 'resources': res })

    return result

