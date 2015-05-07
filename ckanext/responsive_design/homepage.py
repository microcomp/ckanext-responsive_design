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
def xwiki():
    if __builtin__.xwiki_url == None or __builtin__.xwiki_url == "":
        __builtin__.xwiki_url = 'http://xwiki.org'
    return __builtin__.xwiki_url
def recent_datasets():
    most_recent = model.Session.query(Package) \
                    .filter_by(private=False).filter_by(type='dataset').filter_by(state='active').order_by(Package.metadata_modified.desc()) \
                    .limit(10).all()
                    #Package.state == 'active' and Package.type == 'dataset' and 
    result = []
    #most_recent = [x for x in most_recent if x.private == False]
    #most_recent = most_recent[:10]
    for i in most_recent:
        logging.warning(i.private)
    	#text = model.Session.query(model.PackageRevision).filter(model.PackageRevision.name == i.name).first().notes
        notes = i.notes
        if  i.notes != None:
            if len(i.notes) > 300:
                notes = i.notes[:300]+'...'
        else:
            notes = ""
        formats = model.Session.query(model.Resource).filter()
        id = i.id
        logging.warning(__builtin__.site_url)


        data_dict = {"query":'url:'+i.id}
        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author,
                   'auth_user_obj': c.userobj,
                   'for_view': True}
        response = toolkit.get_action('resource_search')(context, data_dict)['results']

        logging.warning(response)
        

        res = []
        for j in response:
        	res.append(j["format"])

        result.append({'title':i.title, 'text': notes, 'url':i.name, 'resources': res })

    return result

