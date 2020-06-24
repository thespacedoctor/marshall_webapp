#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_transients_history.py` resource*

:Author:
    David Young
"""
from builtins import object
import sys
import os
import khufu
from marshall_webapp.models.transients_history.element import models_transients_element_history_get

class templates_transients_history(object):
    """
    The worker class for the templates_transients_history module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element requested (or False)
    
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

        log.debug("instansiating a new 'templates_transients_history' object")

        return None

    def get(self):
        """get the templates_transients_history object

        **Return**

        - ``responseContent`` -- the response
        
        """
        self.log.debug('starting the ``get`` method')

        templates_transients_history = None

        transients_history = models_transients_element_history_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        responseContent = transients_history.get()

        self.log.debug('completed the ``get`` method')
        return responseContent

    # method-override-tmpx
