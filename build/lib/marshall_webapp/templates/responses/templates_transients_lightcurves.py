#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_transients_lightcurves.py` resource*

:Author:
    David Young
"""
from builtins import object
import sys
import os
import khufu
from marshall_webapp.models.transients_lightcurves import models_transients_lightcurves_get

class templates_transients_lightcurves(object):
    """
    The worker class for the templates_transients_lightcurves module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element requested (or False)
    - ``format`` -- format
    
    """

    def __init__(
        self,
        log,
        request,
        elementId=False,
        format=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        self.format = format
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'templates_transients_lightcurves' object")

        return None

    def get(self):
        """get the templates_transients_lightcurves object

        **Return**

        - ``responseContent`` -- the response
        
        """
        self.log.debug('starting the ``get`` method')

        templates_transients_lightcurves = None

        # GRAB THE LIGHTCURVE DATA FROM THE DATABASE
        transients_lightcurves = models_transients_lightcurves_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        responseContent = transients_lightcurves.get()
        metadata = transients_lightcurves.get_metadata()
        metadata = metadata[0]

        chartAttributes = {}
        chartAttributes["title"] = metadata["masterName"]
        chartAttributes["x1title"] = "MJD"
        chartAttributes["x2title"] = "Date"
        chartAttributes["y1title"] = "Apparent Magnitude"

        if self.format:
            responseContent = {
                u"chartAttributes": chartAttributes, u"chartData": responseContent}

        self.log.debug('completed the ``get`` method')
        return responseContent

    # xt-class-method
