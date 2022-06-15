#!/usr/bin/env python
# encoding: utf-8
"""
*The model get for the `models_transients_followup_obs_get.py` resource*

:Author:
    David Young

:Date Created:
    October 9, 2014
"""
################# GLOBAL IMPORTS ####################
import re
import urllib.error
import urllib.parse
import urllib.request
import collections
import khufu
import os
import sys
from builtins import object
from future import standard_library
standard_library.install_aliases()


class models_transients_followup_obs_get(object):

    """
    *The worker class for the models_transients_followup_obs_get module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)

    **Usage:**

    ```eval_rst
    .. todo::

        - add usage info
        - create a sublime snippet for usage
        - add a tutorial about ``models_transients_followup_obs_get`` to documentation
        - create a blog post about what ``models_transients_followup_obs_get`` does
    ```

    ```python
    usage code 
    ```  
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
        self.elementId = elementId
        self.search = search
        self.qs = dict(request.params)  # the query string
        # the query string defaults
        self.defaultQs = {
            "format": "json",
        }

        log.debug(
            "instansiating a new 'models_transients_followup_obs_get' object")

        # Initial Actions
        self._set_default_parameters()

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """
        *execute the get method on the models_transients_followup_obs_get object*

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')

        responseContent = {"elementId": self.elementId}

        self.log.debug('completed the ``get`` method')
        return responseContent

    def _set_default_parameters(
            self):
        """
        *set default parameters*

        **Key Arguments:**
            - 

        **Return:**
            - None
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        for k, v in list(self.defaultQs.items()):
            if k not in self.qs:
                self.qs[k] = v

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
