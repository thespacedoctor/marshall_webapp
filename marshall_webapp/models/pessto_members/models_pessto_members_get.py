#!/usr/local/bin/python
# encoding: utf-8
"""
models_pessto_members_get.py
===============================
:Summary:
    The model get for the `models_pessto_members_get.py` resource

:Author:
    David Young

:Date Created:
    October 9, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
import collections
import urllib
import re


class models_pessto_members_get():

    """
    The worker class for the models_pessto_members_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
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
        self.defaultQs = {
            "format": "json",
            "sortBy": "secondname",
            "sortDesc": False
        }

        log.debug(
            "instansiating a new 'models_pessto_members_get' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """execute the get method on the models_pessto_members_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.info('starting the ``get`` method')

        if "sortBy" in self.qs and self.qs["sortBy"] is not False:
            orderBy = " order by " + self.qs["sortBy"]
        else:
            orderBy = " order by secondname"

        if "sortDesc" in self.qs:
            if self.qs["sortDesc"] == "True" or self.qs["sortDesc"] == True:
                orderDir = "desc"
            else:
                orderDir = ""
        else:
            orderDir = ""

        sqlQuery = u"""
            select firstname, secondname from webapp_users where secondname is not "doe" %(orderBy)s  %(orderDir)s
        """ % locals()

        membersTmp = self.request.db.execute(sqlQuery).fetchall()
        members = []
        members[:] = [dict(zip(row.keys(), row)) for row in membersTmp]

        self.log.info('completed the ``get`` method')
        return members

    def _set_default_parameters(
            self):
        """ set default parameters

        **Key Arguments:**
            -

        **Return:**
            - None
        """
        self.log.info('starting the ``_set_default_parameters`` method')

        if "format" not in self.qs:
            self.qs["format"] = self.defaultQs["format"]

        self.log.info('completed the ``_set_default_parameters`` method')
        return None

    # use the tab-trigger below for new method
    # xt-class-method
