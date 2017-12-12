#!/usr/local/bin/python
# encoding: utf-8
"""
templates_transients.py
=======================
:Summary:
    Template for the transients view

:Author:
    David Young

:Date Created:
    October 3, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import yaml
import re
from ...models.transients import models_transients_get
from pyramid.path import AssetResolver
import khufu


class templates_transients():

    """
    The worker class for the templates_transients module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid/WebObs request object
        - ``elementId`` -- the specific element requested (or False)
        - ``search`` -- is this a search? (boolean)
        - ``tcsCatalogueId`` -- tcs catalogue Id (for catalogue match views)

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        elementId=False,
        search=False,
        tcsCatalogueId=False
    ):
        self.log = log
        self.request = request
        log.debug("instansiating a new 'templates_transients' object")
        self.elementId = elementId
        self.search = search
        self.tcsCatalogueId = tcsCatalogueId

        # xt-self-arg-tmpx

        # grab the required data from the database and add it as attributes to
        # this object
        transientModal = models_transients_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId,
            search=self.search,
            tcsCatalogueId=tcsCatalogueId
        )
        self.qs, self.transientData, self.transientAkas, self.transientLightcurveData, self.transientAtelMatches, self.transients_comments, self.totalTicketCount, self.transientHistories, self.transientCrossmatches = transientModal.get(
        )

        if tcsCatalogueId:
            sqlQuery = u"""
                select table_name from tcs_stats_catalogues where table_id = %(tcsCatalogueId)s
            """ % locals()
            objectDataTmp = self.request.db.execute(sqlQuery).fetchall()
            objectData = []
            objectData[:] = [dict(zip(row.keys(), row))
                             for row in objectDataTmp]
            table_name = objectData[0]["table_name"]
            table_name = table_name.replace(
                "tcs_cat_", "").replace("_", " ")
            regex = re.compile(r'(v\d{1,3}) (\d{1,3})( (\d{1,3}))?')
            self.tcsCatalogueName = regex.sub(
                "\g<1>.\g<2>", table_name)
        else:
            self.tcsCatalogueName = False

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the templates_transients object

        **Return:**
            - ``webpage`` -- the webapge HTML

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        # choose which format of the content to display

        if self.qs["format"] == "html_table":
            maincontent = self._get_object_table()
        else:
            maincontent = self._get_object_tickets()

        from ..commonelements.pagetemplates import defaultpagetemplate

        if self.tcsCatalogueId:
            sideBar = "xmatches"
        else:
            sideBar = False

        webpage = defaultpagetemplate(
            log=self.log,
            request=self.request,
            bodyId=False,
            pageTitle="PESSTO Marshall",
            topNavBar=False,
            sideBar=sideBar,
            mainContent=maincontent,
            relativePathFromDocRoot=False,
            thisPageName=self._get_page_name()
        )

        self.log.info('completed the ``get`` method')
        return webpage

    def _get_list_of_transient_tickets(
            self):
        """ get list of transient tickets

        **Key Arguments:**
            # -

        **Return:**
            - ``ticketList`` -- a list of HTML tickets to display in the webapp

        **Todo**
        """
        from ..commonelements.tickets.single_ticket import single_ticket
        from dryxPython import astrotools as dat

        self.log.info('starting the ``_get_list_of_transient_tickets`` method')

        # for each transient build a ticket to be presented in the browser
        ticketList = []
        for discoveryDataDictionary in self.transientData:
            if discoveryDataDictionary["raDeg"]:
                raSex = dat.ra_to_sex(
                    ra=discoveryDataDictionary["raDeg"],
                    delimiter=':'
                )
                discoveryDataDictionary["raSex"] = raSex
            else:
                discoveryDataDictionary["raSex"] = None
            if discoveryDataDictionary["decDeg"]:
                decSex = dat.dec_to_sex(
                    dec=discoveryDataDictionary["decDeg"],
                    delimiter=':'
                )
                discoveryDataDictionary["decSex"] = decSex
            else:
                discoveryDataDictionary["decSex"] = None
            transientBucketId = discoveryDataDictionary["transientBucketId"]
            observationPriority = discoveryDataDictionary[
                "observationPriority"]

            self.log.debug(
                """transientBucketId, observationPriority: `%(transientBucketId)s` %(observationPriority)s""" % locals())

            thisTicket = single_ticket(
                log=self.log,
                request=self.request,
                discoveryDataDictionary=discoveryDataDictionary,
                objectComments=self.transients_comments,
                objectAkas=self.transientAkas,
                lightcurveData=self.transientLightcurveData,
                atelData=self.transientAtelMatches,
                objectHistories=self.transientHistories,
                transientCrossmatches=self.transientCrossmatches
            )
            ticketList.append(thisTicket)

        self.log.info(
            'completed the ``_get_list_of_transient_tickets`` method')
        return ticketList

    def _get_sort_dropdown(
            self):
        """ get sort dropdown

        **Key Arguments:**
            # -

        **Return:**
            - ``sort`` -- the sort dropdown for the transient listings toolbar
            - ``filtering`` -- the filter dropdown for the trasnsient listings toolbar
        """
        self.log.info('starting the ``_get_sort_dropdown`` method')

        from ..commonelements.sorting.ticket_table_sorting_dropdown import ticket_table_sorting_dropdown

        sort = ticket_table_sorting_dropdown(
            log=self.log,
            request=self.request,
            sortBy=self.qs["sortBy"],
            sortDesc=self.qs["sortDesc"]
        )

        from ..commonelements.filtering.ticket_table_filter_dropdown import ticket_table_filter_dropdown

        filtering = ticket_table_filter_dropdown(
            log=self.log,
            request=self.request,
            filterBy=self.qs["filterBy2"],
            filterValue=self.qs["filterValue2"],
            filterOp=self.qs["filterOp2"]
        )

        self.log.info('completed the ``_get_sort_dropdown`` method')
        return sort, filtering

    def _get_notification(
            self):
        """ get notification for the page

        **Key Arguments:**
            # -

        **Return:**
            - ``notification`` -- notifcation to append to the top of the transient listing page

        **Todo**
        """
        self.log.info('starting the ``_get_notification`` method')

        if "notification" in self.qs:
            notification = khufu.alert(
                alertText=self.qs["notification"],
                alertHeading='notification: ',
                extraPadding=False,
                # [ "warning" | "error" | "success" | "info" ]
                alertLevel='info'
            )
        else:
            notification = ""

        self.log.info('completed the ``_get_notification`` method')
        return notification

    def _get_pagination(
            self):
        """ get pagination for the page

        **Key Arguments:**
            # -

        **Return:**
            - ``pagination`` -- pagination options for the toolbar of the transient listing pages

        **Todo**
        """
        self.log.info('starting the ``_get_pagination`` method')

        from ..commonelements.pagination.ticket_table_pagination import ticket_table_pagination

        pagination = ticket_table_pagination(
            log=self.log,
            totalTickets=self.totalTicketCount,
            request=self.request,
            limit=self.qs["limit"],
            previousPageStart=self.qs["pageStart"]
        )

        self.log.info('completed the ``_get_pagination`` method')
        return pagination

    def _get_view_switcher_buttons(
            self):
        """ get view switcher buttons for the page

        **Key Arguments:**
            # -

        **Return:**
            - ``view_switcher_buttons`` -- the view switcher and download formats buttons with popovers

        **Todo**
        """
        self.log.info('starting the ``_get_view_switcher_buttons`` method')

        from ..commonelements.view_switcher_buttons import view_switcher_buttons

        if self.tcsCatalogueId:
            elementId = self.tcsCatalogueId
        else:
            elementId = self.elementId

        view_switcher_buttons = view_switcher_buttons(
            log=self.log,
            params=self.qs,
            request=self.request,
            elementId=elementId,
            tcsTableName=self.tcsCatalogueName
        )

        self.log.info('completed the ``_get_view_switcher_buttons`` method')
        return view_switcher_buttons

    def _get_ntt_view_button(
            self):
        """ get button that hides sources with dec > 30.

        **Key Arguments:**
            # -

        **Return:**
            - ``view_switcher_buttons`` -- the view switcher and download formats buttons with popovers

        **Todo**
        """
        self.log.info('starting the ``_get_ntt_view_button`` method')

        from ..commonelements.view_switcher_buttons import ntt_view_button

        if self.tcsCatalogueId:
            elementId = self.tcsCatalogueId
        else:
            elementId = self.elementId

        ntt_view_button = ntt_view_button(
            log=self.log,
            params=self.qs.copy(),
            elementId=elementId,
            request=self.request
        )

        self.log.info('completed the ``_get_ntt_view_button`` method')
        return ntt_view_button

    def _get_object_limit_dropdown(
            self):
        """ get object limit dropdown for the page

        **Key Arguments:**
            # -

        **Return:**
            - ``objectsPerPageDropdown`` -- options to display certain numbers of transients on a single webpage (for top toolbar of transient listing page)

        **Todo**
        """
        self.log.info('starting the ``_get_object_limit_dropdown`` method')

        from ..commonelements.sorting.number_of_objects_dropdown import number_of_objects_dropdown

        objectsPerPageDropdown = number_of_objects_dropdown(
            log=self.log,
            request=self.request,
            limit=self.qs["limit"],
            tableView=self.qs["format"]
        )

        self.log.info('completed the ``_get_object_limit_dropdown`` method')
        return objectsPerPageDropdown

    def _get_object_table(
            self):
        """get a table of transients

        **Key Arguments:**
            # -

        **Return:**
            - ``object_table`` -- the table view content for the transient listing pages

        **Todo**
        """
        self.log.info('starting the ``_get_object_table`` method')

        # assoicate the correct column name to mysql database column name
        tableColumnNames = {
            "observationPriority": "priority",
            "masterName": "name",
            "raDeg": "ra",
            "decDeg": "dec",
            "recentClassification": "spectral class",
            "currentMagnitude": "latest mag",
            "absolutePeakMagnitude": "abs peak mag",
            "best_redshift": "z",
            "distanceMpc": "mpc",
            "earliestDetection": "discovery date",
            "lastNonDetectionDate": "last non-detection date",
            "dateAdded": "added to marshall",
            "pi_name": "PI",
            "pi_email": "pi email"
        }

        # a list of names for table and csv views
        tableColumns = [
            "observationPriority",
            "masterName",
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
            "pi_name",
            "plainName"
        ]

        if "mwl" not in self.qs or self.qs["mwl"] not in ["pending observation", "following", "allObsQueue"]:
            tableColumns.remove("observationPriority")

        # get the webpage components
        # tickets = self._get_list_of_transient_tickets()
        sort, filtering = self._get_sort_dropdown()
        count = self.totalTicketCount
        pagination = self._get_pagination()
        ntt_button = self._get_ntt_view_button()
        viewSwitcherButtons = self._get_view_switcher_buttons()
        objectsPerPageDropdown = self._get_object_limit_dropdown()
        notification = self._get_notification()
        pageviewInfo = self._get_page_view_info()

        for obj in self.transientData:

            # convert priorities to words
            if "marshallWorkflowLocation" in obj:
                if obj["marshallWorkflowLocation"] == "following":
                    for n, w, c in zip([1, 2, 3, 4], ["CRITICAL", "IMPORTANT", "USEFUL", "NONE"], ["green", "yellow", "red", "blue"]):
                        if obj["observationPriority"] == n:
                            obj["observationPriority"] = w
                            # add text color
                            obj["observationPriority"] = khufu.coloredText(
                                text=obj["observationPriority"],
                                color=c,
                            )
                            break
                    obj["observationPriority"] = """<strong>""" + \
                        obj["observationPriority"] + """</strong>"""
                elif obj["marshallWorkflowLocation"] == "pending observation":
                    for n, w, c in zip([1, 2, 3], ["HIGH", "MEDIUM", "LOW"], ["green", "yellow", "red"]):
                        if obj["observationPriority"] == n:
                            obj["observationPriority"] = w
                            # add text color
                            obj["observationPriority"] = khufu.coloredText(
                                text=obj["observationPriority"],
                                color=c,
                            )
                            break
                    obj["observationPriority"] = """<strong>""" + \
                        obj["observationPriority"] + """</strong>"""

            # clean data in the obj dictionary
            # set name font sizes
            size = 3
            numerator = 30.
            if "mwl" not in self.qs or self.qs["mwl"] == "inbox":
                numerator = 40.
            test = int(numerator / len(obj["masterName"]))
            if test < 3:
                size = test

            # set icons for object names
            q = obj['marshallWorkflowLocation'].lower()
            icon = ""
            if q == "inbox":
                icon = """<i class="icon-inbox"></i>"""
            elif q == "review for followup":
                icon = """<i class="icon-eye"></i>"""
            elif q == "following":
                icon = """<i class="icon-pin"></i>"""
            elif q == "archive":
                icon = """<i class="icon-archive"></i>"""
            elif q == "pending observation":
                icon = """<i class="icon-target2"></i>"""
            elif q == "followup complete":
                icon = """<i class="icon-checkmark-circle"></i>"""
            thisName = khufu.a(
                content=obj["masterName"],
                href=obj["surveyObjectUrl"]
            )
            thisName = khufu.coloredText(
                text=obj["masterName"],
                color="green",
                size=size
            )
            icon = khufu.coloredText(
                text=icon,
                color="green",
                size=2,  # 1-10
                pull=False,  # "left" | "right"
            )
            obj["plainName"] = obj["masterName"]
            obj["masterName"] = "%(icon)s %(thisName)s" % locals()

            # set mailto links for pi
            if obj["pi_name"]:
                pi_name = obj["pi_name"]
                firstName = pi_name.split(' ', 1)[0]
                thisName = obj["plainName"]
                pi_email = obj["pi_email"]
                pi_name = khufu.a(
                    content="""%(pi_name)s&nbsp<i class="icon-mail7"></i>""" % locals(),
                    href="mailto:%(pi_email)s?subject=%(thisName)s&body=Hi %(firstName)s," % locals(
                    ),
                    tableIndex=False,
                    triggerStyle=False,  # [ False | "dropdown" | "tab" ],
                    htmlClass=False,
                    postInBackground=False
                )
                obj["pi_name"] = pi_name

        # create the sortable tables of objects
        table = khufu.tables.sortable_table.sortable_table(
            currentPageUrl=self.request.path_qs,
            columnsToDisplay=tableColumns,
            tableRowsDictionary=self.transientData,
            log=self.log,
            defaultSort="dateAdded"
        )
        nd = table.modifyDisplayNameDict
        nd["masterName"] = "name"
        nd["observationPriority"] = "priority"
        nd["raDeg"] = "ra"
        nd["decDeg"] = "dec"
        nd["recentClassification"] = "classification"
        nd["currentMagnitude"] = "latest mag"
        nd["absolutePeakMagnitude"] = "abs peak mag"
        nd["best_redshift"] = "z"
        nd["distanceMpc"] = "mpc"
        nd["earliestDetection"] = "discovery date"
        nd["lastNonDetectionDate"] = "last non-detection date"
        nd["dateAdded"] = "added to marshall"
        nd["pi_name"] = "pi"

        table.searchKeyAndColumn = ("search", "plainName")

        # hide columns depending on what list we are looking at
        if "mwl" not in self.qs or self.qs["mwl"] == "inbox":
            table.modifyColumnWidths = ["3", "1", "1", "2",
                                        "1", "1", "1", "1", "2", "2", "2", "2"]
            table.columnsToHide.append("recentClassification")
        table.columnsToHide.append("plainName")
        table = table.get()

        # create the table function bar
        space = "&nbsp" * 10
        smallspace = "&nbsp" * 1

        pageviewInfo = khufu.p(
            content=pageviewInfo,
            lead=False,
            textAlign="right",  # [ left | center | right ]
            color=False,  # [ muted | warning | info | error | success ]
            navBar=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        ticketTableFunctionBar = khufu.navBar(
            brand='',
            contentList=[viewSwitcherButtons, ntt_button, smallspace, filtering,
                         objectsPerPageDropdown, smallspace, space, pagination],
            contentListPull="right",
            dividers=False,
            forms=False,
            fixedOrStatic=False,
            location='top',
            responsive=False,
            dark=False,
            transparent=True
        )
        bottomTicketTableFunctionBar = ticketTableFunctionBar.replace(
            "btn-group", "btn-group dropup")
        dynamicNotification = """<span id="dynamicNotification"></span>"""
        object_table = khufu.grid_column(
            span=12,  # 1-12
            offset=0,  # 1-12
            content="""%(dynamicNotification)s %(notification)s %(ticketTableFunctionBar)s %(pageviewInfo)s %(table)s %(bottomTicketTableFunctionBar)s""" % locals(
            ),
            htmlId="object_table",
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        self.log.info('completed the ``_get_object_table`` method')
        return object_table

    def _get_page_name(
            self):
        """ get page name

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
        """
        self.log.info('starting the ``_get_page_name`` method')

        thisPageName = ""
        if "snoozed" in self.qs:
            thisPageName = "snoozed"
        elif "cf" in self.qs and (self.qs["cf"] == 1 or self.qs["cf"] == "1"):
            thisPageName = "classified"
        elif "awl" in self.qs:
            thisPageName = self.qs["awl"]
        elif "mwl" in self.qs:
            thisPageName = self.qs["mwl"]

        self.log.info('completed the ``_get_page_name`` method')
        return thisPageName

    def _get_object_tickets(
            self):
        """ get object tickets

        **Return:**
            - ``ticket_table`` -- the ticket to display as the main content of the page

        **Todo**
        """
        self.log.info('starting the ``_get_object_tickets`` method')

        # get the webpage components
        ticketList = self._get_list_of_transient_tickets()
        pagination = self._get_pagination()
        notification = self._get_notification()
        ticketsPerPageDropdown = self._get_object_limit_dropdown()
        ntt_button = self._get_ntt_view_button()
        view_switcher_buttons = self._get_view_switcher_buttons()

        sort, filtering = self._get_sort_dropdown()
        pageviewInfo = self._get_page_view_info()

        theseTickets = ""
        for ticket in ticketList:
            theseTickets = "%(theseTickets)s%(ticket)s" % locals()

        space = "&nbsp" * 10
        smallspace = "&nbsp" * 1

        ticketTableFunctionBar = khufu.navBar(
            brand='',
            contentList=[view_switcher_buttons, ntt_button, smallspace, sort, filtering, smallspace,
                         ticketsPerPageDropdown, smallspace, space, pagination],
            contentListPull="right",
            dividers=False,
            forms=False,
            fixedOrStatic=False,
            location='top',
            responsive=False,
            dark=False,
            transparent=True
        )

        pageviewInfo = khufu.p(
            content=pageviewInfo,
            lead=False,
            textAlign="right",  # [ left | center | right ]
            color=False,  # [ muted | warning | info | error | success ]
            navBar=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        bottomTicketTableFunctionBar = ticketTableFunctionBar.replace(
            "btn-group", "btn-group dropup").replace("""data-placement="bottom" """, """data-placement="top" """)

        dynamicNotification = """<span id="dynamicNotification"></span>"""

        ticket_table = khufu.grid_column(
            span=12,  # 1-12
            offset=0,  # 1-12
            content="""%(dynamicNotification)s %(notification)s %(ticketTableFunctionBar)s %(pageviewInfo)s  %(theseTickets)s %(bottomTicketTableFunctionBar)s""" % locals(
            ),
            htmlId="ticket_table",
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        self.log.info('completed the ``_get_object_tickets`` method')
        return ticket_table

    # use the tab-trigger below for new method
    def _get_page_view_info(
            self):
        """ get page view info

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_page_view_info method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_get_page_view_info`` method')

        # craft some text from the download filename
        filename = self.qs["filename"]

        thisListing = filename.replace("pessto_marshall", "").replace(
            "_", " ").strip()

        limit = int(self.qs["limit"])
        pageStart = int(self.qs["pageStart"]) + 1
        pageEnd = pageStart + limit - 1
        totalCount = int(self.totalTicketCount)
        if pageEnd > totalCount:
            pageEnd = totalCount

        filterText1 = self.qs["filterText1"]
        filterText2 = self.qs["filterText2"]

        tcsCatalogueId = self.tcsCatalogueId
        if self.tcsCatalogueName:
            table_name = self.tcsCatalogueName
            if "tcsRank" in self.qs:
                matches = "top-ranked matches"
            else:
                matches = "matched"

            if totalCount == 0:
                thisListing = """<span id="pageinfo">no transients were found matched against the <strong>%(table_name)s</strong> catalogue<span>""" % locals(
                )
            else:
                thisListing = """<span id="pageinfo">showing transients <strong>%(pageStart)s-%(pageEnd)s</strong> of <strong>%(totalCount)s</strong> %(matches)s against the <strong>%(table_name)s</strong> catalogue<span>""" % locals(
                )
        elif "search" in thisListing:
            thisListing = thisListing.replace("search", "").strip()
            if totalCount == 0:
                thisListing = """<span id="pageinfo">no transients were found in the search for "<strong><em>%(thisListing)s</em></strong>"<span>""" % locals(
                )
            else:
                thisListing = """<span id="pageinfo">showing transients <strong>%(pageStart)s-%(pageEnd)s</strong> of <strong>%(totalCount)s</strong> from the search for "<strong><em>%(thisListing)s</em></strong>"<span>""" % locals(
                )
        elif "search" not in thisListing:
            if totalCount == 0:
                thisListing = """<span id="pageinfo">no transients were found %(filterText1)s%(filterText2)sin the <strong>%(thisListing)s</strong> list<span>""" % locals(
                )
            else:
                thisListing = """<span id="pageinfo">showing transients <strong>%(pageStart)s-%(pageEnd)s</strong> of <strong>%(totalCount)s</strong> %(filterText1)s%(filterText2)sin the <strong>%(thisListing)s</strong> list<span>""" % locals(
                )

        else:
            thisListing = ""

        self.log.info('completed the ``_get_page_view_info`` method')
        return thisListing

    # use the tab-trigger below for new method
    # xt-class-method
