#!/usr/local/bin/python
# encoding: utf-8
"""
templates_downloads.py
======================
:Summary:
    The HTML template module for the `templates_downloads.py` resource

:Author:
    David Young

:Date Created:
    November 13, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete review and cleanup this `templates_downloads.py` module
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from datetime import datetime, date, time
import khufu
from pyramid.response import FileResponse
from pyramid.path import AssetResolver


class templates_downloads():

    """
    The worker class for the templates_downloads module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element requested (or False)

    **Todo**
    """

    def __init__(
        self,
        log,
        request,
        elementId=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        self.defaultQs = {
            "filename": "download"
        }
        self.qs = dict(self.request.params)

        log.debug("instansiating a new 'templates_downloads' object")

        # Initial Actions
        self._set_default_parameters()

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the templates_downloads object

        **Return:**
            - ``responseContent`` -- the response

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        # build the absolute filepath for the resource
        myWebapp = AssetResolver(self.qs["webapp"])
        self.log.debug("""myWebapp: `%(myWebapp)s`""" % locals())
        url = self.request.params["url"]
        if url[0] == "/":
            url = url[1:]
        resourcePath = myWebapp.resolve(url)
        resourcePath = resourcePath.abspath()

        # start to build the response for the file
        response = FileResponse(
            resourcePath,
            request=self.request,
        )

        # change the filename of the file
        if "filename" in self.qs:
            now = datetime.now()
            now = now.strftime("%Y%m%dt%H%M%S")
            filename = self.qs["filename"].replace(" ", "_")
            filename = """%(filename)s_%(now)s""" % locals()
            response.content_disposition = "attachment; filename=%(filename)s" % locals(
            )

        self.log.info('completed the ``get`` method')
        return response

    def _set_default_parameters(
            self):
        """ set default parameters

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
        """
        self.log.info('starting the ``_set_default_parameters`` method')

        for k, v in self.defaultQs.iteritems():
            if k not in self.qs:
                self.qs[k] = v

        self.log.info('completed the ``_set_default_parameters`` method')
        return None

    # use the tab-trigger below for new method
    # xt-class-method
