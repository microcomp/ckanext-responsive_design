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


import json
def recent_datasets():
    most_recent = model.Session.query(model.Package) \
                    .filter(model.Package.state == 'active' and model \
                    .Package.type == 'dataset').order_by(model.Package.metadata_modified.desc()) \
                    .limit(10).all()
    result = []
    for i in most_recent:
    	#text = model.Session.query(model.PackageRevision).filter(model.PackageRevision.name == i.name).first().notes
        notes = i.notes
    	if len(i.notes) > 300:
            notes = i.notes[:300]+'...'
        formats = model.Session.query(model.Resource).filter()
        id = i.id
        logging.warning(__builtin__.site_url)
        '''try:
            response = json.load(urllib2.urlopen(__builtin__.site_url+'api/3/action/resource_search?query=url:'+i.id))['result']['results']
        except URLError:
            response = json.load(urllib2.urlopen('http://'+__builtin__.site_url+'api/3/action/resource_search?query=url:'+i.id))['result']['results']
        else:'''
        response = json.load(urllib2.urlopen('http://'+__builtin__.site_url+'/api/3/action/resource_search?query=url:'+i.id))['result']['results']
        
        response = json.load(urllib2.urlopen(__builtin__.site_url+'api/3/action/resource_search?query=url:'+i.id))['result']['results']

        res = []
        for j in response:
        	res.append(j["format"])

        result.append({'title':i.title, 'text': notes, 'url':i.name, 'resources': res })
    return result

