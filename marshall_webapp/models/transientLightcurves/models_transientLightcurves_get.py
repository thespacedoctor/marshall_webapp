#!/usr/local/bin/python
# encoding: utf-8
"""
models_transientLightcurves_get.py
==================================
:Summary:
    The data model module for the `transientLightcurves_get` resource

:Author:
    David Young

:Date Created:
    November 5, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete review and cleanup this models_transientLightcurves_get.py module
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu


class models_transientLightcurves_get():

    """
    The worker class for the models_transientLightcurves_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)

    **Todo**
        - @review: when complete, clean models_transientLightcurves_get class
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
            "format": "json",
        }
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_transientLightcurves_get' object")

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions
        self._set_default_parameters()

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """execute the get method on the models_transientLightcurves_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        elementId = self.elementId

        # GRAB THE LIGHTCURVE DATA FOR THE OBJECT
        sqlQuery = """
            select observationDate, observationMJD, magnitude, filter, survey from transientBucket where transientBucketId = %(elementId)s and observationDate is not null and observationDate != 0000-00-00 and magnitude is not null and magnitude < 50 order by observationDate asc;
        """ % locals()

        lightCurveTmp = self.request.db.execute(sqlQuery).fetchall()
        lightCurve = []
        lightCurve[:] = [dict(zip(row.keys(), row)) for row in lightCurveTmp]

        self.log.info('completed the ``get`` method')
        return lightCurve

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

        if "format" not in self.qs:
            self.qs["format"] = self.defaultQs["format"]

        self.log.info('completed the ``_set_default_parameters`` method')
        return None

    # use the tab-trigger below for new method
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
