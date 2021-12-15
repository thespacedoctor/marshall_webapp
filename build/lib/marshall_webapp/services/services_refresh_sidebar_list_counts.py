#!/usr/local/bin/python
# encoding: utf-8
"""
*The data model module for the `services_refresh_sidebar_list_counts` resource*

:Author:
    David Young
"""
from builtins import object
import sys
import os
import khufu

class services_refresh_sidebar_list_counts(object):
    """
    The worker class for the services_refresh_sidebar_list_counts module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element id requests (or False)
    
    """

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
            "instansiating a new 'services_refresh_sidebar_list_counts' object")
        return None

    def close(self):
        del self
        return None

    def put(self):
        """execute the put method on the services_refresh_sidebar_list_counts object

        **Return**

        - ``responseContent`` -- the reponse to send to the browser
        
        """
        self.log.debug('starting the ``put`` method')

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

        # count all objects
        sqlQuery = """update meta_workflow_lists_counts set count = (select count(*) from pesstoObjects) where listname = "all" """ % locals(
        )
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

        # content for response
        responseContent += "<BR>updated `alertWorkflowLocation` in `meta_workflow_lists_counts` table"

        # count classified objects
        sqlQuery = """update meta_workflow_lists_counts set count = (select count(*) from pesstoObjects where classifiedFlag = 1) where listname = "classified" """ % locals(
        )
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

        # content for response
        responseContent += "<BR>updated `classified` list in `meta_workflow_lists_counts` table"

        # count snoozed objects
        sqlQuery = """update meta_workflow_lists_counts set count = (select count(*) from pesstoObjects where snoozed = 1) where listname = "snoozed" """ % locals(
        )
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

        # content for response
        responseContent += "<BR>updated `snoozed` list in `meta_workflow_lists_counts` table"

        self.log.debug('completed the ``put`` method')
        return responseContent

    # xt-class-method
