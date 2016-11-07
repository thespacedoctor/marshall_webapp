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
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

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

        log.debug(
            "instansiating a new 'models_transients_element_post' object")

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
            select p.classifiedFlag, t.raDeg, t.decDeg, t.name, t.htm20ID, t.htm16ID, t.cx, t.cy, t.cz from transientBucket t, pesstoObjects p where replacedByRowId = 0 and t.transientBucketId = %(transientBucketId)s and t.cx is not null and t.transientBucketId=p.transientBucketId limit 1
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
        if "clsClassificationPhase" not in locals() or len(clsClassificationPhase) == 0:
            clsClassificationPhase = "null"

        username = self.request.authenticated_userid

        # insert the new classification row into the transientBucket
        duplicate = False
        try:
            sqlQuery = """
                INSERT IGNORE INTO transientBucket (raDeg, decDeg, name, htm16ID, cx, cy, cz, transientBucketId, observationDate, observationMjd, survey, spectralType, transientRedshift, dateCreated, dateLastModified, classificationWRTMax, classificationPhase, reducer) VALUES(%(raDeg)s, %(decDeg)s, "%(name)s", %(htm16ID)s, %(cx)s, %(cy)s, %(cz)s, %(transientBucketId)s, "%(clsObsdate)s", %(obsMjd)s, "%(clsSource)s", "%(clsType)s", %(clsRedshift)s, "%(now)s", "%(now)s", "%(clsClassificationWRTMax)s", %(clsClassificationPhase)s, "%(username)s");
            """ % locals()
            self.log.debug('sqlQuery: %(sqlQuery)s' % locals())
            self.request.db.execute(sqlQuery)
            self.request.db.commit()
        except:
            duplicate = True

        if duplicate == True:
            sqlQuery = """
                select primaryKeyId from transientBucket where decDeg= %(decDeg)s and name="%(name)s" and observationMjd=%(obsMjd)s and survey="%(clsSource)s" and replacedByRowId = 0;
            """  % locals()
            objectDataTmp = self.request.db.execute(sqlQuery).fetchall()
            objectData = []
            objectData[:] = [dict(zip(row.keys(), row))
                             for row in objectDataTmp]
            primaryKeyId = objectData[0]["primaryKeyId"]

            sqlQuery = """
                INSERT IGNORE INTO transientBucket (raDeg, decDeg, name, htm16ID, cx, cy, cz, transientBucketId, observationDate, observationMjd, survey, spectralType, transientRedshift, dateCreated, dateLastModified, classificationWRTMax, classificationPhase, reducer, replacedByRowId) VALUES(%(raDeg)s, %(decDeg)s, "%(name)s", %(htm16ID)s, %(cx)s, %(cy)s, %(cz)s, %(transientBucketId)s, "%(clsObsdate)s", %(obsMjd)s, "%(clsSource)s", "%(clsType)s", %(clsRedshift)s, "%(now)s", "%(now)s", "%(clsClassificationWRTMax)s", %(clsClassificationPhase)s, "%(username)s", %(primaryKeyId)s);
                update transientBucket t, (SELECT primaryKeyId FROM transientBucket where replacedByRowId = %(primaryKeyId)s) as o set t.replacedByRowId = o.primaryKeyId where t.primaryKeyId = %(primaryKeyId)s;
                update transientBucket set replacedByRowId = 0 where replacedByRowId = %(primaryKeyId)s;
            """ % locals()
            self.log.debug('sqlQuery: %(sqlQuery)s' % locals())
            self.request.db.execute(sqlQuery)
            self.request.db.commit()

        # UPDATE THE OBJECT'S LOCATION IN THE VARIOUS MARSHALL WORKFLOWS
        if self.request.params["clsSendTo"].lower() == "yes":
            awl = "queued for atel"
        else:
            awl = "archived without alert"

        if classifiedFlag == 1:
            sqlQuery = """
                update pesstoObjects set snoozed = 0, alertWorkflowLocation = "%(awl)s" where transientBucketId = %(transientBucketId)s
            """ % locals()
        else:
            sqlQuery = """
                update pesstoObjects set classifiedFlag = 1, snoozed = 0, marshallWorkflowLocation = "review for followup", alertWorkflowLocation = "%(awl)s" where transientBucketId = %(transientBucketId)s
            """ % locals()
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

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
