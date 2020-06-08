#!/usr/bin/env python
# encoding: utf-8
"""
*The model get for the `models_stats_get.py` resource*

:Author:
    David Young

:Date Created:
    October 9, 2014
"""
################# GLOBAL IMPORTS ####################
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


class models_stats_get(object):

    """
    *The worker class for the models_stats_get module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)

    **Usage:**

    ```python
    usage code 
    ```

    ---

    ```eval_rst
    .. todo::

        - add usage info
        - create a sublime snippet for usage
        - add a tutorial about ``models_stats_get`` to documentation
        - create a blog post about what ``models_stats_get`` does
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
            "instansiating a new 'models_stats_get' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """
        *execute the get method on the models_stats_get object*

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')

        responseContent = self.elementId

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

        if "format" not in self.qs:
            self.qs["format"] = self.defaultQs["format"]

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
