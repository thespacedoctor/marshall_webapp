#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_lightcurves_get.py
==================================
:Summary:
    The data model module for the `transients_lightcurves_get` resource

:Author:
    David Young

:Date Created:
    November 5, 2014

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
import collections


class models_transients_lightcurves_get():

    """
    The worker class for the models_transients_lightcurves_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
        - ``search`` -- is this a search request (boolean)

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
        self.defaultQs = {
            "format": "json",
        }
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_transients_lightcurves_get' object")

        # Initial Actions
        self._set_default_parameters()

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """execute the get method on the models_transients_lightcurves_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser

        **Todo**
        """
        self.log.debug('starting the ``get`` method')

        transientBucketId = self.elementId

        # GRAB THE LIGHTCURVE DATA FOR THE OBJECT
        sqlQuery = """
            select observationMJD, observationDate, magnitude, magnitudeError, limitingMag, filter, survey from transientBucket where replacedByRowId = 0 and transientBucketId = %(transientBucketId)s and observationDate is not null and observationDate != 0000-00-00 and magnitude is not null and magnitude < 50 and survey != "bright sn list" order by observationDate asc;
        """ % locals()
        lightCurveTmp = self.request.db.execute(sqlQuery).fetchall()
        odict = collections.OrderedDict(sorted({}.items()))
        lightCurve = []

        for row in lightCurveTmp:
            odict = collections.OrderedDict(sorted({}.items()))
            for key in row.keys():
                if row[key] == None:
                    value = "-"
                else:
                    value = row[key]
                odict[key] = value
            lightCurve.append(odict)

        self.log.debug('completed the ``get`` method')
        return lightCurve

    def _set_default_parameters(
            self):
        """ set default parameters

        **Key Arguments:**
            - 

        **Return:**
            - None

        **Todo**
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        if "format" not in self.qs:
            self.qs["format"] = self.defaultQs["format"]

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # use the tab-trigger below for new method
    def get_metadata(
            self):
        """ extra metadata

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean get_metadata method
            - @review: when complete add logging
        """
        self.log.debug('starting the ``get_metadata`` method')

        transientBucketId = self.elementId

        sqlQuery = u"""
            select * from transientBucketSummaries where transientBucketId = %(transientBucketId)s
        """ % locals()
        extraMetadataTmp = self.request.db.execute(sqlQuery).fetchall()
        extraMetadata = []
        extraMetadata[:] = [dict(zip(row.keys(), row))
                            for row in extraMetadataTmp]

        self.log.debug('completed the ``get_metadata`` method')
        return extraMetadata

    # use the tab-trigger below for new method
    # xt-class-method
