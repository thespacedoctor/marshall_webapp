#!/usr/local/bin/python
# encoding: utf-8
"""
*The data model module for the `transients_lightcurves_count` resource*

:Author:
    David Young

:Date Created:
    November 5, 2014
"""
import sys
import os
import khufu


class models_transients_lightcurves_count():
    """
    The worker class for the models_transients_lightcurves_count module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
        - ``search`` -- if this a search request (boolean)
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
            "instansiating a new 'models_transients_lightcurves_count' object")

        return None

    def close(self):
        del self
        return None

    def count(self):
        """execute the count method on the models_transients_lightcurves_count object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``count`` method')

        elementId = self.elementId

        responseContent = "Response from <code>" + __name__ + "</code><BR><BR>"
        if elementId:
            responseContent = "%(responseContent)sThe element selected was </code>%(elementId)s</code>" % locals(
            )
        else:
            responseContent = "%(responseContent)sResource Context selected (no element)" % locals(
            )

        self.log.debug('completed the ``count`` method')
        return responseContent

    # xt-class-method
