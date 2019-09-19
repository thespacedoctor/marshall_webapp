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
    logLevel="DEBUG",
    options_first=False,
    projectName=None,
    defaultSettingsFile=False
)
arguments, settings, log, dbConn = su.setup()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
stream = file(
    moduleDirectory + "/../../test_settings.yaml", 'r')
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


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


class test_views_actions_refresh_sidebar_list_counts(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)
        self.testIni = moduleDirectory + "/../../../test.ini#marshall_webapp"
        self.testSettings = settings
        self.settings = settings
        utKit.refresh_database()

    def test_views_actions_refresh_sidebar_list_counts_put(self):
        params = {}
        respsonse = self.testapp.put(
            "/actions/refresh_sidebar_list_counts", params=params)
        self.assertEqual(respsonse.status_code, 200)
