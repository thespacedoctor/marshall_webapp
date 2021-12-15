#!/usr/local/bin/python
# encoding: utf-8
"""
*The model get for the `models_xmatches_get.py` resource*

:Author:
    David Young
"""
from future import standard_library
standard_library.install_aliases()
from builtins import object
import sys
import os
import khufu
import collections
import urllib.request
import urllib.parse
import urllib.error
import re
from dryxPyramid.models.models_base import base_model

class models_xmatches_get(base_model):
    """
    The worker class for the models_xmatches_get module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element id requests (or False)
    
    """

    def __init__(self, log, request, elementId=False, search=False):
        super().__init__(log, request, elementId, search)
        self.resourceName = "xmatches"
        self._set_default_parameters()

        log.debug(
            "instansiating a new 'models_xmatches_get' object")
        return None

    def get(self):
        """execute the get method on the models_xmatches_get object

        **Return**

        - ``responseContent`` -- the reponse to send to the browser
        
        """
        self.log.debug('starting the ``get`` method')

        responseContent = self.elementId

        self.log.debug('completed the ``get`` method')
        return responseContent

    # xt-class-method
