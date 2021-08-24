from __future__ import absolute_import
from . import cl_utils
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid.path import AssetResolver
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.settings import aslist
from os.path import expanduser

# ALLOW DEBUG TOOLBAR OVER HTTPS
from pyramid.url import URLMethodsMixin
URLMethodsMixin.static_url_org = URLMethodsMixin.static_url  # backup of original


def https_static_url(self, *args, **kw):
    kw['_scheme'] = 'https'  # add parameter forcing https
    return URLMethodsMixin.static_url_org(self, *args, **kw)  # call backup
URLMethodsMixin.static_url = https_static_url  # replace original with backup


def db(request):
    # database connection
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()
    request.add_finished_callback(cleanup)

    return session


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    import dryxPyramid
    from dryxPyramid.security import groupfinder
    import yaml
    # the main configurator
    config = Configurator(
        settings=settings, root_factory='dryxPyramid.models.models_login_post.RootFactory')

    # add database connection
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    config.registry.dbmaker = sessionmaker(bind=engine)
    config.add_request_method(db, reify=True)

    # Add settings from YAML file

    myWebapp = AssetResolver("marshall_webapp")
    theseSettings = config.get_settings()
    settingsPath = theseSettings["settingsFile"]
    if settingsPath[0] == "~":
        from os.path import expanduser
        home = expanduser("~")
        settingsPath = settingsPath.replace("~/", home + "/")
    if settingsPath[0] != "/":
        settingsPath = myWebapp.resolve(
            theseSettings["settingsFile"]).abspath()
    stream = open(settingsPath, 'r')
    settings = yaml.load(stream)
    config.add_settings(settings)
    config.add_settings({"yaml settings": settings})
    stream.close()

    # add authorisation
    secret = settings["secrets"]["authn policy"]
    authn_policy = AuthTktAuthenticationPolicy(
        secret, callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    # WHEN ADDING RESOURCES HERE ORDER BY MOST GENERAL TO FINEST GRAINED
    # xpyr-add-route

    # SUPER-CLASS RESOURCES
    config.add_route('base_view', '/base')  # --
    config.add_route('base_element_view', '/base/{elementId}')  # --

    # ACTIONS
    config.add_route(
        'refresh_sidebar_list_counts', '/actions/refresh_sidebar_list_counts')  # --

    # STATIC VIEWS/RESOURCES
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view(
        '.codekit-cache', '.codekit-cache', cache_max_age=3600)

    home = expanduser("~")
    settings[
        "cache-directory"] = settings["cache-directory"].replace("~", home)
    print(settings[
        "cache-directory"])
    config.add_static_view(
        'caches', 'marshall_webapp:caches', cache_max_age=3600)
    config.override_asset(to_override='marshall_webapp:caches/',
                          override_with=settings["cache-directory"])

    # TOP-LEVEL SERVICES
    config.add_route('index', '/')  # --
    config.add_route('download', '/download')  # --
    config.add_route('login', '/login')  # --
    config.add_route('logout', '/logout')  # --

    # TOP-LEVEL RESOURCES
    config.add_route('calendars', '/calendars')
    config.add_route('members', '/members')
    config.add_route('transients', '/transients')  # --
    config.add_route('xmatches', '/xmatches')  # --
    config.add_route('stats', '/stats')  # --

    # TOP-LEVEL SUBRESOURCES
    config.add_route('transients_comments', '/transients/comments')  # --
    config.add_route('transients_akas', '/transients/akas')  # --
    config.add_route('transients_context', '/transients/context')  # --
    config.add_route(
        'transients_search', '/transients/search')  # --
    config.add_route('xmatches_catalogues', '/xmatches/catalogues')  # --
    config.add_route('xmatches_searches', '/xmatches/searches')  # --
    config.add_route('xmatches_views', '/xmatches/views')  # --

    # TOP-LEVEL RESOURCE ELEMENTS
    config.add_route('transients_element', '/transients/{elementId}')  # --
    config.add_route('stats_element', '/stats/{elementId}')  # --

    # TOP-LEVEL RESOURCE-ELEMENTS-SUBRESOURCES
    config.add_route(
        'transients_element_comments', '/transients/{elementId}/comments')  # --
    config.add_route(
        'transients_element_context', '/transients/{elementId}/context')  # --
    config.add_route(
        'transients_element_lightcurves', '/transients/{elementId}/lightcurves')  # --
    config.add_route('transients_element_obs',
                     '/transients/{elementId}/obs')  # --
    config.add_route('transients_history',
                     '/transients/{elementId}/history')  # --
    config.add_route(
        'transients_element_akas', '/transients/{elementId}/akas')

    # TOP-LEVEL SUBRESOURCES-ELEMENTS
    config.add_route('xmatches_element_catalogues',
                     '/xmatches/catalogues/{elementId}')  # --
    config.add_route('xmatches_element_searches',
                     '/xmatches/searches/{elementId}')  # --
    config.add_route('xmatches_element_views',
                     '/xmatches/views/{elementId}')  # --

    # SCAN FOR CONFIGURATION DECORATION
    config.scan()
    config.scan("dryxPyramid")

    # add database connection as a setting (incase we want to use pymysql over
    # sqlachemy)
    import pymysql as ms
    # SETUP A DATABASE CONNECTION BASED ON WHAT ARGUMENTS HAVE BEEN PASSED
    if "database settings" in settings:
        host = settings["database settings"]["host"]
        user = settings["database settings"]["user"]
        passwd = settings["database settings"]["password"]
        dbName = settings["database settings"]["db"]
        port = False
        if "port" in settings["database settings"]:
            port = settings["database settings"]["port"]
        dbConn = ms.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=dbName,
            port=port,
            use_unicode=True,
            charset='utf8',
            local_infile=1,
            client_flag=ms.constants.CLIENT.MULTI_STATEMENTS,
            connect_timeout=3600,
            autocommit=True
        )
        config.add_settings({"dbConn": dbConn})

    # add some deafult renderers
    config.add_renderer('json', dryxPyramid.renderers.renderer_json)
    config.add_renderer('csv', dryxPyramid.renderers.renderer_csv)
    config.add_renderer(
        'plain_table', dryxPyramid.renderers.renderer_plain_table)
    config.add_renderer(
        'plain_text', dryxPyramid.renderers.renderer_plain_text)

    config.include('pyramid_debugtoolbar')
    config.set_debugtoolbar_request_authorization(admin_only_debugtoolbar)

    return config.make_wsgi_app()


def admin_only_debugtoolbar(request):
    """
    Enable toolbar for administrators only.
    Returns True when it should be enabled.
    """
    toolbar_enabled = False
    group = ""

    try:
        if ("marshall/" in request.referrer) and "/_debug_toolbar/" in request.url:
            toolbar_enabled = True
    except:
        pass

    for item in request.effective_principals:
        if "group:" in item:
            group = item.replace("group:", "")
    if group == "superadmin":
        toolbar_enabled = True

    return toolbar_enabled
