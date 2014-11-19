#!/usr/local/bin/python
# encoding: utf-8
"""
templates_transients_lightcurves.py
===================================
:Summary:
    The HTML template module for the `templates_transients_lightcurves.py` resource

:Author:
    David Young

:Date Created:
    November 5, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from ...models.transients_lightcurves import models_transients_lightcurves_get


class templates_transients_lightcurves():

    """
    The worker class for the templates_transients_lightcurves module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element requested (or False)

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        elementId=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'templates_transients_lightcurves' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the templates_transients_lightcurves object

        **Return:**
            - ``responseContent`` -- the response

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        templates_transients_lightcurves = None

        # grab the lightcurve data from the database
        transients_lightcurves = models_transients_lightcurves_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        responseContent = transients_lightcurves.get()

        self.log.info('completed the ``get`` method')
        return responseContent

    # xt-class-method
