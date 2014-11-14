#!/usr/local/bin/python
# encoding: utf-8
"""
models_refresh_sidebar_list_counts.py
=====================================
:Summary:
    The data model module for the `models_refresh_sidebar_list_counts` resource

:Author:
    David Young

:Date Created:
    October 13, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete review and cleanup this models_refresh_sidebar_list_counts.py module
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu


class models_refresh_sidebar_list_counts():

    """
    The worker class for the models_refresh_sidebar_list_counts module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)

    **Todo**
        - @review: when complete, clean models_refresh_sidebar_list_counts class
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
        elementId=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_refresh_sidebar_list_counts' object")

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
        """execute the put method on the models_refresh_sidebar_list_counts object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser

        **Todo**
            - @review: when complete, clean put method
            - @review: when complete add logging
        """
        self.log.info('starting the ``put`` method')

        marshallWorkflowLists = ["inbox", "archive", "following", "pending observation",
                                 "followup complete", "review for followup", "pending classification"]
        for thisList in marshallWorkflowLists:
            sqlListName = thisList.replace(" ", "_")
            sqlQuery = """update meta_workflow_lists_counts set count = (select count(*) from pesstoObjects where marshallWorkflowLocation="%(thisList)s") where listname = "%(thisList)s" """ % locals(
            )
            self.request.db.execute(sqlQuery)

        responseContent = "updated `marshallWorkflowLocations` in `meta_workflow_lists_counts` table"

        alertWorkflowLists = [
            "external alert released", "pessto classification released", "archived without alert", "queued for atel"]

        for thisList in alertWorkflowLists:
            sqlListName = thisList.replace(" ", "_")
            sqlQuery = """update meta_workflow_lists_counts set count = (select count(*) from pesstoObjects where alertWorkflowLocation="%(thisList)s") where listname = "%(thisList)s" """ % locals(
            )
            self.request.db.execute(sqlQuery)

        responseContent += "<BR>updated `alertWorkflowLocation` in `meta_workflow_lists_counts` table"

        self.log.info('completed the ``put`` method')
        return responseContent

    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
