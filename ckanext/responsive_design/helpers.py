import logging
import ckan.lib.helpers as h
import ckan.plugins as p
from sqlalchemy import Table, select, func, and_, desc
import ckan.model as model
from ckan.common import _, c
import ckan.plugins.toolkit as toolkit
from pylons import config, session
cache_enabled = False
import datetime
_VALID_GRAVATAR_DEFAULTS = ['404', 'mm', 'identicon', 'monsterid',
                            'wavatar', 'retro']
from webhelpers.html import escape, HTML, literal, url_escape
def big_orgs():
    dts =  model.Session.query(model.Package.owner_org, func.count(model.Package.owner_org)).group_by(model.Package.owner_org).all()
    result = []
    for i in dts:
        org = model.Session.query(model.Group).filter(model.Group.id == i[0]).first()
        result.append({'id':org.id, 'title':org.title, 'image_url':org.image_url, 'package_count':i[1]})

    return result


def css_cache_helper():
    date = datetime.datetime.now()
    result = "version={}".format("1.0")
    return result 

def sum_org():
    orgs =  model.Session.query(model.Group).all()
    return len(orgs)
def sum_dts():
    dts = model.Session.query(model.Package).filter(model.Package.state == 'active').all()
    return len(dts)

def sum_usr():
    usr = model.Session.query(model.User).filter(model.User.state == 'active').all()
    return len(usr)


def table(name):
    return Table(name, model.meta.metadata, autoload=True)
def public_apps():
    try:
        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author,
                   'auth_user_obj': c.userobj,
                   'for_view': True}
        apps = toolkit.get_action('list_apps')(context, {})
        return len(apps)
    except IndexError:
        return 0

DATE_FORMAT = '%Y-%m-%d'
log = logging.getLogger(__name__)
def biggest_orgs():
    context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author,
                   'auth_user_obj': c.userobj,
                   'for_view': True}
    data_dict = {}
    orgs = toolkit.get_action('m_organization_list')(context, data_dict)
    orgs = orgs[:4]
    return orgs

def raw_packages_by_week():

    rev_stats = RevisionStats()

    c.num_packages_by_week = rev_stats.get_num_packages_by_week()
    c.raw_packages_by_week = []
    c.packages_by_week = []
    for week_date, num_packages, cumulative_num_packages in c.num_packages_by_week:
        c.packages_by_week.append('[new Date(%s), %s]' % (week_date.replace('-', ','), cumulative_num_packages))
        c.raw_packages_by_week.append({'date': h.date_str_to_datetime(week_date), 'total_packages': cumulative_num_packages})

    return c.raw_packages_by_week
 
def uv_url():
    uv_url = config.get('odn.uv.url', None)
    if uv_url == None or uv_url == "":
        uv_url = 'http://www.unifiedviews.eu/'
    return uv_url

def HR(uRoles, lRoles):
    if lRoles[0] == 'all':
        return True
    for i in uRoles:
        if i in lRoles:
            return True
    return False
def get_urls(text):
    user_roles = session.get('ckanext-cas-roles', [])
    _list =sorted([x for x in set( x.split('.')[2] for x in [x for x in config.keys() if text in x])])
    result = []
    for i in _list:

        try:
            sk_text = config.get(text+i+'.description_sk').decode('utf8')
        except AttributeError:
            sk_text = ""
        try:
            en_text = config.get(text+i+'.description_en').decode('utf8')
        except AttributeError:
            en_text = ""

        try:
            popis = config.get(text+i+'.title').decode('utf8')
        except AttributeError:
            popis = ""

        try:
            role = [x.strip() for x in config.get(text+i+'.privilege').split(',')]
        except AttributeError:
            role = ["MOD-R-DATA"]

        try:
            name = config.get(text+i+'.name').decode('utf8')
        except AttributeError:
            try:
                link = config.get(text+i+'.url')
                if link[0] =='*':
                    a = config.get(text+i+'.url')[1:]
                    a = a.split(',')
                    ll = {}
                    ll['controller'] = a[0].split('=')[1]
                    ll['action'] = a[1].split('=')[1]
                    link = toolkit.url_for(controller=ll['controller'], action=ll['action'])
                name = link
            except AttributeError:
                name = ""
            

        try:
            result.append({'name':name, 
                           'url':config.get(text+i+'.url'), 
                           'role':role, 
                           'popis':popis,
                           'sk_text':sk_text,
                           'en_text':en_text})
        except AttributeError:
            pass
    result = [x for x in result if x != None]
    sys = False
    if c.userobj and c.userobj.sysadmin:
        sys = True
    result = [x for x in result if (HR(user_roles, x['role']) or sys)]
    result2 = []
    for i in result:
        if i['url'][0] == '*':
            a = i['url'][1:]
            a = a.split(',')
            ll = {}
            ll['controller'] = a[0].split('=')[1]
            ll['action'] = a[1].split('=')[1]
            i['url'] = toolkit.url_for(controller=ll['controller'], action=ll['action'])
        result2.append(i)
    return result2

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
def userCountHelper():
    context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author,
                   'auth_user_obj': c.userobj,
                   'for_view': True}
    users = toolkit.get_action('user_list')(context, {})
    return len(users)

def recent_datasets(ll=5):
    context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author,
                   'auth_user_obj': c.userobj,
                   'for_view': True}
    
    res = []
    result= []
    '''data_dict= {'rows':ll}
    resp = toolkit.get_action('m_package_search')(context, data_dict)
    for i in resp["results"]:
        title = i['display_name']
        if len(i['display_name']) > 100:
            title= title[0:85]+"..."
        result.append({'title':title, 'id':i['id']})'''
    raw_data = model.Session.query(model.Package).order_by(desc(model.Package.metadata_modified)).limit(ll)
    for i in raw_data:
        title = i.title
        if len(i.title) > 100:
            title= title[0:85]+"..."
        result.append({'title':title, 'id':i.id})
    return result

def gravatar_add_alt(inp):
    return literal('class="gravatar" alt=""'.join(inp.split('class="gravatar"')))

def linked_user(user, maxlength=0, avatar=20):
    if user in [model.PSEUDO_USER__LOGGED_IN, model.PSEUDO_USER__VISITOR]:
        return user
    if not isinstance(user, model.User):
        user_name = unicode(user)
        user = model.User.get(user_name)
        if not user:
            return user_name
    if user:
        name = user.name if model.User.VALID_NAME.match(user.name) else user.id
        icon = gravatar(email_hash=user.email_hash, size=avatar)
        displayname = user.display_name
        if maxlength and len(user.display_name) > maxlength:
            displayname = displayname[:maxlength] + '...'
        return icon + u' ' + link_to(displayname,
                                     url_for(controller='user', action='read', id=name))

class RevisionStats(object):
    @classmethod
    def package_addition_rate(cls, weeks_ago=0):
        week_commenced = cls.get_date_weeks_ago(weeks_ago)
        return cls.get_objects_in_a_week(week_commenced,
                                          type_='package_addition_rate')

    @classmethod
    def package_revision_rate(cls, weeks_ago=0):
        week_commenced = cls.get_date_weeks_ago(weeks_ago)
        return cls.get_objects_in_a_week(week_commenced,
                                          type_='package_revision_rate')

    @classmethod
    def get_date_weeks_ago(cls, weeks_ago):
        '''
        @param weeks_ago: specify how many weeks ago to give count for
                          (0 = this week so far)
        '''
        date_ = datetime.date.today()
        return date_ - datetime.timedelta(days=
                             datetime.date.weekday(date_) + 7 * weeks_ago)

    @classmethod
    def get_week_dates(cls, weeks_ago):
        '''
        @param weeks_ago: specify how many weeks ago to give count for
                          (0 = this week so far)
        '''
        package_revision = table('package_revision')
        revision = table('revision')
        today = datetime.date.today()
        date_from = datetime.datetime(today.year, today.month, today.day) -\
                    datetime.timedelta(days=datetime.date.weekday(today) + \
                                       7 * weeks_ago)
        date_to = date_from + datetime.timedelta(days=7)
        return (date_from, date_to)

    @classmethod
    def get_date_week_started(cls, date_):
        assert isinstance(date_, datetime.date)
        if isinstance(date_, datetime.datetime):
            date_ = datetime2date(date_)
        return date_ - datetime.timedelta(days=datetime.date.weekday(date_))

    @classmethod
    def get_package_revisions(cls):
        '''
        @return: Returns list of revisions and date of them, in
                 format: [(id, date), ...]
        '''
        package_revision = table('package_revision')
        revision = table('revision')
        s = select([package_revision.c.id, revision.c.timestamp], from_obj=[package_revision.join(revision)]).order_by(revision.c.timestamp)
        res = model.Session.execute(s).fetchall() # [(id, datetime), ...]
        return res

    @classmethod
    def get_new_packages(cls):
        '''
        @return: Returns list of new pkgs and date when they were created, in
                 format: [(id, date_ordinal), ...]
        '''
        def new_packages():
            # Can't filter by time in select because 'min' function has to
            # be 'for all time' else you get first revision in the time period.
            package_revision = table('package_revision')
            revision = table('revision')
            s = select([package_revision.c.id, func.min(revision.c.timestamp)], from_obj=[package_revision.join(revision)]).group_by(package_revision.c.id).order_by(func.min(revision.c.timestamp))
            res = model.Session.execute(s).fetchall() # [(id, datetime), ...]
            res_pickleable = []
            for pkg_id, created_datetime in res:
                res_pickleable.append((pkg_id, created_datetime.toordinal()))
            return res_pickleable
        if cache_enabled:
            week_commences = cls.get_date_week_started(datetime.date.today())
            key = 'all_new_packages_%s' + week_commences.strftime(DATE_FORMAT)
            new_packages = our_cache.get_value(key=key,
                                               createfunc=new_packages)
        else:
            new_packages = new_packages()
        return new_packages

    @classmethod
    def get_deleted_packages(cls):
        '''
        @return: Returns list of deleted pkgs and date when they were deleted, in
                 format: [(id, date_ordinal), ...]
        '''
        def deleted_packages():
            # Can't filter by time in select because 'min' function has to
            # be 'for all time' else you get first revision in the time period.
            package_revision = table('package_revision')
            revision = table('revision')
            s = select([package_revision.c.id, func.min(revision.c.timestamp)], from_obj=[package_revision.join(revision)]).\
                where(package_revision.c.state==model.State.DELETED).\
                group_by(package_revision.c.id).\
                order_by(func.min(revision.c.timestamp))
            res = model.Session.execute(s).fetchall() # [(id, datetime), ...]
            res_pickleable = []
            for pkg_id, deleted_datetime in res:
                res_pickleable.append((pkg_id, deleted_datetime.toordinal()))
            return res_pickleable
        if cache_enabled:
            week_commences = cls.get_date_week_started(datetime.date.today())
            key = 'all_deleted_packages_%s' + week_commences.strftime(DATE_FORMAT)
            deleted_packages = our_cache.get_value(key=key,
                                                   createfunc=deleted_packages)
        else:
            deleted_packages = deleted_packages()
        return deleted_packages

    @classmethod
    def get_num_packages_by_week(cls):
        def num_packages():
            new_packages_by_week = cls.get_by_week('new_packages')
            deleted_packages_by_week = cls.get_by_week('deleted_packages')
            first_date = (min(datetime.datetime.strptime(new_packages_by_week[0][0], DATE_FORMAT),
                              datetime.datetime.strptime(deleted_packages_by_week[0][0], DATE_FORMAT))).date()
            cls._cumulative_num_pkgs = 0
            new_pkgs = []
            deleted_pkgs = []
            def build_weekly_stats(week_commences, new_pkg_ids, deleted_pkg_ids):
                num_pkgs = len(new_pkg_ids) - len(deleted_pkg_ids)
                new_pkgs.extend([model.Session.query(model.Package).get(id).name for id in new_pkg_ids])
                deleted_pkgs.extend([model.Session.query(model.Package).get(id).name for id in deleted_pkg_ids])
                cls._cumulative_num_pkgs += num_pkgs
                return (week_commences.strftime(DATE_FORMAT),
                        num_pkgs, cls._cumulative_num_pkgs)
            week_ends = first_date
            today = datetime.date.today()
            new_package_week_index = 0
            deleted_package_week_index = 0
            weekly_numbers = [] # [(week_commences, num_packages, cumulative_num_pkgs])]
            while week_ends <= today:
                week_commences = week_ends
                week_ends = week_commences + datetime.timedelta(days=7)
                if datetime.datetime.strptime(new_packages_by_week[new_package_week_index][0], DATE_FORMAT).date() == week_commences:
                    new_pkg_ids = new_packages_by_week[new_package_week_index][1]
                    new_package_week_index += 1
                else:
                    new_pkg_ids = []
                if datetime.datetime.strptime(deleted_packages_by_week[deleted_package_week_index][0], DATE_FORMAT).date() == week_commences:
                    deleted_pkg_ids = deleted_packages_by_week[deleted_package_week_index][1]
                    deleted_package_week_index += 1
                else:
                    deleted_pkg_ids = []
                weekly_numbers.append(build_weekly_stats(week_commences, new_pkg_ids, deleted_pkg_ids))
            # just check we got to the end of each count
            assert new_package_week_index == len(new_packages_by_week)
            assert deleted_package_week_index == len(deleted_packages_by_week)
            return weekly_numbers
        if cache_enabled:
            week_commences = cls.get_date_week_started(datetime.date.today())
            key = 'number_packages_%s' + week_commences.strftime(DATE_FORMAT)
            num_packages = our_cache.get_value(key=key,
                                               createfunc=num_packages)
        else:
            num_packages = num_packages()
        return num_packages

    @classmethod
    def get_by_week(cls, object_type):
        cls._object_type = object_type
        def objects_by_week():
            if cls._object_type == 'new_packages':
                objects = cls.get_new_packages()
                def get_date(object_date):
                    return datetime.date.fromordinal(object_date)
            elif cls._object_type == 'deleted_packages':
                objects = cls.get_deleted_packages()
                def get_date(object_date):
                    return datetime.date.fromordinal(object_date)
            elif cls._object_type == 'package_revisions':
                objects = cls.get_package_revisions()
                def get_date(object_date):
                    return datetime2date(object_date)
            else:
                raise NotImplementedError()
            first_date = get_date(objects[0][1]) if objects else datetime.date.today()
            week_commences = cls.get_date_week_started(first_date)
            week_ends = week_commences + datetime.timedelta(days=7)
            week_index = 0
            weekly_pkg_ids = [] # [(week_commences, [pkg_id1, pkg_id2, ...])]
            pkg_id_stack = []
            cls._cumulative_num_pkgs = 0
            def build_weekly_stats(week_commences, pkg_ids):
                num_pkgs = len(pkg_ids)
                cls._cumulative_num_pkgs += num_pkgs
                return (week_commences.strftime(DATE_FORMAT),
                        pkg_ids, num_pkgs, cls._cumulative_num_pkgs)
            for pkg_id, date_field in objects:
                date_ = get_date(date_field)
                if date_ >= week_ends:
                    weekly_pkg_ids.append(build_weekly_stats(week_commences, pkg_id_stack))
                    pkg_id_stack = []
                    week_commences = week_ends
                    week_ends = week_commences + datetime.timedelta(days=7)
                pkg_id_stack.append(pkg_id)
            weekly_pkg_ids.append(build_weekly_stats(week_commences, pkg_id_stack))
            today = datetime.date.today()
            while week_ends <= today:
                week_commences = week_ends
                week_ends = week_commences + datetime.timedelta(days=7)
                weekly_pkg_ids.append(build_weekly_stats(week_commences, []))
            return weekly_pkg_ids
        if cache_enabled:
            week_commences = cls.get_date_week_started(datetime.date.today())
            key = '%s_by_week_%s' % (cls._object_type, week_commences.strftime(DATE_FORMAT))
            objects_by_week_ = our_cache.get_value(key=key,
                                    createfunc=objects_by_week)
        else:
            objects_by_week_ = objects_by_week()
        return objects_by_week_

    @classmethod
    def get_objects_in_a_week(cls, date_week_commences,
                                 type_='new-package-rate'):
        '''
        @param type: Specifies what to return about the specified week:
                     "package_addition_rate" number of new packages
                     "package_revision_rate" number of package revisions
                     "new_packages" a list of the packages created
                     in a tuple with the date.
                     "deleted_packages" a list of the packages deleted
                     in a tuple with the date.
        @param dates: date range of interest - a tuple:
                     (start_date, end_date)
        '''
        assert isinstance(date_week_commences, datetime.date)
        if type_ in ('package_addition_rate', 'new_packages'):
            object_type = 'new_packages'
        elif type_ == 'deleted_packages':
            object_type = 'deleted_packages'
        elif type_ == 'package_revision_rate':
            object_type = 'package_revisions'
        else:
            raise NotImplementedError()
        objects_by_week = cls.get_by_week(object_type)
        date_wc_str = date_week_commences.strftime(DATE_FORMAT)
        object_ids = None
        for objects_in_a_week in objects_by_week:
            if objects_in_a_week[0] == date_wc_str:
                object_ids = objects_in_a_week[1]
                break
        if object_ids is None:
            raise TypeError('Week specified is outside range')
        assert isinstance(object_ids, list)
        if type_ in ('package_revision_rate', 'package_addition_rate'):
            return len(object_ids)
        elif type_ in ('new_packages', 'deleted_packages'):
            return [ model.Session.query(model.Package).get(pkg_id) \
                     for pkg_id in object_ids ]
