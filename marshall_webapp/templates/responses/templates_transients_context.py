#!/usr/local/bin/python
# encoding: utf-8
"""
templates_transients_context.py
==============================
:Summary:
    The HTML template module for the `templates_transients_context.py` resource

:Author:
    David Young

:Date Created:
    October 9, 2014

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
from ...models.transients_context import models_transients_context_get
from ...models.transients_context.element import models_transients_element_context_get


class templates_transients_context():

    """
    The worker class for the templates_transients_context module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the element id of the resource requested (or false)

    **Todo**
    """
    # Initialisation

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
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'templates_transients_context' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the templates_transients_context object

        **Return:**
            - ``responseContent`` -- the response

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        from ..commonelements.pagetemplates import defaultpagetemplate

        # grab the comments from the database
        transients_context = models_transients_context_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        context = transients_context.get()

        self.log.info('completed the ``get`` method')
        return context
    # xt-class-method
