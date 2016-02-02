import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.lib.base import BaseController, config
import jinja2
from ckan.common import _, c, g, request

abort = base.abort
render = base.render

class ResponsiveDesign(BaseController):
    def index(self, context=None):
        return render('sitemap/index.html')
    def published_services(self, context=None):
        return render('published_services/index.html')
    def tools(self, context=None):
        return render('tools/index.html')
    
