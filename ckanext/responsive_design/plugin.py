import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
import json
import os

import ckan.logic
import ckan.model as model
from ckan.common import _, c
import logging
import homepage
import __builtin__

class ResponsiveDesign(plugins.SingletonPlugin):

    '''An example theme plugin.

    '''
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    plugins.implements(plugins.IConfigurable)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')


    def get_helpers(self):
        return {'recent_datasets': homepage.recent_datasets,
                'uv_url' : homepage.uv_url,
                'xwiki': homepage.xwiki,
                'geomodul_url': homepage.geomodul_url,
                'onto_editor': homepage.onto_editor,
                'user_req_url':homepage.user_req_url}

    def configure(self, config):
        self.site_url = config.get('ckan.site_url', None)
        __builtin__.site_url = self.site_url

        self.onto_editor = config.get('ckan.onto_url', None)
        __builtin__.onto_editor = self.onto_editor

        self.xwiki_url = config.get('ckan.xwiki.url', None)
        __builtin__.xwiki_url = self.xwiki_url

        self.user_req_url = config.get('ckan.user_req.url', None)
        __builtin__.user_req_url = self.user_req_url

        self.uv_url = config.get('odn.uv.url', None)
        __builtin__.uv_url = self.uv_url
        self.geomodul_url = config.get('ckan.geomodul.url', None)
        __builtin__.geomodul_url = self.geomodul_url

