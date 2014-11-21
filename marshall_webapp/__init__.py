from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid.path import AssetResolver
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
import yaml
import dryxPyramid
from dryxPyramid.security import groupfinder


def db(request):
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
    # authorisation
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(
        settings=settings, root_factory='dryxPyramid.models.acl.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    engine = engine_from_config(settings, prefix='sqlalchemy.')
    config.registry.dbmaker = sessionmaker(bind=engine)
    config.add_request_method(db, reify=True)
    # config.include('pyramid_chameleon')

    # The Routes -- add_route(name, pattern)
    config.add_route('transients_comments', '/transients/comments')
    config.add_route(
        'transients_element_comments', '/transients/{elementId}/comments')
    config.add_route(
        'transients_lightcurves', '/transients/lightcurves')
    config.add_route(
        'transients_element_lightcurves', '/transients/{elementId}/lightcurves')
    config.add_route('transients_element_obs', '/transients/{elementId}/obs')
    config.add_route('transients', '/transients')
    config.add_route(
        'transients_search', '/transients/search')
    config.add_route('transients_element', '/transients/{elementId}')
    config.add_route('stats', '/stats')
    config.add_route('calendars', '/calendars')
    config.add_route(
        'refresh_sidebar_list_counts', '/actions/refresh_sidebar_list_counts')

    # --- end of routes --- #
    # xpyr-add-route

    # Default Routes from dryxPyramid
    config.add_route('download', '/download')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    # xpyr-add-route
    config.add_route('index', '/')
    config.scan()
    config.scan("dryxPyramid")

    # static views
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Add settings from YAML file
    myWebapp = AssetResolver("marshall_webapp")
    theseSettings = config.get_settings()
    settingsPath = myWebapp.resolve(
        theseSettings["settingsFile"]).abspath()
    stream = file(settingsPath, 'r')
    settings = yaml.load(stream)
    config.add_settings(settings)
    stream.close()

    import MySQLdb as ms
    # SETUP A DATABASE CONNECTION BASED ON WHAT ARGUMENTS HAVE BEEN PASSED
    if "database settings" in settings:
        host = settings["database settings"]["host"]
        user = settings["database settings"]["user"]
        passwd = settings["database settings"]["password"]
        dbName = settings["database settings"]["db"]
        dbConn = ms.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=dbName,
            use_unicode=True,
            charset='utf8'
        )
        config.add_settings({"dbConn": dbConn})

    config.add_renderer('json', dryxPyramid.renderers.renderer_json)
    config.add_renderer('csv', dryxPyramid.renderers.renderer_csv)
    config.add_renderer(
        'plain_table', dryxPyramid.renderers.renderer_plain_table)
    config.add_renderer(
        'plain_text', dryxPyramid.renderers.renderer_plain_text)

    return config.make_wsgi_app()

import views
import templates
import models
