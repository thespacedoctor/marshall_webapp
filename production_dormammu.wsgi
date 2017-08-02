from pyramid.paster import get_app, setup_logging
ini_path = '/misc/pessto/git_repos/marshall_webapp/production_dormammu.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
