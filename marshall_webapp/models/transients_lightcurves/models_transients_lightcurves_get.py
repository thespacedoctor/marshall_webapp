#!/usr/local/bin/python
# encoding: utf-8
"""
*The data model module for the `transients_lightcurves_get` resource*

:Author:
    David Young

:Date Created:
    November 5, 2014
"""
from builtins import zip
from builtins import object
import sys
import os
import khufu
import collections


class models_transients_lightcurves_get(object):
    """
    The worker class for the models_transients_lightcurves_get module

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
        self.defaultQs = {
            "format": "json",
        }
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_transients_lightcurves_get' object")

        self._set_default_parameters()

        return None

    def close(self):
        del self
        return None

    def get(self):
        """execute the get method on the models_transients_lightcurves_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
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
            for key in list(row.keys()):
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
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        if "format" not in self.qs:
            self.qs["format"] = self.defaultQs["format"]

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    def get_metadata(
            self):
        """Get some extra transient metadata
        """
        self.log.debug('starting the ``get_metadata`` method')

        transientBucketId = self.elementId

        sqlQuery = u"""
            select * from transientBucketSummaries where transientBucketId = %(transientBucketId)s
        """ % locals()
        extraMetadataTmp = self.request.db.execute(sqlQuery).fetchall()
        extraMetadata = []
        extraMetadata[:] = [dict(list(zip(list(row.keys()), row)))
                            for row in extraMetadataTmp]

        self.log.debug('completed the ``get_metadata`` method')
        return extraMetadata

    # xt-class-method
