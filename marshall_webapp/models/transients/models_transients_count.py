#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_count.py
==========================
:Summary:
    Count the transients with a give flagset

:Author:
    David Young

:Date Created:
    October 3, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os


class models_transients_count():

    """
    The worker class for the models_transients_count module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``mwfFlag`` -- marshall workflow location
        - ``awfFlag`` -- alert workflow location
        - ``cFlag`` -- classification flag
        - ``snoozes`` -- snoozed flag

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        mwfFlag=None,
        awfFlag=None,
        cFlag=None,
        snoozed=None
    ):
        self.log = log
        log.debug("instansiating a new 'models_transients_count' object")
        self.request = request
        self.mwfFlag = mwfFlag
        self.awfFlag = awfFlag
        self.cFlag = cFlag
        self.snoozed = snoozed
        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the models_transients_count object

        **Return:**
            - ``models_transients_count``

        **Todo**
        """
        self.log.debug('starting the ``get`` method')

        mwfFlag = self.mwfFlag
        awfFlag = self.awfFlag
        cFlag = self.cFlag
        snoozed = self.snoozed

        # build the query to count the transients within a given marshall
        # sidebar list
        sqlQuery = """select count from meta_workflow_lists_counts where 1=1 """

        # AMEND WHERE CLAUSE TO INCLUDE WORKFLOW LOCATION FLAGS #
        extraWhere = ""
        if(mwfFlag != None):
            extraWhere = """%(extraWhere)s AND listName= %(mwfFlag)s """ % locals(
            )

        if(awfFlag != None):
            extraWhere = """%(extraWhere)s AND listName= %(awfFlag)s """ % locals(
            )

        if(cFlag != None):
            extraWhere = """%(extraWhere)s  AND listName = "classified" """ % locals(
            )

        if(snoozed != None):
            extraWhere = """%(extraWhere)s  AND listName = "snoozed" """ % locals(
            )

        sqlQuery = """%(sqlQuery)s %(extraWhere)s;""" % locals()

        rowsTmp = self.request.db.execute(sqlQuery).fetchall()
        rows = []
        rows[:] = [dict(zip(row.keys(), row)) for row in rowsTmp]

        count = 0
        for row in rows:
            count += row["count"]

        self.log.debug('completed the ``get`` method')
        return count
    # xt-class-method
