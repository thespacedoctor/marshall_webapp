#!/usr/local/bin/python
# encoding: utf-8
"""
templates_transients_comments.py
==============================
:Summary:
    The HTML template module for the `templates_transients_comments.py` resource

:Author:
    David Young

:Date Created:
    October 9, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from marshall_webapp.models.transients_comments import models_transients_comments_get
from marshall_webapp.models.transients_comments.element import models_transients_element_comments_get


class templates_transients_comments():

    """
    The worker class for the templates_transients_comments module

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
        elementId=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'templates_transients_comments' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the templates_transients_comments object

        **Return:**
            - ``responseContent`` -- the response

        **Todo**
        """
        self.log.debug('starting the ``get`` method')

        templates_transients_comments = None

        # grab the comments from the database
        transients_comments = models_transients_comments_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        responseContent = transients_comments.get()

        self.log.debug('completed the ``get`` method')
        return responseContent
    # xt-class-method
