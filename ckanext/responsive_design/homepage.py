import urllib

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


import json
def uv_url():
    if __builtin__.uv_url == None or __builtin__.uv_url == "":
        __builtin__.uv_url = 'http://www.unifiedviews.eu/'
    return __builtin__.uv_url
def user_req_url():
    if __builtin__.user_req_url == None or __builtin__.user_req_url == "":
        __builtin__.user_req_url = '#'
    return __builtin__.user_req_url
    
def onto_editor():
    if __builtin__.onto_editor == None or __builtin__.onto_editor == "":
        __builtin__.onto_editor = '#'
    return __builtin__.onto_editor

def geomodul_url():
    if __builtin__.geomodul_url == None or __builtin__.geomodul_url == "":
        __builtin__.geomodul_url = '/dashboard'
    return __builtin__.geomodul_url
def xwiki():
    if __builtin__.xwiki_url == None or __builtin__.xwiki_url == "":
        __builtin__.xwiki_url = 'http://xwiki.org'
    return __builtin__.xwiki_url
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

