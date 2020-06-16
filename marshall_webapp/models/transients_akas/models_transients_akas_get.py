#!/usr/bin/env python
# encoding: utf-8
"""
*The model get for the `models_transients_akas_get.py` resource*

:Author:
    David Young
"""
################# GLOBAL IMPORTS ####################
from future import standard_library
standard_library.install_aliases()
from builtins import object
import sys
import os
import khufu
import collections
import urllib.request
import urllib.parse
import urllib.error
import re
from dryxPyramid.models.models_base import base_model


class models_transients_akas_get(base_model):

    """
    *The worker class for the models_transients_akas_get module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)

    **Usage:**

    ```python
    usage code 
    ```

    ---

    ```eval_rst
    .. todo::

        - add usage info
        - create a sublime snippet for usage
        - add a tutorial about ``models_transients_akas_get`` to documentation
        - create a blog post about what ``models_transients_akas_get`` does
    ```
    """

    def __init__(self, log, request, elementId=False, search=False):
        super().__init__(log, request, elementId, search)
        self.resourceName = "stats"
        self.defaultQs = {
            "format": "json",
        }
        self._set_default_parameters()

        log.debug(
            "instansiating a new 'models_transients_akas_get' object")

        # Initial Actions

        return None

    def get(self):
        """
        *execute the get method on the models_transients_akas_get object*

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')

        elementId = self.elementId
        where = self.sql["where"]
        limit = self.sql["limit"]

        if elementId:
            where += " and transientBucketId in (%(elementId)s)" % locals(
            )

        sqlQuery = """
            select transientBucketId, GROUP_CONCAT(name) as akas from marshall_transient_akas %(where)s group by transientBucketId %(limit)s 
        """ % locals()
        tmp = self.request.db.execute(sqlQuery).fetchall()

        responseContent = []
        responseContent[:] = [dict(list(zip(list(row.keys()), row)))
                              for row in tmp]

        self.log.debug('completed the ``get`` method')
        return responseContent

    # xt-class-method
