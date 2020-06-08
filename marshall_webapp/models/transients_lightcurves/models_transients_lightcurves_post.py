#!/usr/local/bin/python
# encoding: utf-8
"""
*The data model module for the `transients_lightcurves_post` resource*

:Author:
    David Young

:Date Created:
    November 5, 2014
"""
from builtins import object
import sys
import os
import khufu


class models_transients_lightcurves_post(object):
    """
    The worker class for the models_transients_lightcurves_post module

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
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_transients_lightcurves_post' object")

        return None

    def close(self):
        del self
        return None

    def post(self):
        """execute the post method on the models_transients_lightcurves_post object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``post`` method')

        elementId = self.elementId

        responseContent = "Response from <code>" + __name__ + "</code><BR><BR>"
        if elementId:
            responseContent = "%(responseContent)sThe element selected was </code>%(elementId)s</code>" % locals(
            )
        else:
            responseContent = "%(responseContent)sResource Context selected (no element)" % locals(
            )

        self.log.debug('completed the ``post`` method')
        return responseContent

    # xt-class-method
