#!/usr/local/bin/python
# encoding: utf-8
"""
*The model get for the `models_xmatches_catalogues_get.py` resource*

:Author:
    David Young

:Date Created:
    October 9, 2014
"""
from future import standard_library
standard_library.install_aliases()
from builtins import zip
from builtins import object
import sys
import os
import khufu
import collections
import urllib.request, urllib.parse, urllib.error
import re


class models_xmatches_catalogues_get(object):
    """
    The worker class for the models_xmatches_catalogues_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
    """

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
        self.defaultQs = {
            "sortBy": "catalogue_table_id",
            "sortDesc": True
        }

        log.debug(
            "instansiating a new 'models_xmatches_catalogues_get' object")

        self._set_default_parameters()

        return None

    def get(self):
        """execute the get method on the models_xmatches_catalogues_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')

        sortBy = self.qs["sortBy"]
        if self.qs["sortDesc"] == True or self.qs["sortDesc"].lower() == "true":
            sortDesc = "desc"
        else:
            sortDesc = ""

        sqlQuery = u"""
            SELECT 
                *
            FROM
                (SELECT 
                    a.catalogue_table_id,
                        a.catalogue_table_name,
                        a.all_count,
                        COALESCE(top_rank_count, 0) AS `top_rank_count`
                FROM
                    (SELECT 
                    COUNT(*) AS all_count,
                        catalogue_table_name,
                        catalogue_table_id
                FROM
                    sherlock_crossmatches
                GROUP BY catalogue_table_name) AS a
                LEFT JOIN (SELECT 
                    COUNT(*) AS `top_rank_count`,
                        catalogue_table_name,
                        catalogue_table_id
                FROM
                    sherlock_crossmatches
                WHERE
                    rank = 1
                GROUP BY catalogue_table_name) AS b ON a.catalogue_table_id = b.catalogue_table_id) AS s order by %(sortBy)s %(sortDesc)s
        """ % locals()
        objectDataTmp = self.request.db.execute(sqlQuery).fetchall()
        objectData = []
        objectData[:] = [dict(list(zip(list(row.keys()), row))) for row in objectDataTmp]

        responseContent = objectData

        self.log.debug('completed the ``get`` method')
        return responseContent

    def _set_default_parameters(
            self):
        """ set default parameters
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        for k, v in list(self.defaultQs.items()):
            if k not in self.qs:
                self.qs[k] = v

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
