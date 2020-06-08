#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `models_transients_element_comments_put.py` resource*

:Author:
    David Young

:Date Created:
    September 18, 2014
"""
import sys
import os
import khufu


class models_transients_element_comments_put():
    """
    The worker class for the models_transients_element_comments_put module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
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

        log.debug(
            "instansiating a new 'models_transients_element_comments_put' object")

        return None

    def close(self):
        del self
        return None

    def put(self):
        """execute the put method on the models_transients_element_comments_put object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``put`` method')

        elementId = self.elementId

        responseContent = "Response from <code>" + __name__ + "</code><BR><BR>"
        if elementId:
            responseContent = "%(responseContent)sThe element selected was </code>%(elementId)s</code>" % locals(
            )
        else:
            responseContent = "%(responseContent)sResource Context selected (no element)" % locals(
            )

        self.log.debug('completed the ``put`` method')
        return responseContent

    # xt-class-method
