from pyramid.paster import get_app, setup_logging
ini_path = '/home/marshall/git_repos/_webapps_/marshall_webapp/developement_cluster.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
