#!/usr/local/bin/python
# encoding: utf-8
"""
*Template for the xmatches view*

:Author:
    David Young

:Date Created:
    October 12, 2015
"""
from builtins import object
import sys
import os
from marshall_webapp.models.xmatches import models_xmatches_get
from pyramid.path import AssetResolver
import khufu


class templates_xmatches(object):
    """
    The worker class for the templates_xmatches module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid/WebObs request object
        - ``elementId`` -- the specific element requested (or False)
        - ``search`` -- is this a search? (boolean)
    """

    def __init__(
        self,
        log,
        request,
        elementId=False,
        search=False
    ):
        self.log = log
        self.request = request
        log.debug("instansiating a new 'templates_xmatches' object")
        self.elementId = elementId
        self.search = search
        # xt-self-arg-tmpx

        return None

    def get(self):
        """get the templates_xmatches object

        **Return:**
            - ``webpage`` -- the webapge HTML
        """
        self.log.debug('starting the ``get`` method')

        from marshall_webapp.templates.commonelements.pagetemplates import defaultpagetemplate

        maincontent = ""

        webpage = defaultpagetemplate(
            log=self.log,
            request=self.request,
            bodyId=False,
            pageTitle="ePESSTO+ Marshall",
            topNavBar=False,
            sideBar="xmatches",
            mainContent=maincontent,
            relativePathFromDocRoot=False,
            thisPageName="xmatches"
        )

        self.log.debug('completed the ``get`` method')
        return webpage

    # xt-class-method
