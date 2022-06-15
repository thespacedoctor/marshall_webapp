#!/usr/bin/env python
# encoding: utf-8
"""
*The data model module for the `transients_element_followup_obs_post` resource*

:Author:
    David Young

:Date Created:
    June 15, 2022
"""
################# GLOBAL IMPORTS ####################
from builtins import object
import sys
import os
import khufu
from fundamentals import times


class models_transients_element_followup_obs_post(object):
    """
    *The worker class for the models_transients_element_followup_obs_post module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
        - ``search`` -- is this a search request (boolean)

    **Usage:**

    ```eval_rst
    .. todo::

        - add usage info
        - create a sublime snippet for usage
        - add a tutorial about ``models_transients_element_followup_obs_post`` to documentation
        - create a blog post about what ``models_transients_element_followup_obs_post`` does
    ```

    ```python
    usage code 
    ```
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        elementId=False,
        search=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        self.search = search
        self.qs = dict(request.params)  # the query string
        # the query string defaults
        self.defaultQs = {}
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_transients_element_followup_obs_post' object")

        # Variable Data Atrributes

        # Initial Actions
        self._set_default_parameters()

        return None

    # Method Attributes
    def post(self):
        """
        *execute the post method on the models_transients_element_followup_obs_post object*

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``post`` method')
        #Transient Bucked ID
        transientBucketId = self.elementId

        # variables
        #now = times.get_now_sql_datetime()
        author = self.request.authenticated_userid
        #comment = self.request.params["comment"]

        #comment = comment.replace(
        #    "'", "\\'").replace('"', '\\"')

        # add the comment to the database
        ob_id = 2
        sqlQuery = """
            INSERT INTO followup_obs (transientBucketId,author,OB_ID) VALUES(%(transientBucketId)s,"%(author)s","%(ob_id)s");
        """ % locals()
        self.log.debug("""add followupob sqlquery: `%(sqlQuery)s`""" % locals())
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

        responseContent = "%(author)s added a follow-ob for %(ob_id)s to transient %(transientBucketId)s in the marshall<BR><BR>" % locals()

        self.log.debug('completed the ``post`` method')
        #in self.qs you have the parameters.
        return responseContent

    def _set_default_parameters(
            self):
        """
        *set default parameters*

        **Key Arguments:**
            - 

        **Return:**
            - None
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        for k, v in list(self.defaultQs.items()):
            if k not in self.qs:
                self.qs[k] = v

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
