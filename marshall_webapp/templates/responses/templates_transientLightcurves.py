#!/usr/local/bin/python
# encoding: utf-8
"""
templates_transientLightcurves.py
=================================
:Summary:
    The HTML template module for the `templates_transientLightcurves.py` resource

:Author:
    David Young

:Date Created:
    November 5, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete review and cleanup this `templates_transientLightcurves.py` module
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from ...models.transientLightcurves import models_transientLightcurves_get


class templates_transientLightcurves():

    """
    The worker class for the templates_transientLightcurves module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element requested (or False)

    **Todo**
        - @review: when complete, clean templates_transientLightcurves class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

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

        log.debug("instansiating a new 'templates_transientLightcurves' object")

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the templates_transientLightcurves object

        **Return:**
            - ``responseContent`` -- the response

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        templates_transientLightcurves = None

        transientLightcurves = models_transientLightcurves_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        responseContent = transientLightcurves.get()

        self.log.info('completed the ``get`` method')
        return responseContent
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
