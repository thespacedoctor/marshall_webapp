#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `models_transients_element_context_post.py` resource*

:Author:
    David Young

:Date Created:
    September 18, 2014
"""
import sys
import os
import khufu
from fundamentals import times


class models_transients_element_context_post():
    """
    The worker class for the models_transients_element_context_post module

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
            "instansiating a new 'models_transients_element_context_post' object")

        return None

    def close(self):
        del self
        return None

    def post(self):
        """execute the put method on the models_transients_element_context_post object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``put`` method')

        transientBucketId = self.elementId

        # variables
        now = times.get_now_sql_datetime()
        author = self.request.authenticated_userid
        comment = self.request.params["sherlockMatchComment"]

        comment = comment.encode('unicode_escape').replace(
            "'", "\\'").replace('"', '\\"')

        # # ADD THE COMMENT TO THE DATABASE
        sqlQuery = """
           update sherlock_classifications set mismatchComment = "%(comment)s", user = "%(author)s", commentDate=now() where transient_object_id = %(transientBucketId)s;
        """ % locals()
        self.log.debug("""add comment sqlquery: `%(sqlQuery)s`""" % locals())
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

        responseContent = "%(author)s added the some verification info for the sherlock classification to transient #%(transientBucketId)s in the marshall<BR><BR>" % locals(
        )

        logEntry = "contextual classifier transient-host mismatch reported by %(author)s" % locals(
        )
        sqlQuery = u"""INSERT INTO transients_history_logs (
            transientBucketId,
            dateCreated,
            log
        )
        VALUES (
            %s,
            "%s",
            "%s"
        )""" % (transientBucketId, now, logEntry)
        self.request.db.execute(sqlQuery)
        self.request.db.commit()

        self.log.debug('completed the ``put`` method')
        return responseContent

    # xt-class-method
