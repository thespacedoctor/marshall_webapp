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


class test_views_services_refresh_sidebar_list_counts(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

        self.testIni = moduleDirectory + "/../../../test.ini#marshall_webapp"
        self.testSettings = settings
        self.settings = settings
        utKit("").refresh_database()

    def test_views_services_refresh_sidebar_list_counts_put(self):
        params = {}
        respsonse = self.testapp.put(
            "/actions/refresh_sidebar_list_counts", params=params)
        self.assertEqual(respsonse.status_code, 200)
