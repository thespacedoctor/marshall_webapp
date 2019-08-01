import os
import shutil
import unittest
import yaml
from pyramid import testing
from pyramid.path import AssetResolver
from pyramid.request import apply_request_extensions
from paste.deploy.loadwsgi import appconfig
import pymysql as ms
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from fundamentals import tools
from marshall_webapp.utKit import utKit
from dryxPyramid.utKit import BaseTest

moduleDirectory = os.path.dirname(__file__)

su = tools(
    arguments={"settingsFile": moduleDirectory + "/../../test_settings.yaml"},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName="marshall_webapp",
    defaultSettingsFile=False
)
arguments, settings, log, dbConn = su.setup()

# # load settings
# stream = file(
#     "/Users/Dave/.config/marshall_webapp/marshall_webapp.yaml", 'r')
# settings = yaml.load(stream)
# stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
stream = file(
    moduleDirectory + "/../../default_settings.yaml", 'r')
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


import shutil
try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

# xt-setup-unit-testing-files-and-folders


class test_views_transients(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)
        self.testIni = moduleDirectory + "/../../../test.ini#marshall_webapp"
        self.testSettings = settings
        self.settings = settings
        utKit.refresh_database()

    def test_views_transients_post(self):
        self.config.add_route('transients', '/transients')
        self.config.add_route(
            'transients_search', '/transients/search')
        utKit.refresh_database()
        from marshall_webapp.views import transients_view
        params = {
            "objectName": "TestSource",
            "objectImageStamp": "http://thespacedoctor.co.uk/images/thespacedoctor_icon_white_circle.png",
            "objectUrl": "http://thespacedoctor.co.uk",
            "objectSurvey": "testSurvey",
            "objectRa": 155.12595833333333,
            "objectDec": -15.178736944444443,
            "objectRedshift": 0.34,
            "objectMagnitude": 20.3,
            "objectDate": 57627.5
        }

        request = testing.DummyRequest(params=params)
        apply_request_extensions(
            request)

        resource = transients_view(
            request=request
        )
        response = resource.post()
        self.assertEqual(response.status_code, 302)

    def test_views_transients_function_exception(self):

        from marshall_webapp.views import transients_view
        try:
            this = transients_view(
                log=log,
                settings=settings,
                fakeKey="break the code"
            )
            this.get()
            assert False
        except Exception, e:
            assert True
            print str(e)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
