#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_transients_context.py` resource*

:Author:
    David Young

:Date Created:
    October 9, 2014
"""
from builtins import object
import sys
import os
import khufu
from marshall_webapp.models.transients_context import models_transients_context_get
from marshall_webapp.models.transients_context.element import models_transients_element_context_get


class templates_transients_context(object):
    """
    The worker class for the templates_transients_context module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the element id of the resource requested (or false)
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
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'templates_transients_context' object")

        return None

    def get(self):
        """get the templates_transients_context object

        **Return:**
            - ``responseContent`` -- the response
        """
        self.log.debug('starting the ``get`` method')

        from marshall_webapp.templates.commonelements.pagetemplates import defaultpagetemplate

        # GRAB THE COMMENTS FROM THE DATABASE
        transients_context = models_transients_context_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )

        context = transients_context.get()

        self.log.debug('completed the ``get`` method')
        return context
    # xt-class-method
