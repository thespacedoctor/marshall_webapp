#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_element_put.py
==============================
:Summary:
    The HTML template module for the `models_transients_element_put.py` resource

:Author:
    David Youn
:Date Created:
    October 7, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete review and cleanup this `models_transients_element_put.py` module
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from dryxPython import commonutils as dcu
from dryxPython import astrotools as dat


class models_transients_element_put():

    """
    The worker class for the models_transients_element_put module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request

    **Todo**
        - @review: when complete, clean models_transients_element_put class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

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

        log.debug("instansiating a new 'models_transients_element_put' object")

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def put(self):
        """get the models_transients_element_put object

        **Return:**
            - ``models_transients_element_put``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        if "mwl" in self.request.params or "awl" in self.request.params:
            self._move_transient_to_another_list()

        if set(("piName", "piEmail")) <= set(self.request.params):
            self._change_pi_for_object()

        if set(("clsObsdate", "clsSnClassification")) <= set(self.request.params):
            self._add_transient_classification()

        self.log.info('completed the ``get`` method')
        if len(self.response) == 0:
            self.response = "nothing has changed"
        return self.response

    def _move_transient_to_another_list(
            self):
        """ create sqlquery for the put request

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _create_sqlquery method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_create_sqlquery`` method')
        transientBucketId = self.transientBucketId

        if "mwl" in self.request.params:
            mwl = self.request.params["mwl"]
            sqlQuery = """
                update pesstoObjects set marshallWorkflowLocation = "%(mwl)s" where transientBucketId = %(transientBucketId)s
            """ % locals()
            self.request.db.execute(sqlQuery)
            self.response = self.response + \
                " transientBucketId %(transientBucketId)s moved to the `%(mwl)s` marshallWorkflowLocation<BR>" % locals(
                )

        if "awl" in self.request.params:
            mwl = self.request.params["awl"]
            sqlQuery = """
                update pesstoObjects set alertWorkflowLocation = "%(awl)s" where transientBucketId = %(transientBucketId)s
            """ % locals()
            self.request.db.execute(sqlQuery)
            self.response = self.response + \
                " transientBucketId %(transientBucketId)s moved to the `%(awl)s` alertWorkflowLocation<BR>" % locals(
                )

        self.log.info('completed the ``_create_sqlquery`` method')
        return None

    # use the tab-trigger below for new method
    def _change_pi_for_object(
            self):
        """ change pi for object

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _change_pi_for_object method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_change_pi_for_object`` method')

        piName = self.request.params["piName"]
        piEmail = self.request.params["piEmail"]
        transientBucketId = self.transientBucketId

        sqlQuery = """
            update pesstoObjects set pi_name = "%(piName)s", pi_email = "%(piEmail)s" where transientBucketId = %(transientBucketId)s   
        """ % locals()
        self.request.db.execute(sqlQuery)

        self.response = self.response + \
            "changed the PI of transient #%(transientBucketId)s to '%(piName)s' (%(piEmail)s)" % locals(
            )

        self.log.info('completed the ``_change_pi_for_object`` method')
        return None

    # use the tab-trigger below for new method
    def _add_transient_classification(
            self):
        """ add transient classification

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _add_transient_classification method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_add_transient_classification`` method')

        now = dcu.get_now_sql_datetime()
        transientBucketId = self.transientBucketId

        sqlQuery = """
            select raDeg, decDeg, name, htm20ID, htm16ID, cx, cy, cz from transientBucket where transientBucketId = %(transientBucketId)s and cx is not null limit 1
        """ % locals()
        rowsTmp = self.request.db.execute(sqlQuery).fetchall()
        rows = []
        rows[:] = [dict(zip(row.keys(), row)) for row in rowsTmp]

        for row in rows:
            for arg, val in row.iteritems():
                varname = arg
                if isinstance(val, str) or isinstance(val, unicode):
                    exec(varname + """ = '%s' """ % (val,))
                else:
                    exec(varname + """ = %s """ % (val,))

            obsMjd = dat.getMJDFromSqlDate(
                # "%Y-%m-%dT%H:%M:%S.%f"
                sqlDate="%(clsObsdate)sT00:00:00.0" % locals()
            )

            clsSnClassification = self.request.params["clsSnClassification"]
            clsType = self.request.params["clsType"]
            if "clsPeculiar" in self.request.params:
                clsSnClassification = "%(clsSnClassification)s-p" % locals()
            if clsType == "supernova":
                clsType = clsSnClassification

            if "clsRedshift" not in self.request.params:
                clsRedshift = "null"
            else:
                clsRedshift = self.request.params["clsRedshift"]

            if "clsClassificationWRTMax" not in self.request.params:
                clsClassificationWRTMax = "unknown"
            else:
                clsClassificationWRTMax = self.request.params[
                    "clsClassificationWRTMax"]

            if "clsClassificationPhase" not in self.request.params:
                clsClassificationPhase = "null"
            else:
                clsClassificationPhase = self.request.params[
                    "clsClassificationPhase"]

            sqlQuery = """
                INSERT INTO transientBucket (raDeg, decDeg, name, htm20ID, htm16ID, cx, cy, cz, transientBucketId, observationDate, observationMjd, survey, spectralType, transientRedshift, dateCreated, dateLastModified, classificationWRTMax, classificationPhase) VALUES(%(raDeg)s, %(decDeg)s, "%(name)s", %(htm20ID)s, %(htm16ID)s, %(cx)s, %(cy)s, %(cz)s, %(clsTransientBucketId)s, "%(clsObsdate)s", %(obsMjd)s, "%(clsSource)s", "%(clsType)s", %(clsRedshift)s, "%(now)s", "%(now)s", "%(clsClassificationWRTMax)s", %(clsClassificationPhase)s);
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

        # UPDATE THE FLAGS
        # update_transientbucketsummaries_flags.update_transientbucketsummaries_flags(
        # log, dbConn, updateAll=False, transientBucketId=clsTransientBucketId)

        self.log.info('completed the ``_add_transient_classification`` method')
        return None

    # use the tab-trigger below for new method
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
