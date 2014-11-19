#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_element_comments_post.py
=======================================
:Summary:
    The HTML template module for the `models_transients_element_comments_post.py` resource

:Author:
    David Young

:Date Created:
    ddate

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
import dryxPython.commonutils as dcu


class models_transients_element_comments_post():

    """
    The worker class for the models_transients_element_comments_post module

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
            "instansiating a new 'models_transients_element_comments_post' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def post(self):
        """execute the put method on the models_transients_element_comments_post object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser

        **Todo**
        """
        self.log.info('starting the ``put`` method')

        transientBucketId = self.elementId

        # variables
        now = dcu.get_now_sql_datetime()
        author = self.request.params["author"]
        comment = self.request.params["comment"]

        # add the comment to the database
        sqlQuery = """
            INSERT INTO pesstoObjectsComments (pesstoObjectsId,commentAuthor,comment,dateCreated,dateLastModified) VALUES(%(transientBucketId)s,"%(author)s","%(comment)s","%(now)s","%(now)s");
        """ % locals()
        self.log.debug("""add comment sqlquery: `%(sqlQuery)s`""" % locals())
        self.request.db.execute(sqlQuery)

        responseContent = "%(author)s added the comment:<blockquote>%(comment)s</blockquote>to transient #%(transientBucketId)s in the marshall<BR><BR>" % locals(
        )

        self.log.info('completed the ``put`` method')
        return responseContent

    # xt-class-method
