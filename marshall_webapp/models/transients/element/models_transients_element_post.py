#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_element_post.py
=================================
:Summary:
    The HTML template module for the `models_transients_element_post.py` resource

:Author:
    David Young

:Date Created:
    October 10, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from dryxPython import commonutils as dcu
from dryxPython import astrotools as dat
from pessto_marshall_engine.database.housekeeping.flags.update_transientbucketsummaries_flags import update_transientbucketsummaries_flags


class models_transients_element_post():

    """
    The worker class for the models_transients_element_post module

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
        request
    ):
        self.log = log
        self.request = request
        self.transientBucketId = request.matchdict["elementId"]
        self.response = ""
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'models_transients_element_post' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def post(self):
        """execute the post method on the models_transients_element_post object

        **Return:**
            - ``response`` -- the reponse to send to the browser

        **Todo**
        """
        self.log.info('starting the ``post`` method')

        # check the right keywords are passed in the query string
        if set(("clsObsdate", "clsSource")) <= set(self.request.params):
            self._add_transient_classification()

        # if the right keywords are not passed throw a warning
        if len(self.response) == 0:
            self.response = "no action was performed"

        self.log.info('completed the ``post`` method')
        return self.response

    def _add_transient_classification(
            self):
        """ add transient classification

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
        """
        self.log.info('starting the ``_add_transient_classification`` method')

        now = dcu.get_now_sql_datetime()
        transientBucketId = self.transientBucketId

        # first select out a row from the transientBucket as a template for the
        # classification
        sqlQuery = """
            select raDeg, decDeg, name, htm20ID, htm16ID, cx, cy, cz from transientBucket where transientBucketId = %(transientBucketId)s and cx is not null limit 1
        """ % locals()
        rowsTmp = self.request.db.execute(sqlQuery).fetchall()
        rows = []
        rows[:] = [dict(zip(row.keys(), row)) for row in rowsTmp]

        # add variables to locals()
        for row in rows:
            for arg, val in row.iteritems():
                varname = arg
                if isinstance(val, str) or isinstance(val, unicode):
                    exec(varname + """ = '%s' """ % (val,))
                else:
                    exec(varname + """ = %s """ % (val,))
        for arg, val in self.request.params.iteritems():
            varname = arg
            if isinstance(val, str) or isinstance(val, unicode):
                exec(varname + ' = """%s""" ' % (val,))
            else:
                exec(varname + " = %s" % (val,))

        # convert date to mjd
        obsMjd = dat.getMJDFromSqlDate(
            # "%Y-%m-%dT%H:%M:%S.%f"
            sqlDate="%(clsObsdate)sT00:00:00.0" % locals()
        )

        # add some default values / null values
        if "clsPeculiar" in locals():
            clsSnClassification = "%(clsSnClassification)s-p" % locals()
        if clsType == "supernova":
            clsType = clsSnClassification
        if "clsRedshift" not in locals() or len(clsRedshift) == 0:
            clsRedshift = "null"
        if "clsClassificationWRTMax" not in locals():
            clsClassificationWRTMax = "unknown"
        if "clsClassificationPhase" not in locals():
            clsClassificationPhase = "null"

        # insert the new classification row into the transientBucket
        sqlQuery = """
            INSERT INTO transientBucket (raDeg, decDeg, name, htm20ID, htm16ID, cx, cy, cz, transientBucketId, observationDate, observationMjd, survey, spectralType, transientRedshift, dateCreated, dateLastModified, classificationWRTMax, classificationPhase) VALUES(%(raDeg)s, %(decDeg)s, "%(name)s", %(htm20ID)s, %(htm16ID)s, %(cx)s, %(cy)s, %(cz)s, %(transientBucketId)s, "%(clsObsdate)s", %(obsMjd)s, "%(clsSource)s", "%(clsType)s", %(clsRedshift)s, "%(now)s", "%(now)s", "%(clsClassificationWRTMax)s", %(clsClassificationPhase)s);
        """ % locals()
        self.log.debug('sqlQuery: %(sqlQuery)s' % locals())
        self.request.db.execute(sqlQuery)

        # UPDATE THE OBJECT'S LOCATION IN THE VARIOUS MARSHALL WORKFLOWS
        if self.request.params["clsSendTo"].lower() == "yes":
            awl = "queued for atel"
        else:
            awl = "archived without alert"
        sqlQuery = """
            update pesstoObjects set classifiedFlag = 1, marshallWorkflowLocation = "review for followup", alertWorkflowLocation = "%(awl)s" where transientBucketId = %(transientBucketId)s
        """ % locals()
        self.request.db.execute(sqlQuery)

        # update_transientbucketsummaries_flags
        update_transientbucketsummaries_flags(
            log=self.log,
            dbConn=self.request.registry.settings["dbConn"],
            updateAll=False,
            transientBucketId=transientBucketId
        )

        self.response = self.response + \
            "Add a classification to transient #%(transientBucketId)s " % locals(
            )

        self.log.info('completed the ``_add_transient_classification`` method')
        return None

    # xt-class-method
