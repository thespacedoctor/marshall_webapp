#!/usr/local/bin/python
# encoding: utf-8
"""
*Count the transients with a given flagset*

:Author:
    David Young
"""
from builtins import zip
from builtins import object
import sys
import os


class models_transients_count(object):
    """
    The worker class for the `models_transients_count` module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``mwfFlag`` -- marshall workflow location
    - ``awfFlag`` -- alert workflow location
    - ``cFlag`` -- classification flag
    - ``snoozes`` -- snoozed flag

    """

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

        return None

    def close(self):
        del self
        return None

    def get(self):
        """get the models_transients_count object

        **Return**

        - ``models_transients_count``
        """
        self.log.debug('starting the ``get`` method')

        mwfFlag = self.mwfFlag
        awfFlag = self.awfFlag
        cFlag = self.cFlag
        snoozed = self.snoozed

        # BUILD THE QUERY TO COUNT THE TRANSIENTS WITHIN A GIVEN MARSHALL
        # SIDEBAR LIST
        sqlQuery = """select count from meta_workflow_lists_counts where 1=1 """

        # AMEND WHERE CLAUSE TO INCLUDE WORKFLOW LOCATION FLAGS #
        extraWhere = ""
        if mwfFlag:
            mwfFlag = mwfFlag.replace('"', '')
            extraWhere = """%(extraWhere)s AND listName= "%(mwfFlag)s" """ % locals(
            )

        if(awfFlag != None):
            extraWhere = """%(extraWhere)s AND listName= %(awfFlag)s """ % locals(
            )

        if(cFlag != None):
            extraWhere = """%(extraWhere)s  AND listName = "classified" """ % locals(
            )

        if snoozed:
            extraWhere = """%(extraWhere)s  AND listName = "snoozed" """ % locals(
            )

        sqlQuery = """%(sqlQuery)s %(extraWhere)s;""" % locals()

        rowsTmp = self.request.db.execute(sqlQuery).fetchall()
        rows = []
        rows[:] = [dict(list(zip(list(row.keys()), row))) for row in rowsTmp]

        count = 0
        for row in rows:
            count += row["count"]

        self.log.debug('completed the ``get`` method')
        return count
    # xt-class-method
