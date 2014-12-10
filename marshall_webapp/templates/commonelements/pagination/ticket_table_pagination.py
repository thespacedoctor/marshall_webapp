#!/usr/local/bin/python
# encoding: utf-8
"""
ticket_table_pagination.py
==========================
:Summary:
    The pagintation for pages displaying a ticket table

:Author:
    David Young

:Date Created:
    January 9, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import math
from docopt import docopt
import khufu
from dryxPython import commonutils as dcu


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 9, 2014
# CREATED : January 9, 2014
# AUTHOR : DRYX


def ticket_table_pagination(
        log,
        totalTickets,
        request,
        limit,
        previousPageStart,
        numberOfButtonsToDisplay=5
):
    """ticket_table_pagination

    **Key Arguments:**
        - ``log`` -- the logger
        - ``totalTickets`` -- the total number of tickets to be listed in pagination
        - ``request`` -- the request
        - ``limit`` -- the limit of tickets to display on the page
        - ``previousPageStart`` -- the index of the previous page's first ticket
        - ``numberOfButtonsToDisplay`` -- the total number of pagination buttons to display on any one page (must be odd number)

    **Return:**
        - ``pagination`` -- the pagination to be displayed

    **Todo**
    """
    routename = request.matched_route.name
    if "elementId" in request.matchdict:
        elementId = request.matchdict["elementId"]
    else:
        elementId = False

    theseParams = dict(request.params)
    alist = ["limit", "pageStart"]
    for i in alist:
        if i in theseParams:
            del theseParams[i]

    # STRIP THE URL OF PREVIOUS PAGINATION SETTINGS
    # thisUrl = re.sub(r"(&|\?)limit=\d*", "", thisUrl)
    # thisUrl = re.sub(r"(&|\?)pageStart=\d*", "", thisUrl)
    # APPEND THE RELEVANT SYMBOL AT END OF NEW URL
    # beginUrlWith = "&"
    # if "?" not in thisUrl:
    #     beginUrlWith = "?"
    # PLACE VARIABLES IN CORRECT FORMAT
    limit = float(limit)
    previousPageStart = float(previousPageStart)
    # CALULATE OTHER VARIABLES
    totalButtons = int(math.ceil(totalTickets * 1. / limit))
    thisButtonIndex = int(math.ceil(previousPageStart / limit)) + 1
    previousPageStart = int(
        math.floor((previousPageStart - 1.) / limit)) * limit
    # CALULATE THE GENERAL RANGE OF THE BUTTONS TO DISPLAY
    displayRangeStart = thisButtonIndex - 1 - int(numberOfButtonsToDisplay / 2)
    displayRangeEnd = thisButtonIndex + int(numberOfButtonsToDisplay / 2)

    numberOfButtonsBeforeThis = thisButtonIndex - 1
    numberOfButtonsAfterThis = totalButtons - thisButtonIndex
    if numberOfButtonsBeforeThis < numberOfButtonsToDisplay / 2:
        displayRangeStart = 0
        displayRangeEnd = numberOfButtonsToDisplay
    if numberOfButtonsAfterThis <= numberOfButtonsToDisplay / 2:
        displayRangeEnd = totalButtons
        if numberOfButtonsBeforeThis > numberOfButtonsToDisplay / 2:
            displayRangeStart = totalButtons - numberOfButtonsToDisplay + \
                int(numberOfButtonsAfterThis / 2 - 0.5)

    if displayRangeStart < 0:
        displayRangeStart = 0
    if displayRangeEnd > totalButtons:
        displayRangeEnd = totalButtons

    limit = int(limit)
    allButtons = ""
    pageStart = (thisButtonIndex) * limit
    theseParams["limit"] = limit
    theseParams["pageStart"] = pageStart
    nextButtonUrl = request.route_path(
        routename, elementId=elementId, _query=theseParams)
    disabled = False
    if thisButtonIndex == totalButtons:
        disabled = True
    nextButton = khufu.a(
        content="&raquo;",
        href=nextButtonUrl,
        tableIndex=-1,
    )
    nextButton = khufu.li(
        content=nextButton,  # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=disabled
    )
    pageStart = (thisButtonIndex - 2) * limit
    theseParams["limit"] = limit
    theseParams["pageStart"] = pageStart
    prevButtonUrl = request.route_path(
        routename, elementId=elementId, _query=theseParams)
    disabled = False
    if thisButtonIndex == 1:
        disabled = True
    prevButton = khufu.a(
        content="&laquo;",
        href=prevButtonUrl,
        tableIndex=-1
    )
    prevButton = khufu.li(
        content=prevButton,  # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=disabled
    )

    for i in range(displayRangeStart, displayRangeEnd):
        buttonNumber = i + 1
        disabled = False
        if buttonNumber == thisButtonIndex:
            disabled = True
        pageStart = i * limit
        theseParams["limit"] = limit
        theseParams["pageStart"] = pageStart
        buttonUrl = request.route_path(
            routename, elementId=elementId, _query=theseParams)
        link = khufu.a(
            content=buttonNumber,
            href=buttonUrl,
            tableIndex=-1
        )
        linkListItem = khufu.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=disabled
        )
        allButtons = """%(allButtons)s%(linkListItem)s""" % locals()

    allButtons = """%(prevButton)s%(allButtons)s%(nextButton)s""" % locals()

    pagination = khufu.pagination(
        listItems=allButtons,
        size='default',
        align=False
    )

    return pagination

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
