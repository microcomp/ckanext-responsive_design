import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
import json
import os

import ckan.logic
import ckan.model as model
from ckan.common import _, c
import logging
import helpers
import __builtin__

class ResponsiveDesign(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)


    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')


    def get_helpers(self):
        return {'recent_datasets': helpers.recent_datasets,
                'uv_url' : helpers.uv_url,
                'xwiki': helpers.xwiki,
                'geomodul_url': helpers.geomodul_url,
                'onto_editor': helpers.onto_editor,
                'get_urls':helpers.get_urls,
                'raw_packages_by_week': helpers.raw_packages_by_week,
                'userCountHelper': helpers.userCountHelper,
                'biggest_orgs':helpers.biggest_orgs}

