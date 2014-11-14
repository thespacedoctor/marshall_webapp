#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_ob_get.py
===========================
:Summary:
    The data model module for the `transients_ob_get` resource

:Author:
    David Young

:Date Created:
    November 14, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete review and cleanup this models_transients_ob_get.py module
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from dryxPython import astrotools as dat


class models_transients_ob_get():

    """
    The worker class for the models_transients_ob_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)

    **Todo**
        - @review: when complete, clean models_transients_ob_get class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

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
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'models_transients_ob_get' object")

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions
        self._set_default_parameters()
        self._get_transient_info()

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """execute the get method on the models_transients_ob_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        elementId = self.elementId
        transient_ob_data = self.qs

        self.log.info('completed the ``get`` method')
        return transient_ob_data

    def _set_default_parameters(
            self):
        """ set default parameters

        **Key Arguments:**
            - 

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _set_default_parameters method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_set_default_parameters`` method')

        for k, v in self.defaultQs.iteritems():
            if k not in self.qs:
                self.qs[k] = v

        self.log.info('completed the ``_set_default_parameters`` method')
        return None

    def _get_transient_info(
            self):
        """ get transient info

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_transient_info method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_get_transient_info`` method')

        elementId = self.elementId

        sqlQuery = u"""
            select * from transientBucketSummaries where transientBucketId = %(elementId)s 
        """ % locals()
        objectDataTmp = self.request.db.execute(sqlQuery).fetchall()
        objectData = []
        objectData[:] = [dict(zip(row.keys(), row)) for row in objectDataTmp]
        objectData = objectData[0]

        self.qs["ra"] = dat.ra_to_sex(
            ra=objectData["raDeg"],
            delimiter=':'
        )

        self.qs["dec"] = dat.dec_to_sex(
            dec=objectData["decDeg"],
            delimiter=':'
        )

        self.qs["objectName"] = objectData["masterName"]

        self.log.info('completed the ``_get_transient_info`` method')
        return None

    # use the tab-trigger below for new method
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
