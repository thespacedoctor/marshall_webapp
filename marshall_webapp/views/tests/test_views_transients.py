import os
import nose
import shutil
from .. import views_transients
from dryxPython.utKit import utKit
from pyramid import testing

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


class test_app():

    def test_views_transients_get(self):
        request = testing.DummyRequest()
        transients_view_object = views_transients.transients_view(request)
        response = transients_view_object.get_html()
        nose.tools.assert_equal(response.status_code, 200)
        nose.tools.assert_in("Hello", response.body)
