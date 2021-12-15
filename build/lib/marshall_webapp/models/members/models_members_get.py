#!/usr/local/bin/python
# encoding: utf-8
"""
*The model get for the `models_members_get.py` resource*

:Author:
    David Young
"""
from builtins import zip
from builtins import object
import sys
import os
import khufu
import collections
import re
from dryxPyramid.models.models_base import base_model

class models_members_get(base_model):
    """
    The worker class for the models_members_get module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element id requests (or False)
    
    """

    def __init__(self, log, request, elementId=False, search=False):
        super().__init__(log, request, elementId, search)
        self.resourceName = "members"
        self.defaultQs = {
            "sortBy": "secondname",
            "sortDesc": False
        }
        self._set_default_parameters()

        log.debug(
            "instansiating a new 'models_members_get' object")
        return None

    def get(self):
        """execute the get method on the models_members_get object

        **Return**

        - ``responseContent`` -- the reponse to send to the browser
        
        """
        self.log.debug('starting the ``get`` method')

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
            select firstname, secondname from webapp_users where secondname != "doe" %(orderBy)s  %(orderDir)s
        """ % locals()

        membersTmp = self.request.db.execute(sqlQuery).fetchall()
        members = []
        members[:] = [dict(list(zip(list(row.keys()), row)))
                      for row in membersTmp]

        self.log.debug('completed the ``get`` method')
        return members

    # xt-class-method
