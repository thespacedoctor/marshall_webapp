from __future__ import print_function
from builtins import str
import os
import shutil
import unittest
import yaml
import shutil
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
from os.path import expanduser
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


class test_views_transients_followup_obs(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)
        self.testIni = moduleDirectory + "/../../../test.ini#marshall_webapp"
        self.testSettings = settings
        self.settings = settings

    def test_views_transients_followup_obs_post(self):
        self.config.add_route('transients_followup_obs',
                              '/transients/followup_obs')
        self.config.add_route(
            'transients_element_followup_obs', '/transients/{elementId}/followup_obs')

        from marshall_webapp.views import transients_followup_obs_view
        params = {
            "key": "value"
        }

        request = testing.DummyRequest(params=params)
        apply_request_extensions(
            request)

        resource = transients_followup_obs_view(
            request=request
        )
        response = resource.post()
        self.assertEqual(response.status_code, 302)

    def test_views_transients_followup_obs_function_exception(self):

        from marshall_webapp.views import transients_followup_obs_view
        try:
            this = transients_followup_obs_view(
                log=log,
                settings=settings,
                fakeKey="break the code"
            )
            this.get()
            assert False
        except Exception as e:
            assert True
            print(str(e))
