#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_element_obs_get.py
===================================
:Summary:
    The data model module for the `transients_element_obs_get` resource

:Author:
    David Young

:Date Created:
    November 14, 2014

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


class models_transients_element_obs_get():

    """
    The worker class for the models_transients_element_obs_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
        - ``search`` -- is this a search request (boolean)`

    **Todo**
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
            "instansiating a new 'models_transients_element_obs_get' object")

        # Initial Actions
        self._set_default_parameters()

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """execute the get method on the models_transients_element_obs_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        transientBucketId = self.elementId

        # grab the summary data for the transient
        sqlQuery = u"""
            select * from transientBucketSummaries where transientBucketId = %(transientBucketId)s 
        """ % locals()
        objectDataTmp = self.request.db.execute(sqlQuery).fetchall()
        objectData = []
        objectData[:] = [dict(zip(row.keys(), row)) for row in objectDataTmp]

        responseContent = "Response from <code>" + __name__ + "</code><BR><BR>"
        if transientBucketId:
            responseContent = "%(responseContent)sThe element selected was </code>%(transientBucketId)s</code>" % locals(
            )
        else:
            responseContent = "%(responseContent)sResource Context selected (no element)" % locals(
            )

        self.log.info('completed the ``get`` method')
        return objectData

    def _set_default_parameters(
            self):
        """ set default parameters

        **Key Arguments:**
            - 

        **Return:**
            - None

        **Todo**
        """
        self.log.info('starting the ``_set_default_parameters`` method')

        self.log.info('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
