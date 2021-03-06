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

    def before_map(self, map):
        map.connect('sitemap', '/sitemap',
            controller='ckanext.responsive_design.responsive_design:ResponsiveDesign',
            action='index')
        map.connect('legal', '/legal',
            controller='ckanext.responsive_design.responsive_design:ResponsiveDesign',
            action='legal')
        map.connect('licence', '/licence',
            controller='ckanext.responsive_design.responsive_design:ResponsiveDesign',
            action='licence')
        map.connect('datasets', '/dataset',
            controller='ckanext.responsive_design.responsive_design:ResponsiveDesign',
            action='search')
        map.connect('tools', '/tools',
            controller='ckanext.responsive_design.responsive_design:ResponsiveDesign',
            action='tools')
        map.connect('published-services', '/published-services',
            controller='ckanext.responsive_design.responsive_design:ResponsiveDesign',
            action='published_services')
        return map
    def get_helpers(self):
        return {'recent_datasets': helpers.recent_datasets,
                'uv_url' : helpers.uv_url,
                'xwiki': helpers.xwiki,
                'geomodul_url': helpers.geomodul_url,
                'onto_editor': helpers.onto_editor,
                'get_urls':helpers.get_urls,
                'raw_packages_by_week': helpers.raw_packages_by_week,
                'userCountHelper': helpers.userCountHelper,
                'biggest_orgs':helpers.biggest_orgs,
                'public_apps':helpers.public_apps,
                'css_cache_helper': helpers.css_cache_helper,
                'gravatar_helper': helpers.gravatar_add_alt,
                'sum_org':helpers.sum_org,
                'sum_usr':helpers.sum_usr,
                'sum_dts':helpers.sum_dts,
                'big_orgs':helpers.big_orgs}

