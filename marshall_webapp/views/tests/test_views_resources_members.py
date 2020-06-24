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

# COMMON STATUS CODES
# 200 OK
# 301 Moved Permanently
# 302 Found - possibly rediected
# 304 Not Modified
# 400 Bad Request
# 403 Forbidden
# 409 Conflict
# 401 Unauthorized
# 404 Not Found
# 405 Method Not Allowed
# 408 Request Timeout
# 429 Too Many Requests
# 500 Internal Server Error
# 504 Gateway Timeout
# 502 Bad Gateway

class test_views_resources_members(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

        self.testIni = moduleDirectory + "/../../../test.ini#marshall_webapp"
        self.testSettings = settings
        self.settings = settings

        utKit("").refresh_database()

    def test_views_resources_members_post(self):
        utKit("").refresh_database()
        # PARAM DICTIONARY = URL TOKENS
        params = {}

        respsonse = self.testapp.post(
            "/members", params=params, status=404)
        self.assertEqual(respsonse.status_code, 404)

    def test_views_resources_members_get(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}

        params["format"] = "html"
        respsonse = self.testapp.get('/members',
                                     params=params)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "json"
        respsonse = self.testapp.get('/members',
                                     params=params)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "csv"
        respsonse = self.testapp.get('/members',
                                     params=params)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = "plain_table"
        respsonse = self.testapp.get('/members',
                                     params=params)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 200)
        params["format"] = None
        respsonse = self.testapp.get('/members',
                                     params=params)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 200)

    def test_views_resources_members_delete(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}
        respsonse = self.testapp.delete('/members',
                                        params=params, status=404)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 404)

    def test_views_resources_members_put(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}
        respsonse = self.testapp.put('/members',
                                     params=params, status=404)
        print(respsonse)
        self.assertEqual(respsonse.status_code, 404)
