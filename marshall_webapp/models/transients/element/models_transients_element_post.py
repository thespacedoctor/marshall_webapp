#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `models_transients_element_post.py` resource*

:Author:
    David Young
"""
from builtins import zip
from builtins import object
import sys
import os
import khufu
from marshallEngine.housekeeping import update_transient_summaries
from astrocalc.times import conversions
from fundamentals import times
from fundamentals.logs import emptyLogger


class models_transients_element_post(object):
    """
    The worker class for the models_transients_element_post module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element id requests (or False)
    """

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

        return None

    def close(self):
        del self
        return None

    def post(self):
        """execute the post method on the models_transients_element_post object

        **Return**

        - ``response`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``post`` method')

        # CHECK THE RIGHT KEYWORDS ARE PASSED IN THE QUERY STRING
        if set(("clsObsdate", "clsSource")) <= set(self.request.params):
            self._add_transient_classification()

        # IF THE RIGHT KEYWORDS ARE NOT PASSED THROW A WARNING
        if len(self.response) == 0:
            self.response = "no action was performed"

        self.log.debug('completed the ``post`` method')
        return self.response

    def _add_transient_classification(
            self):
        """ add transient classification
        """
        self.log.debug('starting the ``_add_transient_classification`` method')

        transientBucketId = self.transientBucketId

        # ASTROCALC CONVERTER
        converter = conversions(
            log=self.log
        )

        # FIRST SELECT OUT A ROW FROM THE TRANSIENTBUCKET AS A TEMPLATE FOR THE
        # CLASSIFICATION
        sqlQuery = """
            select p.classifiedFlag, t.raDeg, t.decDeg, t.name from transientBucket t, pesstoObjects p where replacedByRowId = 0 and t.transientBucketId = %(transientBucketId)s and t.transientBucketId=p.transientBucketId limit 1
        """ % locals()

        rowsTmp = self.request.db.execute(sqlQuery).fetchall()
        rows = []
        rows[:] = [dict(list(zip(list(row.keys()), row))) for row in rowsTmp]

        # ADD VARIABLES TO a
        params = dict(list(self.request.params.items()))
        params["now"] = times.get_now_sql_datetime()
        params["transientBucketId"] = self.transientBucketId
        for row in rows:
            params["raDeg"] = row["raDeg"]
            params["decDeg"] = row["decDeg"]
            params["name"] = row["name"]
            params["classifiedFlag"] = row["classifiedFlag"]

        # CONVERT DATE TO MJD
        params["obsMjd"] = converter.ut_datetime_to_mjd(
            utDatetime="%(clsObsdate)sT00:00:00.0" % params)

        # ADD SOME DEFAULT VALUES / NULL VALUES
        if "clsPeculiar" in params:
            params[
                "clsSnClassification"] = "%(clsSnClassification)s-p" % params
        if params["clsType"] == "supernova":
            params["clsType"] = params["clsSnClassification"]
        if "clsRedshift" not in params or len(params["clsRedshift"]) == 0:
            params["clsRedshift"] = "null"
        if "clsClassificationWRTMax" not in params:
            params["clsClassificationWRTMax"] = "unknown"
        if "clsClassificationPhase" not in params or len(params["clsClassificationPhase"]) == 0:
            params["clsClassificationPhase"] = "null"

        params["username"] = self.request.authenticated_userid

        # INSERT THE NEW CLASSIFICATION ROW INTO THE TRANSIENTBUCKET

        try:
            duplicate = False
            sqlQuery = """
                    INSERT INTO transientBucket (raDeg, decDeg, name, transientBucketId, observationDate, observationMjd, survey, spectralType, transientRedshift, dateCreated, dateLastModified, classificationWRTMax, classificationPhase, reducer) VALUES(%(raDeg)s, %(decDeg)s, "%(name)s", %(transientBucketId)s, "%(clsObsdate)s", %(obsMjd)s, "%(clsSource)s", "%(clsType)s", %(clsRedshift)s, "%(now)s", "%(now)s", "%(clsClassificationWRTMax)s", %(clsClassificationPhase)s, "%(username)s");
                """ % params

            self.request.db.execute(sqlQuery)
            self.request.db.commit()
        except:
            duplicate = True

        if duplicate == True:
            sqlQuery = """
                select primaryKeyId from transientBucket where decDeg= %(decDeg)s and name="%(name)s" and observationMjd=%(obsMjd)s and survey="%(clsSource)s" and replacedByRowId = 0;
            """  % params

            objectDataTmp = self.request.db.execute(sqlQuery).fetchall()
            objectData = []
            objectData[:] = [dict(list(zip(list(row.keys()), row)))
                             for row in objectDataTmp]
            primaryKeyId = objectData[0]["primaryKeyId"]
            params["primaryKeyId"] = primaryKeyId

            sqlQuery = """
                INSERT IGNORE INTO transientBucket (raDeg, decDeg, name, transientBucketId, observationDate, observationMjd, survey, spectralType, transientRedshift, dateCreated, dateLastModified, classificationWRTMax, classificationPhase, reducer, replacedByRowId) VALUES(%(raDeg)s, %(decDeg)s, "%(name)s", %(transientBucketId)s, "%(clsObsdate)s", %(obsMjd)s, "%(clsSource)s", "%(clsType)s", %(clsRedshift)s, "%(now)s", "%(now)s", "%(clsClassificationWRTMax)s", %(clsClassificationPhase)s, "%(username)s", %(primaryKeyId)s);
            """ % params
            self.log.debug('sqlQuery: %(sqlQuery)s' % locals())
            self.request.db.execute(sqlQuery)
            self.request.db.commit()

            sqlQuery = """
                update transientBucket t, (SELECT primaryKeyId FROM transientBucket where replacedByRowId = %(primaryKeyId)s) as o set t.replacedByRowId = o.primaryKeyId where t.primaryKeyId = %(primaryKeyId)s;
            """ % locals()
            self.log.debug('sqlQuery: %(sqlQuery)s' % locals())
            self.request.db.execute(sqlQuery)
            self.request.db.commit()

            sqlQuery = """
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

        if params["classifiedFlag"] == 1:
            sqlQuery = """
                update pesstoObjects set snoozed = 0, alertWorkflowLocation = "%(awl)s" where transientBucketId = %(transientBucketId)s
            """ % locals()
        else:
            sqlQuery = """
                update pesstoObjects set classifiedFlag = 1, snoozed = 0, marshallWorkflowLocation = "review for followup", alertWorkflowLocation = "%(awl)s" where transientBucketId = %(transientBucketId)s
            """ % locals()
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

        updater = update_transient_summaries(
            log=emptyLogger(),
            settings=self.request.registry.settings["yaml settings"],
            dbConn=self.request.registry.settings["dbConn"],
            transientBucketId=transientBucketId
        ).update()

        self.response = self.response + \
            "Add a classification to transient #%(transientBucketId)s " % locals(
            )

        self.log.debug(
            'completed the ``_add_transient_classification`` method')
        return None

    # xt-class-method
