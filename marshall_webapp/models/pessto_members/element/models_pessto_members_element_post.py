#!/usr/local/bin/python
# encoding: utf-8
"""
models_pessto_members_element_post.py
=================================================================
:Summary:
    The data model module for the `pessto_members_element_post` resource

:Author:
    David Young

:Date Created:
    January 21, 2016

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu


class models_pessto_members_element_post():
    """
    The worker class for the models_pessto_members_element_post module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
        - ``search`` -- is this a search request (boolean)
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
        self.defaultQs = {}
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_pessto_members_element_post' object")

        # Variable Data Atrributes

        # Initial Actions
        self._set_default_parameters()

        return None

    # Method Attributes
    def post(self):
        """execute the post method on the models_pessto_members_element_post object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.info('starting the ``post`` method')

        elementId = self.elementId

        responseContent = "Response from <code>" + __name__ + "</code><BR><BR>"
        if elementId:
            responseContent = "%(responseContent)sThe element selected was </code>%(elementId)s</code>" % locals(
            )
        else:
            responseContent = "%(responseContent)sResource Context selected (no element)" % locals(
            )

        self.log.info('completed the ``post`` method')
        return responseContent

    def _set_default_parameters(
            self):
        """ set default parameters

        **Key Arguments:**
            - 

        **Return:**
            - None
        """
        self.log.info('starting the ``_set_default_parameters`` method')

        for k, v in self.defaultQs.iteritems():
            if k not in self.qs:
                self.qs[k] = v

        self.log.info('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
