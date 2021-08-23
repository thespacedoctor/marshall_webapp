#!/usr/bin/env python
# encoding: utf-8
"""
*The model get for the `models_transients_akas_get.py` resource*

:Author:
    David Young
"""
from builtins import str
from builtins import zip
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
        - add a tutorial about ``models_transients_akas_get`` to documentation
        - create a blog post about what ``models_transients_akas_get`` does
    ```
    """

    def __init__(self, log, request, elementId=False, search=False):
        super().__init__(log, request, elementId, search)
        self.resourceName = "stats"
        self._set_default_parameters()

        log.debug(
            "instansiating a new 'models_transients_akas_get' object")

        # Initial Actions

        return None

    def get(self):
        """
        *execute the get method on the models_transients_akas_get object*

        **Return**

        - ``responseContent`` -- the reponse to send to the browser

        """
        self.log.debug('starting the ``get`` method')

        elementId = self.elementId
        where = self.sql["where"]
        limit = self.sql["limit"]

        if elementId:
            sqlWhere = where + " and transientBucketId in (%(elementId)s)" % locals(
            )
        else:
            sqlWhere = ""

        sqlQuery = """
            select transientBucketId, GROUP_CONCAT(name) as akas from marshall_transient_akas %(sqlWhere)s group by transientBucketId %(limit)s
        """ % locals()
        tmp = self.request.db.execute(sqlQuery).fetchall()

        theseIds = []
        theseIds[:] = [str(t["transientBucketId"]) for t in tmp]
        theseIds = (",").join(theseIds)
        sqlWhere = where + \
            " and transientBucketId in (-99, %(theseIds)s)" % locals()

        if len(theseIds):
            sqlQuery = """
                select transientBucketId, name, url from marshall_transient_akas %(sqlWhere)s and hidden = 0 order by transientBucketId, master desc
            """ % locals()
            rows = self.request.db.execute(sqlQuery).fetchall()
        else:
            rows = []

        if not self.qs["format"]:
            objectAkas = []
            objectAkas[:] = [dict(list(zip(list(row.keys()), row)))
                             for row in rows]
            responseContent = objectAkas

        else:
            responseContent = self.convert_to_nested_data_structure(
                listOfDict=rows,
                primaryKey="transientBucketId",
                resourceName="akas",
                resourceKeys=["name", "url"])

        self.log.debug('completed the ``get`` method')
        return responseContent

    def convert_to_nested_data_structure(
            self,
            listOfDict,
            primaryKey,
            resourceName,
            resourceKeys):
        """*given a flat list of dictionaries, converts and returns the content in a nested structure better suited for json rendering*

        **Key Arguments**

        - ``listOfDict`` -- the list of dictionaries (generally returned from a database query)
        - ``primaryKey`` -- the primary key in the result sets by which to group json results by
        - ``resourceName`` -- the name of the subresource belong to be collected together
        - ``resourceKeys`` -- the name of the keys to be grouped together under the subresource


        **Usage**

        Here's an example usage of this method:

        ```python
        responseContent = self.convert_to_nested_data_structure(
            listOfDict=rows,
            primaryKey="transientBucketId",
            resourceName="akas",
            resourceKeys=["name", "url"]
        )
        ```
        """
        self.log.debug(
            'starting the ``convert_to_nested_data_structure`` method')

        import collections
        orderResults = collections.OrderedDict()

        seen = []
        responseBuilder = {}

        # CHECK FOR NULL CONTENT
        if not len(listOfDict):
            return []

        # GET THE ROOT LEVEL KEYS
        uniqueKeys = [primaryKey]
        for k in list(listOfDict[0].keys()):
            if k not in resourceKeys and k not in uniqueKeys:
                uniqueKeys.append(k)

        # BUILD THE NESTED STRUCTURE
        for row in listOfDict:
            pk = str(row[primaryKey])
            # HAVE WE SEEN THE PRIMARYKEY YET?
            if pk not in seen:
                seen.append(pk)
                responseBuilder[pk] = {
                    primaryKey: row[primaryKey]}
                for u in uniqueKeys:
                    responseBuilder[pk][u] = row[u]

                responseBuilder[pk][resourceName] = []

            # APPEND THE RESOURCES
            subresource = {}
            for k, v in dict(row).items():
                if k in resourceKeys:
                    subresource[k] = v
            if len(subresource):
                responseBuilder[pk][resourceName].append(subresource)

        # SORT THE NESTED STRUCTURE
        # sortList = [primaryKey] + sorted(uniqueKeys) + [resourceName]
        # for name, aDict in list(responseBuilder.items()):
        #     for k in sortList:
        #         orderResults[k] = aDict[k]
        #     responseBuilder[name] = orderResults

        responseContent = list(responseBuilder.values())

        self.log.debug(
            'completed the ``convert_to_nested_data_structure`` method')
        return responseContent

    # use the tab-trigger below for new method
    # xt-class-method
