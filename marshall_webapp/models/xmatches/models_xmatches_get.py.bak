#!/usr/local/bin/python
# encoding: utf-8
"""
*The model get for the `models_xmatches_get.py` resource*

:Author:
    David Young

:Date Created:
    October 9, 2014
"""
import sys
import os
import khufu
import collections
import urllib
import re


class models_xmatches_get():
    """
    The worker class for the models_xmatches_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
    """

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
            "instansiating a new 'models_xmatches_get' object")

        return None

    def close(self):
        del self
        return None

    def get(self):
        """execute the get method on the models_xmatches_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')

        responseContent = self.elementId

        self.log.debug('completed the ``get`` method')
        return responseContent

    def _set_default_parameters(
            self):
        """ set default parameters
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        if "format" not in self.qs:
            self.qs["format"] = self.defaultQs["format"]

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
