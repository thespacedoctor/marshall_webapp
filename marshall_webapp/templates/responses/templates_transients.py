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
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import yaml
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

    **Todo**
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
        log.debug("instansiating a new 'templates_transients' object")
        self.elementId = elementId
        self.search = search
        # xt-self-arg-tmpx

        # grab the required data from the database and add it as attributes to
        # this object
        transientModal = models_transients_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId,
            search=self.search
        )
        self.qs, self.transientData, self.transientAkas, self.transientLightcurveData, self.transientAtelMatches, self.transients_comments, self.totalTicketCount = transientModal.get(
        )

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

        webpage = defaultpagetemplate(
            log=self.log,
            request=self.request,
            bodyId=False,
            pageTitle="PESSTO Marshall",
            topNavBar=False,
            sideBar=False,
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

        self.log.info('starting the ``_get_list_of_transient_tickets`` method')

        # for each transient build a ticket to be presented in the browser
        ticketList = []
        for discoveryDataDictionary in self.transientData:
            transientBucketId = discoveryDataDictionary["transientBucketId"]
            observationPriority = discoveryDataDictionary["observationPriority"]

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
            )
            ticketList.append(thisTicket)

        self.log.info('completed the ``_get_list_of_transient_tickets`` method')
        return ticketList

    def _get_sort_dropdown(
            self):
        """ get sort dropdown

        **Key Arguments:**
            # -

        **Return:**
            - ``sort`` -- the sort dropdown for the transient listings toolbar

        **Todo**
        """
        self.log.info('starting the ``_get_sort_dropdown`` method')

        from ..commonelements.sorting.ticket_table_sorting_dropdown import ticket_table_sorting_dropdown

        sort = ticket_table_sorting_dropdown(
            log=self.log,
            request=self.request,
            sortBy=self.qs["sortBy"],
            sortDesc=self.qs["sortDesc"]
        )

        self.log.info('completed the ``_get_sort_dropdown`` method')
        return sort

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

        view_switcher_buttons = view_switcher_buttons(
            log=self.log,
            params=self.qs,
            request=self.request,
            elementId=self.elementId
        )

        self.log.info('completed the ``_get_view_switcher_buttons`` method')
        return view_switcher_buttons

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
            "masterName": "name",
            "raDeg": "ra",
            "decDeg": "dec",
            "recentClassification": "spectral class",
            "transientTypePrediction": "prediction",
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

        # get the webpage components
        tickets = self._get_list_of_transient_tickets()
        sort = self._get_sort_dropdown()
        count = self.totalTicketCount
        pagination = self._get_pagination()
        viewSwitcherButtons = self._get_view_switcher_buttons()
        objectsPerPageDropdown = self._get_object_limit_dropdown()
        notification = self._get_notification()
        pageviewInfo = self._get_page_view_info()

        for obj in self.transientData:

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
        nd["raDeg"] = "ra"
        nd["decDeg"] = "dec"
        nd["recentClassification"] = "classification"
        nd["transientTypePrediction"] = "prediction"
        nd["currentMagnitude"] = "latest mag"
        nd["absolutePeakMagnitude"] = "abs peak mag"
        nd["best_redshift"] = "z"
        nd["distanceMpc"] = "mpc"
        nd["earliestDetection"] = "discovery date"
        nd["lastNonDetectionDate"] = "last non-detection date"
        nd["dateAdded"] = "added to marshall"
        nd["pi_name"] = "pi"

        table.searchKeyAndColumn = ("searchString", "plainName")

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
        ticketTableFunctionBar = khufu.navBar(
            brand='',
            contentList=[pageviewInfo, viewSwitcherButtons, smallspace,
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
            content="""%(dynamicNotification)s %(notification)s %(ticketTableFunctionBar)s %(table)s %(bottomTicketTableFunctionBar)s""" % locals(
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
        if "mwl" in self.qs:
            thisPageName = self.qs["mwl"]
        elif "awl" in self.qs:
            thisPageName = self.qs["awl"]
        elif "cf" in self.qs and (self.qs["cf"] == 1 or self.qs["cf"] == "1"):
            thisPageName = "classified"

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
        view_switcher_buttons = self._get_view_switcher_buttons()
        sort = self._get_sort_dropdown()
        pageviewInfo = self._get_page_view_info()

        theseTickets = ""
        for ticket in ticketList:
            theseTickets = "%(theseTickets)s%(ticket)s" % locals()

        space = "&nbsp" * 10
        smallspace = "&nbsp" * 1

        ticketTableFunctionBar = khufu.navBar(
            brand='',
            contentList=[pageviewInfo, view_switcher_buttons, smallspace, sort, smallspace,
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

        bottomTicketTableFunctionBar = ticketTableFunctionBar.replace(
            "btn-group", "btn-group dropup").replace("""data-placement="bottom" """, """data-placement="top" """)

        dynamicNotification = """<span id="dynamicNotification"></span>"""

        ticket_table = khufu.grid_column(
            span=12,  # 1-12
            offset=0,  # 1-12
            content="""%(dynamicNotification)s %(notification)s %(ticketTableFunctionBar)s %(theseTickets)s %(bottomTicketTableFunctionBar)s""" % locals(
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

        #
        limit = int(self.qs["limit"])
        pageStart = int(self.qs["pageStart"]) + 1
        pageEnd = pageStart + limit - 1
        totalCount = int(self.totalTicketCount)
        if pageEnd > totalCount:
            pageEnd = totalCount

        if "search" not in thisListing:
            if totalCount == 0:
                thisListing = """<span id="pageinfo">no transients were found in the <strong>%(thisListing)s</strong> list<span>""" % locals(
                )
            else:
                thisListing = """<span id="pageinfo">showing transients <strong>%(pageStart)s-%(pageEnd)s</strong> of <strong>%(totalCount)s</strong> in the <strong>%(thisListing)s</strong> list<span>""" % locals(
                )
        elif "search" in thisListing:
            thisListing = thisListing.replace("search", "").strip()
            if totalCount == 0:
                thisListing = """<span id="pageinfo">no transients were found in the search for "<strong><em>%(thisListing)s</em></strong>"<span>""" % locals(
                )
            else:
                thisListing = """<span id="pageinfo">showing transients <strong>%(pageStart)s-%(pageEnd)s</strong> of <strong>%(totalCount)s</strong> from the search for "<strong><em>%(thisListing)s</em></strong>"<span>""" % locals(
                )

        else:
            thisListing = ""

        self.log.info('completed the ``_get_page_view_info`` method')
        return thisListing

    # use the tab-trigger below for new method
    # xt-class-method
