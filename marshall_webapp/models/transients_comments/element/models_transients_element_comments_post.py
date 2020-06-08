#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `models_transients_element_comments_post.py` resource*

:Author:
    David Young

:Date Created:
    September 18, 2014
"""
from builtins import object
import sys
import os
import khufu
from fundamentals import times


class models_transients_element_comments_post(object):
    """
    The worker class for the models_transients_element_comments_post module

    **Key Arguments:**
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
            "instansiating a new 'models_transients_element_comments_post' object")

        return None

    def close(self):
        del self
        return None

    def post(self):
        """execute the put method on the models_transients_element_comments_post object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``put`` method')

        transientBucketId = self.elementId

        # variables
        now = times.get_now_sql_datetime()
        author = self.request.authenticated_userid
        comment = self.request.params["comment"]

        comment = comment.encode('unicode_escape').replace(
            "'", "\\'").replace('"', '\\"')

        # add the comment to the database
        sqlQuery = """
            INSERT INTO pesstoObjectsComments (pesstoObjectsId,commentAuthor,comment,dateCreated,dateLastModified) VALUES(%(transientBucketId)s,"%(author)s","%(comment)s","%(now)s","%(now)s");
        """ % locals()
        self.log.debug("""add comment sqlquery: `%(sqlQuery)s`""" % locals())
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

        responseContent = "%(author)s added the comment:<blockquote>%(comment)s</blockquote>to transient #%(transientBucketId)s in the marshall<BR><BR>" % locals(
        )

        self.log.debug('completed the ``put`` method')
        return responseContent

    # xt-class-method
