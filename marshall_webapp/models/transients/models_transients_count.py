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
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
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

    **Todo**
        - @review: when complete, clean models_transients_count class
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
        mwfFlag=None,
        awfFlag=None,
        cFlag=None
    ):
        self.log = log
        log.debug("instansiating a new 'models_transients_count' object")
        self.request = request
        self.mwfFlag = mwfFlag
        self.awfFlag = awfFlag
        self.cFlag = cFlag
        # xt-self-arg-tmpx

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
    def get(self):
        """get the models_transients_count object

        **Return:**
            - ``models_transients_count``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        mwfFlag = self.mwfFlag
        awfFlag = self.awfFlag
        cFlag = self.cFlag

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

        sqlQuery = """%(sqlQuery)s %(extraWhere)s;""" % locals()

        rowsTmp = self.request.db.execute(sqlQuery).fetchall()
        rows = []
        rows[:] = [dict(zip(row.keys(), row)) for row in rowsTmp]

        count = 0
        for row in rows:
            count += row["count"]

        self.log.info('completed the ``get`` method')
        return count
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
