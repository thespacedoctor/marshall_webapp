#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_transients_comments.py` resource*

:Author:
    David Young
"""
from builtins import object
import sys
import os
import khufu
from marshall_webapp.models.transients_comments import models_transients_comments_get
from marshall_webapp.models.transients_comments.element import models_transients_element_comments_get

class templates_transients_comments(object):
    """
    The worker class for the templates_transients_comments module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the element id of the resource requested (or false)
    
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
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'templates_transients_comments' object")

        return None

    def get(self):
        """get the templates_transients_comments object

        **Return**

        - ``responseContent`` -- the response
        
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
