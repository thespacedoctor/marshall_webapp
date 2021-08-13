#!/usr/local/bin/python
# encoding: utf-8
"""
*model for transient data in the marshall database - use this code to grab the transient data*

:Author:
    David Young
"""
from future import standard_library
standard_library.install_aliases()
from builtins import zip
from builtins import object
import sys
import os
import collections
from sqlalchemy.sql import text
import urllib.request
import urllib.parse
import urllib.error
from astrocalc.coords import unit_conversion
from dryxPyramid.models.models_base import base_model
import re


class models_transients_get(base_model):
    """
    The worker class for the `models_transients_get` module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element id requests (or False)

    """

    def __init__(self, log, request, elementId=False, search=False, tcsCatalogueId=False):
        super().__init__(log, request, elementId, search)

        self.resourceName = "transients"
        self.defaultQs = {  # the query string defaults
            "mwl": "inbox",
            "format": "html_tickets",
            "ticketLimit": 10,
            "tableLimit": 100,
            "pageStart": 0,
            "sortBy": "dateAdded",
            "sortDesc": False,
            "filterBy1": "decDeg",
            "filterValue1": 30,
            "filterOp1": "<",
            "filterBy2": False,
            "filterValue2": False,
            "filterOp2": "="
        }
        self.tcsCatalogueId = tcsCatalogueId

        self._set_default_parameters()
        self.transientData, self.matchedTransientBucketIds, self.totalTicketCount = self._get_transient_data_from_database()

        log.debug(
            "instansiating a new 'models_transients_get' object")
        return None

    def get(self):
        """
        *get the transientData object*

        **Return**

        - ``transientData``

        """
        self.log.debug('starting the ``get`` method')

        self.transientAkas = self._get_associated_transient_aka()
        self.transientLightcurveData = self._get_associated_lightcurve_data()
        self.transientAtelMatches = self._get_associated_atel_data()
        self.transients_comments = self._get_associated_comments()
        self.transient_history = self._get_associated_transient_history()
        self.transient_crossmatches = self._get_associated_transient_crossmatches()

        self.log.debug('completed the ``get`` method')

        if "format" in self.qs and (self.qs["format"] == "json" or self.qs["format"] == "csv" or self.qs["format"] == "plain_table"):
            self._clean_data_for_plain_text_outputs()
            return self.transientData

        qs = self.qs
        self.log.debug("""self.qs: `%(qs)s`""" % locals())

        return self.qs, self.transientData, self.transientAkas, self.transientLightcurveData, self.transientAtelMatches, self.transients_comments, self.totalTicketCount, self.transient_history, self.transient_crossmatches

    def _get_transient_data_from_database(
            self):
        """
        *get the sqlquery based on the request object parameters*

        **Return**

        - ``objectData``
        - ``matchedTransientBucketIds``
        - ``totalTicketCount``

        """
        self.log.debug('starting the ``get_data_from_database`` method')

        tcsCatalogueId = self.tcsCatalogueId
        sqlWhereList = []
        regex1 = re.compile(r'[^A-Za-z0-9]')
        regex2 = re.compile(r'^(AT|SN)')
        # SEARCH
        if self.search and "q" in self.request.params:
            searchString = self.request.params["q"]
            searchString = regex1.sub('', searchString)
            searchString = regex2.sub('^(AT|SN)', searchString)
            self.log.debug("""searchString: `%(searchString)s`""" % locals())

            sqlQuery = f"""
                select  DISTINCT  transientBucketId from marshall_transient_akas where  REGEXP_REPLACE(name,"[^A-Za-z0-9]","") REGEXP '{searchString}' 
                union
                select DISTINCT  transientBucketId from pesstoObjects where  REGEXP_REPLACE(pi_name,"[^A-Za-z0-9]","") REGEXP '{searchString}' 
            """
            rows = self.request.db.execute(
                text(sqlQuery)).fetchall()

            searchList = ""
            for row in rows:
                transientBucketId = row["transientBucketId"]
                searchList = """%(searchList)s %(transientBucketId)s,""" % locals(
                )

            thisWhere = """t.transientBucketId in (%(searchList)s -99)""" % locals(
            )

            sqlWhereList.append(thisWhere)
            thisPageName = searchString
            self.log.debug("""searchList: `%(searchList)s`""" % locals())

        # Single Element Id (i.e. transientBucketId)
        if self.elementId:
            thisTransientBucketId = self.elementId
            thisWhere = """t.transientBucketId in (%(thisTransientBucketId)s)""" % locals(
            )
            sqlWhereList.append(thisWhere)

        # MARSHALL WORKFLOW
        if "mwl" in self.qs:
            if self.qs["mwl"] == "allObsQueue":
                thisWhere = """(marshallWorkflowLocation = "following" or marshallWorkflowLocation = "pending observation") """
            elif self.qs["mwl"] == "all":
                thisWhere = """1=1"""
            else:
                thisWhere = """marshallWorkflowLocation = "%(mwl)s" """ % self.qs
            sqlWhereList.append(thisWhere)

        # ALERT WORKFLOW
        if "awl" in self.qs:
            thisWhere = """alertWorkflowLocation = "%(awl)s" """ % self.qs
            sqlWhereList.append(thisWhere)

        # CLASSIFIED?
        if "cf" in self.qs:
            thisWhere = """classifiedFlag = "%(cf)s" """ % self.qs
            sqlWhereList.append(thisWhere)

        # SNOOZED?
        if "snoozed" in self.qs:
            thisWhere = """snoozed = "%(snoozed)s" """ % self.qs
            sqlWhereList.append(thisWhere)

        # FILTER?
        if "filterBy1" in self.qs and self.qs['filterBy1'] and "filterValue1" in self.qs and self.qs['filterValue1'] and "filterOp1" in self.qs and self.qs['filterOp1']:
            if self.qs['filterBy1'] in ("decDeg", "raDeg"):
                thisWhere = """t.`%(filterBy1)s` %(filterOp1)s %(filterValue1)s """ % self.qs
            else:
                try:
                    self.qs["filterValue1"] = float(self.qs["filterValue1"])
                    thisWhere = """`%(filterBy1)s` %(filterOp1)s %(filterValue1)s """ % self.qs
                except:
                    thisWhere = """`%(filterBy1)s` %(filterOp1)s "%(filterValue1)s" """ % self.qs

            sqlWhereList.append(thisWhere)

        if "filterBy2" in self.qs and self.qs['filterBy2'] and "filterValue2" in self.qs and self.qs['filterValue2'] and "filterOp2" in self.qs and self.qs['filterOp2']:
            if self.qs['filterBy2'] in ("decDeg", "raDeg"):
                thisWhere = """t.`%(filterBy2)s` %(filterOp2)s %(filterValue2)s """ % self.qs
            else:
                try:
                    self.qs["filterValue2"] = float(self.qs["filterValue2"])
                    thisWhere = """`%(filterBy2)s` %(filterOp2)s %(filterValue2)s """ % self.qs
                except:
                    thisWhere = """`%(filterBy2)s` %(filterOp2)s "%(filterValue2)s" """ % self.qs

            sqlWhereList.append(thisWhere)

        if "phaseiiiCheck" in self.qs:
            phaseiiiCheck = self.qs["phaseiiiCheck"]
            if phaseiiiCheck == "null":
                phaseiiiCheck = "is null"
            else:
                phaseiiiCheck = "= %(phaseiiiCheck)s" % locals()
            thisWhere = """t.transientBucketId in (SELECT transientBucketId FROM phase_iii_transient_catalogue_ssdr3 p, sherlock_classifications s where s.transient_object_id=p.TransientBucketId and s.matchVerified %(phaseiiiCheck)s) """ % locals()
            sqlWhereList.append(thisWhere)

        # tcsCatalogueId?
        if tcsCatalogueId:
            thisWhere = """cm.catalogue_table_id = %(tcsCatalogueId)s """ % locals(
            )
            if "tcsRank" in self.qs:
                rank = self.qs["tcsRank"]
                thisWhere += """ and cm.rank=%(rank)s""" % locals()
            sqlWhereList = []
            sqlWhereList.append(thisWhere)
            tcsCm = ", sherlock_crossmatches cm"
            tec = "and t.transientBucketId = cm.transient_object_id"
            sec = "and s.transientBucketId = cm.transient_object_id"
        else:
            tcsCm = ""
            tec = ""
            sec = ""

        # COMBINE THE WHERE CLAUSES
        queryWhere = ""
        for i, v in enumerate(sqlWhereList[:-1]):
            queryWhere = """%(queryWhere)s %(v)s and""" % locals()
        if len(sqlWhereList):
            finalWhere = sqlWhereList[-1]
            queryWhere = """where %(queryWhere)s %(finalWhere)s""" % locals()

        # Now build the SQL Query
        tep = "and t.transientBucketId = p.transientBucketId"
        sep = "and s.transientBucketId = p.transientBucketId"

        orderBy = ""
        if "sortBy" in self.qs and self.qs["sortBy"] is not False:
            sortRev = 0
            sortDirection = ""
            if "dateAdded" in self.qs["sortBy"] or "earliestDetection" in self.qs["sortBy"] or "Comment" in self.qs["sortBy"] or "lastNonDetectionDate" in self.qs["sortBy"]:
                sortRev = 1

            if (self.qs["sortDesc"] == "True" or self.qs["sortDesc"] == True) and sortRev == 0:
                sortDirection = "desc"
            elif (self.qs["sortDesc"] != "True" and self.qs["sortDesc"] != True) and sortRev == 1:
                sortDirection = "desc"

            if self.qs["sortBy"] == "redshift":
                sqlQuery = """
                     select s.transientBucketId from transientBucketSummaries s, pesstoObjects p %(tcsCm)s %(queryWhere)s %(sep)s %(sec)s  order by s.best_redshift %(sortDirection)s
                """ % locals()
            elif self.qs["sortBy"] == "latestComment":
                sqlQuery = """
                    select * from (select t.transientBucketId from pesstoObjects p, transientBucketSummaries t %(tcsCm)s %(queryWhere)s %(tec)s %(tep)s) as a LEFT OUTER JOIN (SELECT pesstoObjectsId, MAX(dateCreated) AS latestCommentDate FROM pesstoObjectsComments GROUP BY pesstoObjectsId) as b ON a.transientBucketId = b.pesstoObjectsId ORDER BY latestCommentDate %(sortDirection)s
                """ % locals()

            elif self.qs["sortBy"] == "pi_name":
                # the ticket selection query
                sortBy = self.qs["sortBy"]
                sqlQuery = """
                    select t.transientBucketId from transientBucketSummaries t, pesstoObjects p %(tcsCm)s %(queryWhere)s %(tep)s %(tec)s  order by case when p.%(sortBy)s is null then 1 else 0 end,  p.%(sortBy)s %(sortDirection)s
                """ % locals()

            elif self.qs["sortBy"] == "observationPriority":
                sortBy = self.qs["sortBy"]
                sqlQuery = """
                    select t.transientBucketId from transientBucketSummaries t, pesstoObjects p %(tcsCm)s %(queryWhere)s %(tep)s %(tec)s  order by p.%(sortBy)s %(sortDirection)s, case when t.dateAdded is null then 1 else 0 end,  t.dateAdded desc
                """ % locals()

            else:
                # the ticket selection query
                sortBy = self.qs["sortBy"]
                sqlQuery = """
                    select t.transientBucketId from transientBucketSummaries t, pesstoObjects p %(tcsCm)s %(queryWhere)s %(tep)s %(tec)s  order by case when t.%(sortBy)s is null then 1 else 0 end,  t.%(sortBy)s %(sortDirection)s
                """ % locals()
        else:
            sqlQuery = """
                select t.transientBucketId from transientBucket t, pesstoObjects p %(tcsCm)s %(queryWhere)s and replacedByRowId =0  %(tep)s %(tec)s
            """ % locals()

        # Add the limits and pagination to query
        pageStart = self.qs["pageStart"]
        limit = self.qs["limit"]
        sqlQuery = """%(sqlQuery)s limit %(pageStart)s, %(limit)s""" % locals()

        # grab the transientBucketIds

        rows = self.request.db.execute(sqlQuery).fetchall()
        self.log.debug("""{rows}""".format(**dict(globals(), **locals())))
        # GET ORDERED LIST OF THE TRANSIENTBUCKETIDs
        matchedTransientBucketIds = ""
        for aRow in rows:
            tbi = aRow["transientBucketId"]
            matchedTransientBucketIds = """%(matchedTransientBucketIds)s %(tbi)s,""" % locals(
            )
        matchedTransientBucketIds = "%(matchedTransientBucketIds)s -99" % locals(
        )

        # select column names
        selectColumns = ""
        skipColumns = [
            "lastNonDetectionDate", "classificationWRTMax", "classificationPhase"]
        tables = {"transientBucketSummaries": "s",
                  "transientBucket": "t",
                  "pesstoObjects": "p",
                  "sherlock_classifications": "sc"}

        thisSchema = self.request.registry.settings["database_schema"]
        for k, v in list(tables.items()):
            sqlQuery = """SELECT COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where table_name = "%(k)s" and TABLE_SCHEMA = "%(thisSchema)s" """ % locals(
            )
            rows = self.request.db.execute(sqlQuery).fetchall()
            self.log.debug(
                """rows: {rows}""".format(**dict(globals(), **locals())))

            for row in rows:
                if row["COLUMN_NAME"] not in skipColumns or k == "transientBucketSummaries":
                    skipColumns.append(row["COLUMN_NAME"])
                    columnName = row["COLUMN_NAME"]
                    selectColumns = """{selectColumns} {v}.{columnName},""".format(
                        **dict(globals(), **locals()))

        selectColumns = selectColumns[:-1]

        self.log.debug(
            """selectColumns: {selectColumns}""".format(**dict(globals(), **locals())))

        # grab the remaining data assocatied with the transientBucketIds
        sqlQuery = """
            select %(selectColumns)s from transientBucket t, transientBucketSummaries s, pesstoObjects p, sherlock_classifications sc where t.replacedByRowId = 0 and t.transientBucketId in (%(matchedTransientBucketIds)s) and t.masterIdFlag = 1 and t.transientBucketId = p.transientBucketId and p.transientBucketId=s.transientBucketId and t.transientBucketId = sc.transient_object_id order by FIELD(t.transientBucketId, %(matchedTransientBucketIds)s)
        """ % locals()
        tmpObjectData = self.request.db.execute(
            text(sqlQuery)).fetchall()

        objectData = []
        objectData[:] = [dict(list(zip(list(row.keys()), row)))
                         for row in tmpObjectData]
        # for row in objectData:
        #     row = dict(zip(row.keys(), row))
        self.log.debug(
            """{objectData}""".format(**dict(globals(), **locals())))

        # get the total ticket count
        totalTicketCount = self._get_total_ticket_count_for_list(
            queryWhere=queryWhere)

        self.log.debug('completed the ``get_data_from_database`` method')
        return objectData, matchedTransientBucketIds, totalTicketCount

    def _set_default_parameters(
            self):
        """
        *set default parameters in the request object if they have not yet been set*
        """
        self.log.debug('starting the ``set_default_parameters`` method')

        self.log.debug("""these are the current query string key/values: {self.qs}""".format(
            **dict(globals(), **locals())))

        # Assign the default values for the variables if they do not exist
        # Set inbox as the default view
        checkList = ["q", "mwl", "cf", "awl", "snoozed"]
        setDefaults = True
        for item in checkList:
            if item in self.qs:
                setDefaults = False

        if setDefaults is True and self.search == False and self.elementId == False:
            self.qs[u"mwl"] = u"inbox"

        # set ticketView as the default data type
        if "format" not in self.qs:
            self.qs["format"] = self.defaultQs["format"]

        # setup default pagination and limits
        if "limit" not in self.qs:
            if self.qs["format"] == "html_table":
                self.qs["limit"] = self.defaultQs["tableLimit"]
            elif self.qs["format"] == "html_tickets":
                self.qs["limit"] = self.defaultQs["ticketLimit"]
            else:
                self.qs["limit"] = 20000

        if "pageStart" not in self.qs:
            self.qs["pageStart"] = self.defaultQs["pageStart"]

        if "sortBy" not in self.qs:
            if "mwl" in self.qs and self.qs["mwl"] in ["following", "pending observation", "allObsQueue"]:
                self.qs["sortBy"] = "observationPriority"
                self.qs["sortDesc"] = False
            elif ("mwl" in self.qs and self.qs["mwl"] in ["inbox"]) or "snoozed" in self.qs:
                self.qs["sortBy"] = "currentMagnitudeDate"
                self.qs["sortDesc"] = True
            else:
                self.qs["sortBy"] = self.defaultQs["sortBy"]
                self.qs["sortDesc"] = self.defaultQs["sortDesc"]

        # ADD THE REST OF THE DEFAULTS TO THE QUERY STRING
        for k, v in list(self.defaultQs.items()):
            if k not in self.qs and 'q' not in self.qs and not self.elementId:
                if "awl" in self.qs and k == "mwl":
                    continue
                self.qs[k] = v

        self.qs["filterText1"] = ""
        if "filterBy1" in self.qs and self.qs["filterBy1"] and (self.qs["filterBy1"].lower() == "false" or "null" in self.qs["filterBy1"].lower()):
            self.qs["filterBy1"] = False
        if "filterBy1" in self.qs and self.qs["filterBy1"]:
            if "filterOp1" not in self.qs:
                self.qs["filterOp1"] = self.defaultQs["filterOp1"]
            if self.qs["filterOp1"].lower() == "eq":
                self.qs["filterOp1"] = "="
            elif self.qs["filterOp1"].lower() == "lt":
                self.qs["filterOp1"] = "<"
            elif self.qs["filterOp1"].lower() == "gt":
                self.qs["filterOp1"] = ">"
            elif self.qs["filterOp1"].lower() == "neq":
                self.qs["filterOp1"] = "!="

            self.qs[
                "filterText1"] = "with <strong>%(filterBy1)s %(filterOp1)s %(filterValue1)s</strong> " % self.qs

        self.qs["filterText2"] = ""
        if "filterBy2" in self.qs and self.qs["filterBy2"] and self.qs["filterBy2"].lower() == "false":
            self.qs["filterBy2"] = False
        if "filterBy2" in self.qs and self.qs["filterBy2"]:
            if "filterOp2" not in self.qs:
                self.qs["filterOp2"] = self.defaultQs["filterOp2"]
            if self.qs["filterOp2"].lower() == "eq":
                self.qs["filterOp2"] = "="
            elif self.qs["filterOp2"].lower() == "lt":
                self.qs["filterOp2"] = "<"
            elif self.qs["filterOp2"].lower() == "gt":
                self.qs["filterOp2"] = ">"
            elif self.qs["filterOp2"].lower() == "neq":
                self.qs["filterOp2"] = "!="

            self.qs[
                "filterText2"] = "with <strong>%(filterBy2)s %(filterOp2)s %(filterValue2)s</strong> " % self.qs
            self.qs["filterText2"] = self.qs["filterText2"].replace(
                "sherlockClassification", "contextual classification")

        self.log.debug("""these are the new query string key/values: {self.qs}""".format(
            **dict(globals(), **locals())))

        self.log.debug('completed the ``set_default_parameters`` method')
        return None

    def _get_associated_transient_aka(
            self):
        """
        *get associated aka names for the trasnsients*

        **Return**

        - ``objectAkas`` -- the akas for the objects found

        """
        self.log.debug('starting the ``_get_associated_transient_aka`` method')
        from marshall_webapp.models.transients_akas import models_transients_akas_get
        transients_akas = models_transients_akas_get(
            log=self.log,
            request=self.request,
            elementId=self.matchedTransientBucketIds
        )
        akas = transients_akas.get()

        self.log.debug(
            'completed the ``_get_associated_transient_aka`` method')
        return akas

    def _get_associated_lightcurve_data(
            self):
        """
        *get associated lightcurve data for the matched transients*

        **Return**

        - ``lightCurveData`` -- the found objects' lightcurve data

        """
        self.log.debug(
            'completed the ````_get_associated_lightcurve_data`` method')

        matchedTransientBucketIds = self.matchedTransientBucketIds

        sqlQuery = """
            select transientBucketId, magnitude, filter, survey, surveyObjectUrl, observationDate from transientBucket where replacedByRowId = 0 and transientBucketId in (%(matchedTransientBucketIds)s) and observationDate is not null and observationDate != 0000-00-00 and magnitude is not null and magnitude < 50 and limitingMag = 0 order by observationDate desc;
        """ % locals()
        lightCurveDataTmp = self.request.db.execute(sqlQuery).fetchall()
        lightCurveData = []
        lightCurveData[:] = [dict(list(zip(list(row.keys()), row)))
                             for row in lightCurveDataTmp]

        self.log.debug(
            'completed the ``_get_associated_lightcurve_data`` method')
        return lightCurveData

    def _get_associated_atel_data(
            self):
        """
        *get associated atel data for the matched transients*

        **Return**

        - ``transientAtelMatches`` -- the matched atels fot the transients

        """
        self.log.debug('starting the ``_get_associated_atel_data`` method')

        matchedTransientBucketIds = self.matchedTransientBucketIds

        sqlQuery = """
            select distinct transientBucketId, name, surveyObjectUrl from transientBucket where replacedByRowId = 0 and transientBucketId in (%(matchedTransientBucketIds)s) and name like "%%atel_%%"
        """ % locals()
        transientAtelMatchesTmp = self.request.db.execute(sqlQuery).fetchall()
        transientAtelMatches = []
        transientAtelMatches[:] = [
            dict(list(zip(list(row.keys()), row))) for row in transientAtelMatchesTmp]

        self.log.debug('completed the ``_get_associated_atel_data`` method')
        return transientAtelMatches

    def _get_associated_comments(
            self):
        """
        *get associated comments for the transients*

        **Return**

        - ``objectComments`` -- object comments

        """
        self.log.debug('starting the ``_get_associated_comments`` method')

        matchedTransientBucketIds = self.matchedTransientBucketIds

        sqlQuery = """
            select * from pesstoObjectsComments where pesstoObjectsID in (%(matchedTransientBucketIds)s) order by dateCreated desc
        """ % locals()
        objectCommentsTmp = self.request.db.execute(sqlQuery).fetchall()
        objectComments = []
        objectComments[:] = [dict(list(zip(list(row.keys()), row)))
                             for row in objectCommentsTmp]

        self.log.debug('completed the ``_get_associated_comments`` method')
        return objectComments

    def _get_total_ticket_count_for_list(
            self,
            queryWhere):
        """
        *get total ticket count for list*

        **Key Arguments**

        - ``queryWhere`` -- the where segment of the ticket list sqlQuery string


        **Return**

        - ``totalTickets`` -- total number of object in list

        """
        self.log.debug(
            'completed the ````_get_total_ticket_count_for_list`` method')

        tcsCatalogueId = self.tcsCatalogueId
        if self.search:
            sqlQuery = """
                select count(*) from pesstoObjects p, transientBucketSummaries t %(queryWhere)s and t.transientBucketId = p.transientBucketId;
            """ % locals()
            totalTicketsTmp = self.request.db.execute(sqlQuery).fetchall()
            totalTickets = []
            totalTickets[:] = [dict(list(zip(list(row.keys()), row)))
                               for row in totalTicketsTmp]
            totalTickets = totalTickets[0]["count(*)"]
        elif self.elementId:
            totalTickets = 1
        elif tcsCatalogueId:
            if "tcsRank" in self.qs:
                sqlQuery = """
                    select top_ranked_transient_associations as count from tcs_stats_catalogues where table_id = %(tcsCatalogueId)s;
                """ % locals()
            else:
                sqlQuery = """
                    select all_transient_associations as count from tcs_stats_catalogues where table_id = %(tcsCatalogueId)s;
                """ % locals()
            ticketCountRowsTmp = self.request.db.execute(sqlQuery).fetchall()
            ticketCountRows = []
            ticketCountRows[:] = [dict(list(zip(list(row.keys()), row)))
                                  for row in ticketCountRowsTmp]
            totalTickets = 0
            for row in ticketCountRows:
                totalTickets += row["count"]
        elif 'filterBy1' in self.qs or 'filterBy2' in self.qs:
            tcsCm = ", sherlock_crossmatches cm"
            tec = "and t.transientBucketId = cm.transient_object_id"
            sec = "and s.transientBucketId = cm.transient_object_id"
            tep = "and t.transientBucketId = p.transientBucketId"
            sep = "and s.transientBucketId = p.transientBucketId"

            sqlQuery = """
                    select count(*) as count from transientBucketSummaries t, pesstoObjects p %(queryWhere)s %(tep)s
                """ % locals()

            ticketCountRowsTmp = self.request.db.execute(sqlQuery).fetchall()
            ticketCountRows = []
            ticketCountRows[:] = [dict(list(zip(list(row.keys()), row)))
                                  for row in ticketCountRowsTmp]
            totalTickets = 0
            for row in ticketCountRows:
                totalTickets += row["count"]
        elif 'phase_iii_transient_catalogue_ssdr3' in queryWhere:
            sqlQuery = """
                    select count(*) as count FROM phase_iii_transient_catalogue_ssdr3 p, sherlock_classifications s where s.transient_object_id=p.TransientBucketId and s.matchVerified is null
            """ % locals()
            ticketCountRowsTmp = self.request.db.execute(sqlQuery).fetchall()
            ticketCountRows = []
            ticketCountRows[:] = [dict(list(zip(list(row.keys()), row)))
                                  for row in ticketCountRowsTmp]
            totalTickets = 0
            for row in ticketCountRows:
                totalTickets += row["count"]
        else:
            ticketCountWhere = queryWhere.replace("marshallWorkflowLocation", "listName").replace(
                "alertWorkflowLocation", "listName").replace('classifiedFlag = "1"', 'listName="classified"').replace('snoozed = "1"', 'listName="snoozed"')
            sqlQuery = """
                select count from meta_workflow_lists_counts %(ticketCountWhere)s;
            """ % locals()
            ticketCountRowsTmp = self.request.db.execute(sqlQuery).fetchall()
            ticketCountRows = []
            ticketCountRows[:] = [dict(list(zip(list(row.keys()), row)))
                                  for row in ticketCountRowsTmp]
            totalTickets = 0
            for row in ticketCountRows:
                totalTickets += row["count"]

        self.log.debug(
            'completed the ``_get_total_ticket_count_for_list`` method')
        return totalTickets

    def _clean_data_for_plain_text_outputs(
            self):
        """
        *clean data for plain text outputs*

        **Return**

        - None

        """
        self.log.debug(
            'completed the ````_clean_data_for_plain_text_outputs`` method')

        # ASTROCALC UNIT CONVERTER OBJECT
        converter = unit_conversion(
            log=self.log
        )

        # assoicate the correct column name to mysql database column name
        tmpDict = {}
        tableColumnNames = collections.OrderedDict(
            sorted(tmpDict.items()))
        tableColumnNames["masterName"] = "name"
        tableColumnNames["observationPriority"] = "priority"
        tableColumnNames["raDeg"] = "ra"
        tableColumnNames["decDeg"] = "dec"
        tableColumnNames["recentClassification"] = "spectral class"
        tableColumnNames["classificationPhase"] = "classification phase"
        tableColumnNames["classificationWRTMax"] = "classificationWRTMax"
        tableColumnNames["classificationDate"] = "classification date"
        tableColumnNames["currentMagnitude"] = "latest mag"
        tableColumnNames["absolutePeakMagnitude"] = "abs peak mag"
        tableColumnNames["best_redshift"] = "z"
        tableColumnNames["distanceMpc"] = "mpc"
        tableColumnNames["earliestDetection"] = "discovery date"
        tableColumnNames["lastNonDetectionDate"] = "last non-detection date"
        tableColumnNames["dateAdded"] = "added to marshall"
        tableColumnNames["pi_name"] = "PI"
        tableColumnNames["pi_email"] = "pi email"
        tableColumnNames["akas"] = "akas"

        # a list of names for table and csv views
        tableColumns = [
            "masterName",
            "observationPriority",
            "raDeg",
            "decDeg",
            "recentClassification",
            "classificationPhase",
            "classificationWRTMax",
            "classificationDate",
            "currentMagnitude",
            "absolutePeakMagnitude",
            "best_redshift",
            "distanceMpc",
            "earliestDetection",
            "lastNonDetectionDate",
            "dateAdded",
            "pi_name"
        ]

        # convert priorities to words
        for obj in self.transientData:

            for item in self.transientAkas:
                if item["transientBucketId"] == obj["transientBucketId"]:
                    obj["masterName"] = item["akas"][0]['name']
                    obj["akas"] = item["akas"]
                    break

            if "marshallWorkflowLocation" in obj:
                if obj["marshallWorkflowLocation"] == "following":
                    for n, w, c in zip([1, 2, 3, 4], ["CRITICAL", "IMPORTANT", "USEFUL", "NONE"], ["green", "yellow", "red", "blue"]):
                        if obj["observationPriority"] == n:
                            obj["observationPriority"] = w
                            break
                elif obj["marshallWorkflowLocation"] == "pending observation":
                    for n, w, c in zip([1, 2, 3], ["HIGH", "MEDIUM", "LOW"], ["green", "yellow", "red"]):
                        if obj["observationPriority"] == n:
                            obj["observationPriority"] = w
                            break

        newTransientData = []
        for oldRow in self.transientData:
            tmpRow = {}
            newRow = collections.OrderedDict(sorted(tmpRow.items()))

            for oldName, newName in list(tableColumnNames.items()):

                newRow[newName] = oldRow[oldName]
                if "decdeg" in oldName.lower():

                    raSex = converter.ra_decimal_to_sexegesimal(
                        ra=float(oldRow["raDeg"]),
                        delimiter=":"
                    )
                    newRow["ra (sex)"] = raSex
                    decSex = converter.dec_decimal_to_sexegesimal(
                        dec=float(oldRow["decDeg"]),
                        delimiter=":"
                    )
                    newRow["dec (sex)"] = decSex
            newTransientData.append(newRow)

        self.transientData = newTransientData

        self.log.debug(
            'completed the ``_clean_data_for_plain_text_outputs`` method')
        return None

    def _get_associated_transient_history(
            self):
        """
        *get associated transient history*
        """
        self.log.debug(
            'completed the ````_get_associated_transient_history`` method')

        matchedTransientBucketIds = self.matchedTransientBucketIds

        sqlQuery = """
            select * from transients_history_logs where transientBucketId in (%(matchedTransientBucketIds)s) order by dateCreated desc
        """ % locals()

        objectHistoryTmp = self.request.db.execute(sqlQuery).fetchall()
        objectHistory = []
        objectHistory[:] = [dict(list(zip(list(row.keys()), row)))
                            for row in objectHistoryTmp]

        from operator import itemgetter
        objectHistory = list(objectHistory)
        objectHistory = sorted(
            objectHistory, key=itemgetter('dateCreated'), reverse=False)

        self.log.debug(
            'completed the ``_get_associated_transient_history`` method')
        return objectHistory

    def _get_associated_transient_crossmatches(
            self):
        """
        *get associated transient crossmatches*
        """
        self.log.debug(
            'completed the ````_get_associated_transient_crossmatches`` method')

        from astrocalc.coords import unit_conversion
        # ASTROCALC UNIT CONVERTER OBJECT
        converter = unit_conversion(
            log=self.log
        )

        matchedTransientBucketIds = self.matchedTransientBucketIds

        sqlQuery = """
            select *, t.raDeg, t.decDeg from sherlock_crossmatches t, transientBucket b where b.replacedByRowId = 0 and b.transientBucketId in (%(matchedTransientBucketIds)s) and b.transientBucketId = t.transient_object_id  and b.masterIDFlag = 1 and rank is not null order by rank
        """ % locals()

        crossmatchesTmp = self.request.db.execute(sqlQuery).fetchall()
        crossmatches = []
        crossmatches[:] = [dict(list(zip(list(row.keys()), row)))
                           for row in crossmatchesTmp]

        from operator import itemgetter
        crossmatches = list(crossmatches)
        crossmatches = sorted(
            crossmatches, key=itemgetter('rank'), reverse=False)

        for c in crossmatches:
            c["object_link"] = None
            objectName = urllib.parse.quote(c["catalogue_object_id"])
            if "ned" in c["catalogue_table_name"].lower():
                c[
                    "object_link"] = "https://ned.ipac.caltech.edu/cgi-bin/objsearch?objname=%(objectName)s&extend=no&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=RA+or+Longitude&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES" % locals()
            elif "sdss" in c["catalogue_table_name"].lower():
                c[
                    "object_link"] = "http://skyserver.sdss.org/dr12/en/tools/explore/Summary.aspx?id=%(objectName)s" % locals()
                ra = converter.ra_decimal_to_sexegesimal(
                    ra=c["raDeg"],
                    delimiter=""
                )
                dec = converter.dec_decimal_to_sexegesimal(
                    dec=c["decDeg"],
                    delimiter=""
                )
                c["catalogue_object_id"] = "SDSS J" + ra[0:9] + dec[0:9]
                objectName = urllib.parse.quote(c["catalogue_object_id"])
            elif "milliquas" in c["catalogue_table_name"].lower():
                c[
                    "object_link"] = "https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3query.pl?bparam_name=%(objectName)s&navtrail=%%3Ca+class%%3D%%27navpast%%27+href%%3D%%27https%%3A%%2F%%2Fheasarc.gsfc.nasa.gov%%2FW3Browse%%2Fall%%2Fmilliquas.html%%27%%3E+Choose+Tables%%3C%%2Fa%%3E+%%3E+%%3Ca+class%%3D%%27navpast%%27+href%%3D%%27%%2Fcgi-bin%%2FW3Browse%%2Fw3table.pl%%3FREAL_REMOTE_HOST%%3D143.117.37.81%%26tablehead%%3Dname%%253Dmilliquas%%26Action%%3DMore%%2BOptions%%26REAL_REMOTE_HOST%%3D143%%252E117%%252E37%%252E81%%26Equinox%%3D2000%%26Action%%3DMore%%2BOptions%%26sortby%%3Dpriority%%26ResultMax%%3D1000%%26maxpriority%%3D99%%26Coordinates%%3DEquatorial%%26tablehead%%3Dname%%253Dmilliquas%%26Action%%3DParameter%%2BSearch%%27%%3EParameter+Search%%3C%%2Fa%%3E&popupFrom=Query+Results&tablehead=name%%3Dheasarc_milliquas%%26description%%3DMillion+Quasars+Catalog+%%28MILLIQUAS%%29%%2C+Version+4.5+%%2810+May+2015%%29%%26url%%3Dhttp%%3A%%2F%%2Fheasarc.gsfc.nasa.gov%%2FW3Browse%%2Fgalaxy-catalog%%2Fmilliquas.html%%26archive%%3DN%%26radius%%3D1%%26mission%%3DGALAXY+CATALOG%%26priority%%3D5%%26tabletype%%3DObject&dummy=Examples+of+query+constraints%%3A&varon=name&bparam_name%%3A%%3Aunit=+&bparam_name%%3A%%3Aformat=char25&varon=ra&bparam_ra=&bparam_ra%%3A%%3Aunit=degree&bparam_ra%%3A%%3Aformat=float8%%3A.5f&varon=dec&bparam_dec=&bparam_dec%%3A%%3Aunit=degree&bparam_dec%%3A%%3Aformat=float8%%3A.5f&varon=bmag&bparam_bmag=&bparam_bmag%%3A%%3Aunit=mag&bparam_bmag%%3A%%3Aformat=float8%%3A4.1f&varon=rmag&bparam_rmag=&bparam_rmag%%3A%%3Aunit=mag&bparam_rmag%%3A%%3Aformat=float8%%3A4.1f&varon=redshift&bparam_redshift=&bparam_redshift%%3A%%3Aunit=+&bparam_redshift%%3A%%3Aformat=float8%%3A6.3f&varon=radio_name&bparam_radio_name=&bparam_radio_name%%3A%%3Aunit=+&bparam_radio_name%%3A%%3Aformat=char22&varon=xray_name&bparam_xray_name=&bparam_xray_name%%3A%%3Aunit=+&bparam_xray_name%%3A%%3Aformat=char22&bparam_lii=&bparam_lii%%3A%%3Aunit=degree&bparam_lii%%3A%%3Aformat=float8%%3A.5f&bparam_bii=&bparam_bii%%3A%%3Aunit=degree&bparam_bii%%3A%%3Aformat=float8%%3A.5f&bparam_broad_type=&bparam_broad_type%%3A%%3Aunit=+&bparam_broad_type%%3A%%3Aformat=char4&bparam_optical_flag=&bparam_optical_flag%%3A%%3Aunit=+&bparam_optical_flag%%3A%%3Aformat=char3&bparam_red_psf_flag=&bparam_red_psf_flag%%3A%%3Aunit=+&bparam_red_psf_flag%%3A%%3Aformat=char1&bparam_blue_psf_flag=&bparam_blue_psf_flag%%3A%%3Aunit=+&bparam_blue_psf_flag%%3A%%3Aformat=char1&bparam_ref_name=&bparam_ref_name%%3A%%3Aunit=+&bparam_ref_name%%3A%%3Aformat=char6&bparam_ref_redshift=&bparam_ref_redshift%%3A%%3Aunit=+&bparam_ref_redshift%%3A%%3Aformat=char6&bparam_qso_prob=&bparam_qso_prob%%3A%%3Aunit=percent&bparam_qso_prob%%3A%%3Aformat=int2%%3A3d&bparam_alt_name_1=&bparam_alt_name_1%%3A%%3Aunit=+&bparam_alt_name_1%%3A%%3Aformat=char22&bparam_alt_name_2=&bparam_alt_name_2%%3A%%3Aunit=+&bparam_alt_name_2%%3A%%3Aformat=char22&Entry=&Coordinates=J2000&Radius=Default&Radius_unit=arcsec&NR=CheckCaches%%2FGRB%%2FSIMBAD%%2FNED&Time=&ResultMax=10&displaymode=Display&Action=Start+Search&table=heasarc_milliquas" % locals()
            elif ("ps1" not in c["catalogue_table_name"].lower()) and ("ritter" not in c["catalogue_table_name"].lower()) and ("down" not in c["catalogue_table_name"].lower()) and ("guide_star" not in c["catalogue_table_name"].lower()) and ("kepler" not in c["catalogue_table_name"].lower()):
                c[
                    "object_link"] = "http://simbad.u-strasbg.fr/simbad/sim-id?Ident=%(objectName)s&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit+id" % locals()

            c["best_mag"] = None
            c["best_mag_error"] = None
            c["best_mag_filter"] = None
            filters = ["R", "V", "B", "I", "J", "G", "H", "K", "U",
                       "_r", "_g", "_i", "_g", "_z", "_y", "_u", "unkMag"]
            for f in filters:
                if c[f] and not c["best_mag"]:
                    c["best_mag"] = c[f]
                    c["best_mag_error"] = c[f + "Err"]
                    c["best_mag_filter"] = f.replace(
                        "_", "").replace("Mag", "")

        self.log.debug(
            'completed the ``_get_associated_transient_crossmatches`` method')
        return crossmatches

        # xt-class-method
