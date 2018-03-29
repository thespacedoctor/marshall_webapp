#!/usr/local/bin/python
# encoding: utf-8
"""
templates_xmatches.py
=======================
:Summary:
    Template for the xmatches view

:Author:
    David Young

:Date Created:
    October 12, 2015

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import yaml
from ...models.xmatches import models_xmatches_get
from pyramid.path import AssetResolver
import khufu


class templates_xmatches():

    """
    The worker class for the templates_xmatches module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid/WebObs request object
        - ``elementId`` -- the specific element requested (or False)
        - ``search`` -- is this a search? (boolean)
    """
    # Initialisation

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

    # Method Attributes
    def get(self):
        """get the templates_xmatches object

        **Return:**
            - ``webpage`` -- the webapge HTML
        """
        self.log.debug('starting the ``get`` method')

        from ..commonelements.pagetemplates import defaultpagetemplate

        maincontent = ""

        webpage = defaultpagetemplate(
            log=self.log,
            request=self.request,
            bodyId=False,
            pageTitle="PESSTO Marshall",
            topNavBar=False,
            sideBar="xmatches",
            mainContent=maincontent,
            relativePathFromDocRoot=False,
            thisPageName="xmatches"
        )

        self.log.debug('completed the ``get`` method')
        return webpage

    # use the tab-trigger below for new method
    # xt-class-method
