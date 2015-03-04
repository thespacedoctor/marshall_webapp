#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_get.py
========================
:Summary:
    model for transient data in the marshall database - use this code to grab the transient data

:Author:
    David Young

:Date Created:
    September 30, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import collections
from sqlalchemy.sql import text
from dryxPython import mysql as dms
from dryxPython import astrotools as dat


class models_transients_get():

    """
    The worker class for the models_transients_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid/WebObs request object
        - ``elementId`` -- elementId (transientBucketId)
        - ``search`` -- is this a search query?

    **Todo**
    """

    def __init__(
        self,
        log,
        request,
        elementId=False,
        search=False
    ):
        self.log = log
        self.log.debug("instansiating a new 'models_transients_get' object")
        self.request = request
        self.qs = dict(request.params)  # the query string
        self.defaultQs = {  # the query string defaults
            "mwl": "inbox",
            "format": "html_tickets",
            "ticketLimit": 10,
            "tableLimit": 50,
            "pageStart": 0,
            "sortBy": "dateAdded",
            "sortDesc": False,
        }
        self.search = search
        self.elementId = elementId

        # xt-self-arg-tmpx

        # Initial Actions
        self._set_default_parameters()
        self.transientData, self.matchedTransientBucketIds, self.totalTicketCount = self._get_transient_data_from_database()

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the transientData object

        **Return:**
            - ``transientData``

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        self.transientAkas = self._get_associated_transient_aka()
        self.transientLightcurveData = self._get_associated_lightcurve_data()
        self.transientAtelMatches = self._get_associated_atel_data()
        self.transients_comments = self._get_associated_comments()

        self.log.info('completed the ``get`` method')

        if "format" in self.qs and (self.qs["format"] == "json" or self.qs["format"] == "csv" or self.qs["format"] == "plain_table"):
            self._clean_data_for_plain_text_outputs()
            return self.transientData

        qs = self.qs
        self.log.debug("""self.qs: `%(qs)s`""" % locals())

        return self.qs, self.transientData, self.transientAkas, self.transientLightcurveData, self.transientAtelMatches, self.transients_comments, self.totalTicketCount

    def _get_transient_data_from_database(
            self):
        """get the sqlquery based on the request object parameters

        **Key Arguments:**
            # -

        **Return:**
            - ``objectData``, ``matchedTransientBucketIds``, ``totalTicketCount`` -- 

        **Todo**
        """
        self.log.info('starting the ``get_data_from_database`` method')

        sqlWhereList = []

        # SEARCH
        if self.search and "q" in self.request.params:
            searchString = self.request.params["q"]

            searchString = searchString.lower().replace(" ", "%").replace(
                "-", "%").replace("_", "%").replace(":", "%").replace("+", "%")
            self.log.debug("""searchString: `%(searchString)s`""" % locals())
            # SEARCH MASTER & AKA NAMES
            sqlQuery = """
                select distinct t.transientBucketId as transientBucketId from transientBucket t, pesstoObjects p where (lower(t.name) like "%%%(searchString)s%%" or replace(p.pi_name," ","") like "%%%(searchString)s%%") and t.transientBucketId = p.transientBucketId
            """ % locals()
            self.log.debug(
                """sqlQUery for searchString: `%(sqlQuery)s`""" % locals())
            rows = dms.execute_mysql_read_query(
                sqlQuery=sqlQuery,
                dbConn=self.request.registry.settings["dbConn"],
                log=self.log
            )
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

        # COMBINE THE WHERE CLAUSES
        queryWhere = ""
        for thisWhere in range(len(sqlWhereList) - 1):
            queryWhere = """%(queryWhere)s %(thisWhere)s and""" % locals()
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
                     select s.transientBucketId from transientBucketSummaries s, pesstoObjects p %(queryWhere)s %(sep)s order by s.best_redshift %(sortDirection)s
                """ % locals()
            elif self.qs["sortBy"] == "latestComment":
                newWhere = queryWhere.replace("t.t", "t")
                sqlQuery = """
                    select c.pesstoObjectsId as transientBucketId, max(c.dateCreated) as latestCommentDate from pesstoObjectsComments c, pesstoObjects p %(newWhere)s and c.pesstoObjectsId = p.transientBucketID group by c.pesstoObjectsId order by latestCommentDate %(sortDirection)s
                """ % locals()

            elif self.qs["sortBy"] == "pi_name":
                # the ticket selection query
                sqlQuery = """
                    select t.transientBucketId from transientBucketSummaries t, pesstoObjects p %(queryWhere)s %(tep)s order by case when p.%(sortBy)s is null then 1 else 0 end,  p.%(sortBy)s %(sortDirection)s
                """ % locals()

            elif self.qs["sortBy"] == "observationPriority":
                sortBy = self.qs["sortBy"]
                sqlQuery = """
                    select t.transientBucketId from transientBucketSummaries t, pesstoObjects p %(queryWhere)s %(tep)s order by p.%(sortBy)s %(sortDirection)s
                """ % locals()

            else:
                # the ticket selection query
                sortBy = self.qs["sortBy"]
                sqlQuery = """
                    select t.transientBucketId from transientBucketSummaries t, pesstoObjects p %(queryWhere)s %(tep)s order by case when t.%(sortBy)s is null then 1 else 0 end,  t.%(sortBy)s %(sortDirection)s
                """ % locals()
        else:
            sqlQuery = """
                select t.transientBucketId from transientBucket t, pesstoObjects p %(queryWhere)s %(tep)s
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
                  "pesstoObjects": "p"}

        thisSchema = self.request.registry.settings["database_schema"]
        for k, v in tables.iteritems():
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
            select %(selectColumns)s from transientBucket t, transientBucketSummaries s, pesstoObjects p where t.transientBucketId in (%(matchedTransientBucketIds)s) and t.masterIdFlag = 1 and t.transientBucketId = p.transientBucketId and p.transientBucketId=s.transientBucketId order by FIELD(t.transientBucketId, %(matchedTransientBucketIds)s)
        """ % locals()
        tmpObjectData = self.request.db.execute(
            text(sqlQuery)).fetchall()

        objectData = []
        objectData[:] = [dict(zip(row.keys(), row)) for row in tmpObjectData]
        # for row in objectData:
        #     row = dict(zip(row.keys(), row))
        self.log.debug("""{objectData}""".format(**dict(globals(), **locals())))

        # get the total ticket count
        totalTicketCount = self._get_total_ticket_count_for_list(
            queryWhere=queryWhere)

        self.log.info('completed the ``get_data_from_database`` method')
        return objectData, matchedTransientBucketIds, totalTicketCount

    # use the tab-trigger below for new method
    def _set_default_parameters(
            self):
        """set default parameters in the request object if they have not yet been set

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
        """
        self.log.info('starting the ``set_default_parameters`` method')

        self.log.debug("""these are the current query string key/values: {self.qs}""".format(
            **dict(globals(), **locals())))

        # Assign the default values for the variables if they do not exist
        # Set inbox as the default view
        checkList = ["q", "mwl", "cf", "awl"]
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
                self.qs["limit"] = 10000

        if "pageStart" not in self.qs:
            self.qs["pageStart"] = self.defaultQs["pageStart"]

        if "sortBy" not in self.qs:
            if "mwl" in self.qs and self.qs["mwl"] in ["following", "pending observation", "allObsQueue"]:
                self.qs["sortBy"] = "observationPriority"
                self.qs["sortDesc"] = False
            else:
                self.qs["sortBy"] = self.defaultQs["sortBy"]
                self.qs["sortDesc"] = self.defaultQs["sortDesc"]

        self.log.debug("""these are the new query string key/values: {self.qs}""".format(
            **dict(globals(), **locals())))

        self.log.info('completed the ``set_default_parameters`` method')
        return None

    # use the tab-trigger below for new method
    def _get_associated_transient_aka(
            self):
        """ get associated aka names for the trasnsients

        **Key Arguments:**
            # -

        **Return:**
            - ``objectAkas`` -- the akas for the objects found

        **Todo**
        """
        self.log.info('starting the ``_get_associated_transient_aka`` method')

        matchedTransientBucketIds = self.matchedTransientBucketIds

        # GRAB AKAS
        sqlQuery = """
            select distinct transientBucketId, name, surveyObjectUrl from transientBucket where transientBucketId in (%(matchedTransientBucketIds)s) and name not like "%%atel%%" and masterIDFlag=0
        """ % locals()
        objectAkasTmp = self.request.db.execute(sqlQuery).fetchall()

        self.log.debug("""objectAkasTmp: `%(objectAkasTmp)s`""" % locals())

        objectAkas = []
        objectAkas[:] = [dict(zip(row.keys(), row)) for row in objectAkasTmp]

        self.log.info('completed the ``_get_associated_transient_aka`` method')
        return objectAkas

    # use the tab-trigger below for new method
    def _get_associated_lightcurve_data(
            self):
        """ get associated lightcurve data for the matched transients

        **Key Arguments:**
            # -

        **Return:**
            - ``lightCurveData`` -- the found objects' lightcurve data

        **Todo**
        """
        self.log.info('starting the ``_get_associated_lightcurve_data`` method')

        matchedTransientBucketIds = self.matchedTransientBucketIds

        sqlQuery = """
            select transientBucketId, magnitude, filter, survey, surveyObjectUrl, observationDate from transientBucket where transientBucketId in (%(matchedTransientBucketIds)s) and observationDate is not null and observationDate != 0000-00-00 and magnitude is not null and magnitude < 50 order by observationDate desc;
        """ % locals()
        lightCurveDataTmp = self.request.db.execute(sqlQuery).fetchall()
        lightCurveData = []
        lightCurveData[:] = [dict(zip(row.keys(), row))
                             for row in lightCurveDataTmp]

        self.log.info(
            'completed the ``_get_associated_lightcurve_data`` method')
        return lightCurveData

    # use the tab-trigger below for new method
    def _get_associated_atel_data(
            self):
        """ get associated atel data for the matched transients

        **Key Arguments:**
            # -

        **Return:**
            - ``transientAtelMatches`` -- the matched atels fot the transients

        **Todo**
        """
        self.log.info('starting the ``_get_associated_atel_data`` method')

        matchedTransientBucketIds = self.matchedTransientBucketIds

        sqlQuery = """
            select distinct transientBucketId, name, surveyObjectUrl from transientBucket where transientBucketId in (%(matchedTransientBucketIds)s) and name like "%%atel_%%"
        """ % locals()
        transientAtelMatchesTmp = self.request.db.execute(sqlQuery).fetchall()
        transientAtelMatches = []
        transientAtelMatches[:] = [
            dict(zip(row.keys(), row)) for row in transientAtelMatchesTmp]

        self.log.info('completed the ``_get_associated_atel_data`` method')
        return transientAtelMatches

    # use the tab-trigger below for new method
    def _get_associated_comments(
            self):
        """ get associated comments for the transients

        **Key Arguments:**
            # -

        **Return:**
            - ``objectComments`` -- object comments

        **Todo**
        """
        self.log.info('starting the ``_get_associated_comments`` method')

        matchedTransientBucketIds = self.matchedTransientBucketIds

        sqlQuery = """
            select * from pesstoObjectsComments where pesstoObjectsID in (%(matchedTransientBucketIds)s) order by dateCreated desc
        """ % locals()
        objectCommentsTmp = self.request.db.execute(sqlQuery).fetchall()
        objectComments = []
        objectComments[:] = [dict(zip(row.keys(), row))
                             for row in objectCommentsTmp]

        self.log.info('completed the ``_get_associated_comments`` method')
        return objectComments

    def _get_total_ticket_count_for_list(
            self,
            queryWhere):
        """ get total ticket count for list

        **Key Arguments:**
            - ``queryWhere`` -- the where segment of the ticket list sqlQuery string

        **Return:**
            - ``totalTickets`` -- total number of object in list

        **Todo**
        """
        self.log.info(
            'starting the ``_get_total_ticket_count_for_list`` method')

        if self.search:
            sqlQuery = """
                select count(*) from pesstoObjects t %(queryWhere)s;
            """ % locals()
            totalTicketsTmp = self.request.db.execute(sqlQuery).fetchall()
            totalTickets = []
            totalTickets[:] = [dict(zip(row.keys(), row))
                               for row in totalTicketsTmp]
            totalTickets = totalTickets[0]["count(*)"]
        elif self.elementId:
            totalTickets = 1
        else:
            ticketCountWhere = queryWhere.replace("marshallWorkflowLocation", "listName").replace(
                "alertWorkflowLocation", "listName").replace('classifiedFlag = "1"', 'listName="classified"')
            sqlQuery = """
                select count from meta_workflow_lists_counts %(ticketCountWhere)s;
            """ % locals()
            ticketCountRowsTmp = self.request.db.execute(sqlQuery).fetchall()
            ticketCountRows = []
            ticketCountRows[:] = [dict(zip(row.keys(), row))
                                  for row in ticketCountRowsTmp]
            totalTickets = 0
            for row in ticketCountRows:
                totalTickets += row["count"]

        self.log.info(
            'completed the ``_get_total_ticket_count_for_list`` method')
        return totalTickets

    # use the tab-trigger below for new method
    def _clean_data_for_plain_text_outputs(
            self):
        """ clean data for plain text outputs

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
        """
        self.log.info(
            'starting the ``_clean_data_for_plain_text_outputs`` method')

        # assoicate the correct column name to mysql database column name
        tmpDict = {}
        tableColumnNames = collections.OrderedDict(
            sorted(tmpDict.items()))
        tableColumnNames["masterName"] = "name"
        tableColumnNames["observationPriority"] = "priority"
        tableColumnNames["raDeg"] = "ra"
        tableColumnNames["decDeg"] = "dec"
        tableColumnNames["recentClassification"] = "spectral class"
        tableColumnNames["transientTypePrediction"] = "prediction"
        tableColumnNames["currentMagnitude"] = "latest mag"
        tableColumnNames["absolutePeakMagnitude"] = "abs peak mag"
        tableColumnNames["best_redshift"] = "z"
        tableColumnNames["distanceMpc"] = "mpc"
        tableColumnNames["earliestDetection"] = "discovery date"
        tableColumnNames["lastNonDetectionDate"] = "last non-detection date"
        tableColumnNames["dateAdded"] = "added to marshall"
        tableColumnNames["pi_name"] = "PI"
        tableColumnNames["pi_email"] = "pi email"

        # a list of names for table and csv views
        tableColumns = [
            "masterName",
            "observationPriority",
            "raDeg",
            "decDeg",
            "recentClassification",
            "transientTypePrediction",
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
            if "marshallWorkflowLocation" in obj:
                if obj["marshallWorkflowLocation"] == "following":
                    for n, w, c in zip([1, 2, 3], ["HIGH", "MEDIUM", "LOW"], ["red", "yellow", "green"]):
                        if obj["observationPriority"] == n:
                            obj["observationPriority"] = w
                            break
                elif obj["marshallWorkflowLocation"] == "pending observation":
                    for n, w, c in zip([1, 2, 3], ["HIGH", "MEDIUM", "LOW"], ["red", "yellow", "green"]):
                        if obj["observationPriority"] == n:
                            obj["observationPriority"] = w
                            break

        newTransientData = []
        for oldRow in self.transientData:
            tmpRow = {}
            newRow = collections.OrderedDict(sorted(tmpRow.items()))

            for oldName, newName in tableColumnNames.iteritems():
                newRow[newName] = oldRow[oldName]
                if "decdeg" in oldName.lower():
                    raSex = dat.ra_to_sex(
                        ra=float(oldRow["raDeg"]),
                        delimiter=':'
                    )
                    newRow["ra (sex)"] = raSex
                    decSex = dat.dec_to_sex(
                        dec=float(oldRow["decDeg"]),
                        delimiter=':'
                    )
                    newRow["dec (sex)"] = decSex
            newTransientData.append(newRow)

        self.transientData = newTransientData

        self.log.info(
            'completed the ``_clean_data_for_plain_text_outputs`` method')
        return None

        # use the tab-trigger below for new method
        # xt-class-method
