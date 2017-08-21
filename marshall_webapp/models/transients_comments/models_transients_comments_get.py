#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_comments_get.py
===============================
:Summary:
    The HTML template module for the `models_transients_comments_get.py` resource

:Author:
    David Young

:Date Created:
    October 9, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu


class models_transients_comments_get():

    """
    The worker class for the models_transients_comments_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)

    **Todo**
    """
    # Initialisation

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

        log.debug("instansiating a new 'models_transients_comments_get' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """execute the get method on the models_transients_comments_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser

        **Todo**
        """
        self.log.info('starting the ``get`` method')
        elementId = self.elementId

        responseContent = "Response from <code>" + __name__ + "</code><BR><BR>"
        if elementId:
            responseContent = "%(responseContent)sThe element selected was </code>%(elementId)s</code>" % locals(
            )
        else:
            responseContent = "%(responseContent)sResource Context selected (no element)" % locals(
            )

        self.log.info('completed the ``get`` method')
        return responseContent

    # xt-class-method
