import os
import shutil
import unittest
import yaml
from pyramid import testing
import pymysql as ms
from fundamentals import tools
from marshall_webapp.utKit import utKit
from dryxPyramid.utKit import BaseTest

moduleDirectory = os.path.dirname(__file__)

su = tools(
    arguments={"settingsFile": moduleDirectory + "/../../test_settings.yaml"},
    docString=__doc__,
    logLevel="WARNING",
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
    moduleDirectory + "/../../test_settings.yaml", 'r')
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

    def test_01_views_transients_post(self):
        utKit.refresh_database()
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
        respsonse = self.testapp.post("/transients", params=params, status=302)
        self.assertEqual(respsonse.status_code, 302)

    def test_views_transients_gets(self):
        params = {
            "format": "json",
            "sortBy": "currentMagnitudeDate",
            "filterOp1": "<",
            "filterOp2": "=",
            "filterText2": "null",
            "filterText1": "with+<strong>decDeg+<+30</strong>+",
            "filterValue2": "False",
            "filterValue1": "30",
            "sortDesc": "True",
            "filterBy2": "False",
            "filterBy1": "decDeg",
            "limit": "100",
            "ticketLimit": "10",
            "tableLimit": "100",
            "pageStart": "0",
            "method": "get",
            "mwl": "inbox",
        }

        respsonse = self.testapp.get('/transients',
                                     params=params)
        print respsonse
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "csv"
        respsonse = self.testapp.get('/transients',
                                     params=params)
        print respsonse
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "plain_table"
        respsonse = self.testapp.get('/transients',
                                     params=params)
        print respsonse
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = None
        respsonse = self.testapp.get('/transients',
                                     params=params)
        # print respsonse
        self.assertEqual(respsonse.status_code, 200)

    def test_views_transients_downloads(self):
        params = {
            "format": "json",
            "sortBy": "currentMagnitudeDate",
            "filterOp1": "null",
            "filterOp2": "=",
            "filterText2": "null",
            "filterText1": "null",
            "filterValue2": "False",
            "filterValue1": "null",
            "sortDesc": "True",
            "filename": "pessto_marshall_inbox",
            "filterBy2": "False",
            "filterBy1": "null",
            "limit": "100",
            "ticketLimit": "10",
            "tableLimit": "100",
            "pageStart": "0",
            "method": "get",
            "mwl": "inbox",
        }

        respsonse = self.testapp.get('/transients',
                                     params=params)
        print respsonse
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "csv"
        respsonse = self.testapp.get('/transients',
                                     params=params)
        print respsonse
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "plain_table"
        respsonse = self.testapp.get('/transients',
                                     params=params)
        print respsonse
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = None
        respsonse = self.testapp.get('/transients',
                                     params=params)
        # print respsonse
        self.assertEqual(respsonse.status_code, 200)

    def test_views_transients_element(self):

        respsonse = self.testapp.get('/transients/1',
                                     params={})
        self.assertEqual(respsonse.status_code, 200)

    def test_views_transients_search(self):

        respsonse = self.testapp.get('/transients',
                                     params={"search": "TestSource", "format": "plain_table"})
        print respsonse
        self.assertEqual(respsonse.status_code, 200)

    def test_views_transients_classification(self):

        params = {
            "clsSource": "atel",
            "clsObsdate": "2022-08-12",
            "clsType": "supernova",
            "clsSnClassification": "Ib",
            "clsRedshift": "3.4",
            "clsSendTo": "no",
            "clsClassificationWRTMax": "at+max",
            "redirectURL": "/marshall/transients/1",
        }
        respsonse = self.testapp.post('/transients/1',
                                      params=params)
        print respsonse
        self.assertEqual(respsonse.status_code, 302)

    def test_views_transients_put_pi(self):

        params = {
            "method": "put",
            "piName": "boblin",
            "piEmail": "d.r.young@qub.ac.uk",
            "redirectURL": "/marshall/transients/1",
        }
        respsonse = self.testapp.put('/transients/1',
                                     params=params)
        self.assertEqual(respsonse.status_code, 302)

    def test_02_views_transients_put_move(self):

        params = {
            "method": "put",
            "mwl": "inbox",
        }
        respsonse = self.testapp.put('/transients/1',
                                     params=params)
        self.assertEqual(respsonse.status_code, 200)

    def test_views_transients_put_priority(self):

        params = {
            "observationPriority": "3",
            "method": "put",
        }
        respsonse = self.testapp.put('/transients/1',
                                     params=params)
        self.assertEqual(respsonse.status_code, 200)

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
