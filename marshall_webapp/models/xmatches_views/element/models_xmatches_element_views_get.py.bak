#!/usr/local/bin/python
# encoding: utf-8
"""
*The data model module for the `xmatches_element_views_get` resource*

:Author:
    David Young

:Date Created:
    October 13, 2015
"""
import sys
import os
import khufu
from marshall_webapp.models.transients.models_transients_get import models_transients_get


class models_xmatches_element_views_get(models_transients_get):
    """
    The worker class for the models_xmatches_element_views_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
        - ``search`` -- is this a search request (boolean)
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
        self.defaultQs = {}
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_xmatches_element_views_get' object")

        # Variable Data Atrributes

        # Initial Actions
        self._set_default_parameters()

        return None

    def get(self):
        """execute the get method on the models_xmatches_element_views_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')

        elementId = self.elementId

        responseContent = "Response from <code>" + __name__ + "</code><BR><BR>"
        if elementId:
            responseContent = "%(responseContent)sThe element selected was </code>%(elementId)s</code>" % locals(
            )
        else:
            responseContent = "%(responseContent)sResource Context selected (no element)" % locals(
            )

        self.log.debug('completed the ``get`` method')
        return responseContent

    def _set_default_parameters(
            self):
        """ set default parameters
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        for k, v in self.defaultQs.items():
            if k not in self.qs:
                self.qs[k] = v

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
