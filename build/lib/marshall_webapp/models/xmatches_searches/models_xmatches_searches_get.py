#!/usr/local/bin/python
# encoding: utf-8
"""
*The model get for the `models_xmatches_searches_get.py` resource*

:Author:
    David Young
"""
from future import standard_library
standard_library.install_aliases()
from builtins import zip
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

class models_xmatches_searches_get(base_model):
    """
    The worker class for the models_xmatches_searches_get module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element id requests (or False)
    
    """

    def __init__(self, log, request, elementId=False, search=False):
        super().__init__(log, request, elementId, search)
        self.resourceName = "xmatches_searches"
        self.defaultQs = {
            "sortBy": "top_ranked_transient_associations",
            "sortDesc": True
        }
        self._set_default_parameters()

        log.debug(
            "instansiating a new 'models_xmatches_searches_get' object")
        return None

    def get(self):
        """execute the get method on the models_xmatches_searches_get object

        **Return**

        - ``responseContent`` -- the reponse to send to the browser
        
        """
        self.log.debug('starting the ``get`` method')

        sortBy = self.qs["sortBy"]
        if self.qs["sortDesc"] == True or self.qs["sortDesc"].lower() == "true":
            sortDesc = "desc"
        else:
            sortDesc = ""

        sqlQuery = u"""
            select * from tcs_stats_catalogues where transientStream = 0 order by %(sortBy)s %(sortDesc)s
        """ % locals()
        objectDataTmp = self.request.db.execute(sqlQuery).fetchall()
        objectData = []
        objectData[:] = [dict(list(zip(list(row.keys()), row)))
                         for row in objectDataTmp]

        responseContent = objectData

        self.log.debug('completed the ``get`` method')
        return responseContent

    # xt-class-method
