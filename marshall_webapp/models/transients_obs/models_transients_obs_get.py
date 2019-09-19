#!/usr/local/bin/python
# encoding: utf-8
"""
*The data model module for the `transients_obs_get` resource*

:Author:
    David Young

:Date Created:
    November 14, 2014
"""
import sys
import os
import khufu
from astrocalc.coords import unit_conversion


class models_transients_obs_get():
    """
    The worker class for the models_transients_obs_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
        - ``search`` -- is this a search query?
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
            "objectClass": "SN",
            "instrument": "efosc",
            "spectrumOrImage": "spectrum",
            "grism": 13,
            "badSeeing": False
        }
        self.log.debug(
            "instansiating a new 'models_transients_obs_get' object")

        self._set_default_parameters()
        self._get_transient_info()

        return None

    def close(self):
        del self
        return None

    def get(self):
        """execute the get method on the models_transients_obs_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')

        elementId = self.elementId
        transient_ob_data = self.qs

        self.log.debug('completed the ``get`` method')
        return transient_ob_data

    def _set_default_parameters(
            self):
        """ set default parameters

        **Key Arguments:**
            - 

        **Return:**
            - None

        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        for k, v in self.defaultQs.iteritems():
            if k not in self.qs:
                self.qs[k] = v

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    def _get_transient_info(
            self):
        """ get transient info
        """
        self.log.debug('starting the ``_get_transient_info`` method')

        elementId = self.elementId

        # query database for the info needed
        sqlQuery = u"""
            select raDeg, decDeg, masterName from transientBucketSummaries where transientBucketId = %(elementId)s 
        """ % locals()
        objectDataTmp = self.request.db.execute(sqlQuery).fetchall()
        objectData = []
        objectData[:] = [dict(zip(row.keys(), row)) for row in objectDataTmp]
        objectData = objectData[0]

        # ASTROCALC UNIT CONVERTER OBJECT
        converter = unit_conversion(
            log=self.log
        )
        self.qs["ra"] = converter.ra_sexegesimal_to_decimal(
            ra=objectData["raDeg"]
        )
        self.qs["dec"] = converter.dec_sexegesimal_to_decimal(
            dec=objectData["decDeg"]
        )

        self.qs["objectName"] = objectData["masterName"]

        self.log.debug('completed the ``_get_transient_info`` method')
        return None

    # use the tab-trigger below for new method
    # xt-class-method
