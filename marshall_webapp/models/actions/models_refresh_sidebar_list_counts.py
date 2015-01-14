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
    """
    # Initialisation

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

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def put(self):
        """execute the put method on the models_refresh_sidebar_list_counts object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser

        **Todo**
        """
        self.log.info('starting the ``put`` method')

        # all marshall workflow list titles
        marshallWorkflowLists = ["inbox", "archive", "following", "pending observation",
                                 "followup complete", "review for followup", "pending classification"]

        # count objects in each list and update the `meta_workflow_lists_counts`
        # table
        for thisList in marshallWorkflowLists:
            sqlListName = thisList.replace(" ", "_")
            sqlQuery = """update meta_workflow_lists_counts set count = (select count(*) from pesstoObjects where marshallWorkflowLocation="%(thisList)s") where listname = "%(thisList)s" """ % locals(
            )
            self.request.db.execute(sqlQuery)
            self.request.db.commit()

        # content for response
        responseContent = "updated `marshallWorkflowLocations` in `meta_workflow_lists_counts` table"

        # all alert workflow list titles
        alertWorkflowLists = [
            "external alert released", "pessto classification released", "archived without alert", "queued for atel"]

        # count objects in each list and update the `meta_workflow_lists_counts`
        # table
        for thisList in alertWorkflowLists:
            sqlListName = thisList.replace(" ", "_")
            sqlQuery = """update meta_workflow_lists_counts set count = (select count(*) from pesstoObjects where alertWorkflowLocation="%(thisList)s") where listname = "%(thisList)s" """ % locals(
            )
            self.request.db.execute(sqlQuery)
            self.request.db.commit()

        # content for response
        responseContent += "<BR>updated `alertWorkflowLocation` in `meta_workflow_lists_counts` table"

        self.log.info('completed the ``put`` method')
        return responseContent

    # xt-class-method
