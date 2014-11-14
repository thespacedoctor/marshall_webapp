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
    @review: when complete pull all general functions and classes into dryxPython
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
        - ``search`` -- is this a search?

    **Todo**
        - @review: when complete, clean templates_transients class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

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

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        transientModal = models_transients_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId,
            search=self.search
        )
        self.qs, self.transientData, self.transientAkas, self.transientLightcurveData, self.transientAtelMatches, self.transientComments, self.totalTicketCount = transientModal.get(
        )

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the templates_transients object

        **Return:**
            - ``templates_transients``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

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
            - None

        **Todo**
            - @review: when complete, clean _get_list_of_transient_tickets method
            - @review: when complete add logging
        """
        from ..commonelements.tickets.single_ticket import single_ticket

        self.log.info('starting the ``_get_list_of_transient_tickets`` method')

        ticketList = []
        for discoveryDataDictionary in self.transientData:
            transientBucketId = discoveryDataDictionary["transientBucketId"]

            thisTicket = single_ticket(
                log=self.log,
                request=self.request,
                discoveryDataDictionary=discoveryDataDictionary,
                objectComments=self.transientComments,
                objectAkas=self.transientAkas,
                lightcurveData=self.transientLightcurveData,
                atelData=self.transientAtelMatches,
            )
            ticketList.append(thisTicket)

        self.log.info('completed the ``_get_list_of_transient_tickets`` method')
        return ticketList

    # use the tab-trigger below for new method
    def _get_sort_dropdown(
            self):
        """ get sort dropdown

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_sort_dropdown method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_get_sort_dropdown`` method')

        from ..commonelements.sorting.ticket_table_sorting_dropdown import ticket_table_sorting_dropdown

        sort = ticket_table_sorting_dropdown(
            log=self.log,
            thisUrl=self.request.url,
            sortBy=self.qs["sortBy"],
            sortDesc=self.qs["sortDesc"]
        )

        self.log.info('completed the ``_get_sort_dropdown`` method')
        return sort

    # use the tab-trigger below for new method
    def _get_notification(
            self):
        """ get notification for the page

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_notification method
            - @review: when complete add logging
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

    # use the tab-trigger below for new method
    def _get_pagination(
            self):
        """ get pagination for the page

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_pagination method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_get_pagination`` method')

        from ..commonelements.pagination.ticket_table_pagination import ticket_table_pagination

        pagination = ticket_table_pagination(
            log=self.log,
            totalTickets=self.totalTicketCount,
            thisUrl=self.request.url,
            limit=self.qs["limit"],
            previousPageStart=self.qs["pageStart"]
        )

        self.log.info('completed the ``_get_pagination`` method')
        return pagination

    # use the tab-trigger below for new method
    def _get_view_switcher_buttons(
            self):
        """ get view switcher buttons for the page

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_view_switcher_buttons method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_get_view_switcher_buttons`` method')

        from ..commonelements.view_switcher_buttons import view_switcher_buttons

        view_switcher_buttons = view_switcher_buttons(
            log=self.log,
            params=self.qs,
            request=self.request
        )

        self.log.info('completed the ``_get_view_switcher_buttons`` method')
        return view_switcher_buttons

    # use the tab-trigger below for new method
    def _get_object_limit_dropdown(
            self):
        """ get object limit dropdown for the page

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_object_limit_dropdown method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_get_object_limit_dropdown`` method')

        from ..commonelements.sorting.number_of_objects_dropdown import number_of_objects_dropdown

        objectsPerPageDropdown = number_of_objects_dropdown(
            log=self.log,
            thisUrl=self.request.url,
            limit=self.qs["limit"],
            tableView=self.qs["format"]
        )

        self.log.info('completed the ``_get_object_limit_dropdown`` method')
        return objectsPerPageDropdown

    # use the tab-trigger below for new method
    def _get_object_table(
            self):
        """get a table of transients

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_object_table method
            - @review: when complete add logging
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

        tickets = self._get_list_of_transient_tickets()
        sort = self._get_sort_dropdown()
        count = self.totalTicketCount
        pagination = self._get_pagination()
        viewSwitcherButtons = self._get_view_switcher_buttons()
        objectsPerPageDropdown = self._get_object_limit_dropdown()
        notification = self._get_notification()

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
            currentPageUrl=self.request.url,
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
            contentList=[viewSwitcherButtons, smallspace,
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

    # use the tab-trigger below for new method
    def _get_page_name(
            self):
        """ get page name

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _get_page_name method
            - @review: when complete add logging
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

    # use the tab-trigger below for new method
    def _get_object_tickets(
            self):
        """ get object tickets

        **Return:**
            - ``ticket_table`` -- the ticket to display as the main content of the page

        **Todo**
            - @review: when complete, clean _get_object_tickets method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_get_object_tickets`` method')

        ticketList = self._get_list_of_transient_tickets()
        pagination = self._get_pagination()
        notification = self._get_notification()
        ticketsPerPageDropdown = self._get_object_limit_dropdown()
        view_switcher_buttons = self._get_view_switcher_buttons()
        sort = self._get_sort_dropdown()

        theseTickets = ""
        for ticket in ticketList:
            theseTickets = "%(theseTickets)s%(ticket)s" % locals()

        space = "&nbsp" * 10
        smallspace = "&nbsp" * 1

        ticketTableFunctionBar = khufu.navBar(
            brand='',
            contentList=[view_switcher_buttons, smallspace, sort, smallspace,
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
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
