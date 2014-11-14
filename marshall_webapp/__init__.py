from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid.path import AssetResolver
import yaml
import dryxPyramid


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
    config = Configurator(settings=settings)
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    config.registry.dbmaker = sessionmaker(bind=engine)
    config.add_request_method(db, reify=True)
    # config.include('pyramid_chameleon')

    # The Routes -- add_route(name, pattern)
    config.add_route('transient_comments', '/transient/comments')
    config.add_route(
        'transients_element_comments', '/transients/{elementId}/comments')
    config.add_route('transients', '/transients')
    config.add_route(
        'transients_search', '/transients/search')
    config.add_route('transients_element', '/transients/{elementId}')
    config.add_route('stats', '/stats')
    config.add_route('calendars', '/calendars')
    config.add_route(
        'refresh_sidebar_list_counts', '/actions/refresh_sidebar_list_counts')
    config.add_route('refresh_sidebar_list_counts_element',
                     '/actions/refresh_sidebar_list_counts/{elementId}')

    config.add_route(
        'transientLightcurves', '/transients/{elementId}/lightcurve')
    config.add_route('download', '/download')
    config.add_route('transients_ob_element', '/transients/{elementId}/ob')
    # --- end of routes --- #
    # xpyr-add-route

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
