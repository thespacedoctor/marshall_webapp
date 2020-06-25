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


class test_views_resources_transients_element(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

        # xt-setup-unit-testing-files-and-folders

        self.testIni = moduleDirectory + "/../../../test.ini#marshall_webapp"

        self.testSettings = settings
        self.settings = settings

        utKit("").refresh_database()

    def test_views_reosurces_transients_element_get(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}
        respsonse = self.testapp.get('/transients/1',
                                     params=params)
        self.assertEqual(respsonse.status_code, 200)

    def test_views_reosurces_transients_element_post(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}
        respsonse = self.testapp.post('/transients/1',
                                      params=params)
        self.assertEqual(respsonse.status_code, 200)

    def test_views_reosurces_transients_element_delete(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}
        respsonse = self.testapp.delete('/transients/1',
                                        params=params, status=404)
        self.assertEqual(respsonse.status_code, 404)

    def test_views_reosurces_transients_element_put(self):
        # PARAM DICTIONARY = URL TOKENS
        params = {}
        respsonse = self.testapp.put('/transients/1',
                                     params=params)
        self.assertEqual(respsonse.status_code, 200)

    def test_02_views_reosurces_transients_element_put_move(self):

        params = {
            "method": "put",
            "mwl": "inbox",
        }
        respsonse = self.testapp.put('/transients/1',
                                     params=params)
        self.assertEqual(respsonse.status_code, 200)

    def test_views_reosurces_transients_element_put_priority(self):

        params = {
            "observationPriority": "3",
            "method": "put",
        }
        respsonse = self.testapp.put('/transients/1',
                                     params=params)
        self.assertEqual(respsonse.status_code, 200)

    def test_views_reosurces_transients_element_put_pi(self):

        params = {
            "method": "put",
            "piName": "boblin",
            "piEmail": "d.r.young@qub.ac.uk",
            "redirectURL": "/marshall/transients/1",
        }
        respsonse = self.testapp.put('/transients/1',
                                     params=params)
        self.assertEqual(respsonse.status_code, 302)

    def test_views_reosurces_transients_element_post_classification(self):

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
        # print(respsonse)
        self.assertEqual(respsonse.status_code, 302)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
