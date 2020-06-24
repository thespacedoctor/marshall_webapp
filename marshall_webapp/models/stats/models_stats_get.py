#!/usr/bin/env python
# encoding: utf-8
"""
*The model get for the `models_stats_get.py` resource*

:Author:
    David Young
"""
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


class models_stats_get(base_model):
    """
    *The worker class for the models_stats_get module*

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element id requests (or False)

    **Usage**

    ```python
    usage code 
    ```

    ```eval_rst
    .. todo::

        - add usage info
        - create a sublime snippet for usage
        - add a tutorial about ``models_stats_get`` to documentation
        - create a blog post about what ``models_stats_get`` does
    ```
    """

    def __init__(self, log, request, elementId=False, search=False):
        super().__init__(log, request, elementId, search)
        self.resourceName = "stats"
        self._set_default_parameters()

        log.debug(
            "instansiating a new 'models_stats_get' object")

        # Initial Actions

        return None

    def get(self):
        """
        *execute the get method on the models_stats_get object*

        **Return**

        - ``responseContent`` -- the reponse to send to the browser

        """
        self.log.debug('starting the ``get`` method')

        elementId = self.elementId
        # STATS OVERVIEW
        sqlQuery = """
            select * from stats_%(elementId)s_overview
        """ % locals()
        rowsTmp = self.request.db.execute(sqlQuery).fetchall()

        fileTypes = []
        fileTypes[:] = [dict(zip(row.keys(), row)) for row in rowsTmp]

        for row in fileTypes:
            try:
                del row['primaryId']
            except:
                pass

        sqlQuery = """
            select sum(numberOfFiles) as numberOfFiles, sum(dataVolumeBytes) as dataVolumeBytes from stats_%(elementId)s_overview
        """ % locals()

        rowsTmp = self.request.db.execute(sqlQuery).fetchall()
        fileTotals = []
        fileTotals[:] = [dict(zip(row.keys(), row)) for row in rowsTmp]

        print(f'self.qs["format"]: {self.qs["format"]}')
        if self.qs["format"] in ("csv", "plain_table"):
            print("SHIT")
            return fileTypes

        self.log.debug('completed the ``get`` method')
        return {"fileTypes": fileTypes, "fileTotals": fileTotals}

    # xt-class-method
