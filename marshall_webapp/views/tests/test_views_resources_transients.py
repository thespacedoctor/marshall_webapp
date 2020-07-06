from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import yaml
from marshall_webapp.utKit import utKit
from fundamentals import tools
from os.path import expanduser
from dryxPyramid.utKit import BaseTest
home = expanduser("~")

packageDirectory = utKit("").get_project_root()
# settingsFile = packageDirectory + "/test_settings.yaml"
settingsFile = home + "/git_repos/_misc_/settings/marshall/test_settings.yaml"

exists = os.path.exists(settingsFile)
if exists:
    su = tools(
        arguments={"settingsFile": settingsFile},
        docString=__doc__,
        logLevel="DEBUG",
        options_first=False,
        projectName=None,
        defaultSettingsFile=False
    )
    arguments, settings, log, dbConn = su.setup()

    # SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
    moduleDirectory = os.path.dirname(__file__)
    pathToInputDir = moduleDirectory + "/input/"
    pathToOutputDir = moduleDirectory + "/output/"

    try:
        shutil.rmtree(pathToOutputDir)
    except:
        pass
    # COPY INPUT TO OUTPUT DIR
    shutil.copytree(pathToInputDir, pathToOutputDir)

    # Recursively create missing directories
    if not os.path.exists(pathToOutputDir):
        os.makedirs(pathToOutputDir)


class test_views_resources_transients(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

        # xt-setup-unit-testing-files-and-folders

        self.testIni = moduleDirectory + "/../../../test.ini#marshall_webapp"

        self.testSettings = settings
        self.settings = settings

    def test_01_views_resources_transients_post(self):
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

    def test_views_resources_transients_gets(self):
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
        # print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "csv"
        respsonse = self.testapp.get('/transients',
                                     params=params)
        # print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "plain_table"
        respsonse = self.testapp.get('/transients',
                                     params=params)
        # print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = None
        respsonse = self.testapp.get('/transients',
                                     params=params)
        # print respsonse
        self.assertEqual(respsonse.status_code, 200)

    def test_views_resources_transients_downloads(self):
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
        # print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "csv"
        respsonse = self.testapp.get('/transients',
                                     params=params)
        # print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "plain_table"
        respsonse = self.testapp.get('/transients',
                                     params=params)
        # print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = None
        respsonse = self.testapp.get('/transients',
                                     params=params)
        # print respsonse
        self.assertEqual(respsonse.status_code, 200)

    def test_views_resources_transients_search(self):

        respsonse = self.testapp.get('/transients',
                                     params={"search": "TestSource", "format": "plain_table"})
        # print(respsonse)
        self.assertEqual(respsonse.status_code, 200)

    def test_views_resources_transients_function_exception(self):

        from marshall_webapp.views import views_resources_transients
        try:
            this = transients_view(
                log=log,
                settings=settings,
                fakeKey="break the code"
            )
            this.get()
            assert False
        except Exception as e:
            assert True
            print(str(e))
