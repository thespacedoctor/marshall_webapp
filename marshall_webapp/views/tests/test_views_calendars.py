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


class test_views_calendars(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

        self.testIni = moduleDirectory + "/../../../test.ini#marshall_webapp"
        self.testSettings = settings
        self.settings = settings

        utKit("").refresh_database()

    def test_01_views_calendars_post(self):
        utKit("").refresh_database()
        params = {}
        # STATUS = 302 ... REDIRECT AFTER POST
        respsonse = self.testapp.post(
            "/calendars", params=params, status=405)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 405)

    def test_views_calendars_get(self):
        params = {}

        respsonse = self.testapp.get('/calendars',
                                     params=params)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 200)

    def test_views_calendars_delete(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}
        respsonse = self.testapp.delete('/calendars',
                                        params=params, status=405)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 405)

    def test_views_calendars_put(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}
        respsonse = self.testapp.put('/calendars',
                                     params=params, status=405)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 405)
