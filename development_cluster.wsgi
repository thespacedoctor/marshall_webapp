from pyramid.paster import get_app, setup_logging
ini_path = '/home/dev/git_repos/_webapps_/marshall_webapp/development_cluster.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
