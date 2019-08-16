from pyramid.paster import get_app, setup_logging
ini_path = '/Users/Dave/git_repos/_webapps_/marshall_webapp/production_mac.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
