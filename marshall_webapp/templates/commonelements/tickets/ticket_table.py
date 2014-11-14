#!/usr/local/bin/python
# encoding: utf-8
"""
ticket_table.py
===============
:Summary:
    The block containing the tables and the toolbars associated with them

:Author:
    David Young

:Date Created:
    November 20, 2013

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import commonutils as dcu

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : November 20, 2013
# CREATED : November 20, 2013
# AUTHOR : DRYX


def ticket_table(
    log,
    ticketList=[],
    pagination=False,
    notification=False,
    ticketsPerPageDropdown=False,
    view_switcher_buttons=False,
    downloadButton=False,
    sort=False
):
    """create ticket_table

    **Key Arguments:**
        - ``log`` -- logger
        - ``ticketList`` -- a list of tickets to display on this page
        - ``ticketsPerPageDropdown`` -- dropdown to select number of tickets / page
        - ``notification`` -- some alert for the user
        - ``downloadButton`` -- download current marshall view

    **Return:**
        - ``ticket_table``

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    if notification is False:
        notification = ""

    theseTickets = ""
    for ticket in ticketList:
        theseTickets = "%(theseTickets)s%(ticket)s" % locals()

    if pagination is False:
        pagination = ""

    if sort is False:
        sort = ""

    if downloadButton is False:
        downloadButton = ""

    if view_switcher_buttons is False:
        view_switcher_buttons = ""

    if ticketsPerPageDropdown is False:
        ticketsPerPageDropdown = ""

    space = "&nbsp" * 10
    smallspace = "&nbsp" * 1

    ticketTableFunctionBar = khufu.navBar(
        brand='',
        contentList=[view_switcher_buttons, smallspace, sort, smallspace,
                     ticketsPerPageDropdown, smallspace, downloadButton, space, pagination],
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

    return """%(ticket_table)s""" % locals()

# use the tab-trigger below for new function
# x-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

############################################
# CODE TO BE DEPECIATED                    #
############################################

if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
