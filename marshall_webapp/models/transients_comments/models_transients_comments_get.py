#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `models_transients_comments_get.py` resource*

:Author:
    David Young

:Date Created:
    October 9, 2014
"""
from builtins import object
import sys
import os
import khufu
from dryxPyramid.models.models_base import base_model


class models_transients_comments_get(base_model):
    """
    The worker class for the models_transients_comments_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
    """

    def __init__(self, log, request, elementId=False, search=False):
        super().__init__(log, request, elementId, search)
        self.resourceName = "transients_comments"
        self._set_default_parameters()
        log.debug(
            "instansiating a new 'models_transients_comments_get' object")
        return None

    def get(self):
        """execute the get method on the models_transients_comments_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')
        elementId = self.elementId

        if elementId:
            whereClause = " and pesstoObjectsID = %(elementId)s" % locals()
        else:
            whereClause = ""

        sqlQuery = """
            select * from pesstoObjectsComments where 1=1 %(whereClause)s order by dateCreated desc limit 10
        """ % locals()

        objectCommentsTmp = self.request.db.execute(sqlQuery).fetchall()
        objectComments = []
        objectComments[:] = [dict(list(zip(list(row.keys()), row)))
                             for row in objectCommentsTmp]

        print(objectComments)

        self.log.debug('completed the ``get`` method')
        return objectComments

    # xt-class-method
