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
# LAST MODIFIED : January 9, 2014
# CREATED : January 9, 2014
# AUTHOR : DRYX


def ticket_table_pagination(
        log,
        totalTickets,
        thisUrl,
        limit,
        previousPageStart,
        numberOfButtonsToDisplay=5
):
    """ticket_table_pagination

    **Key Arguments:**
        - ``log`` -- the logger
        - ``totalTickets`` -- the total number of tickets to be listed in pagination
        - ``thisUrl`` -- the current url
        - ``limit`` -- the limit of tickets to display on the page
        - ``previousPageStart`` -- the index of the previous page's first ticket
        - ``numberOfButtonsToDisplay`` -- the total number of pagination buttons to display on any one page (must be odd number)

    **Return:**
        - ``pagination`` -- the pagination to be displayed

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    import math
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    # STRIP THE URL OF PREVIOUS PAGINATION SETTINGS
    thisUrl = re.sub(r"(&|\?)limit=\d*", "", thisUrl)
    thisUrl = re.sub(r"(&|\?)pageStart=\d*", "", thisUrl)
    # APPEND THE RELEVANT SYMBOL AT END OF NEW URL
    beginUrlWith = "&"
    if "?" not in thisUrl:
        beginUrlWith = "?"
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
    nextButtonUrl = """%(thisUrl)s%(beginUrlWith)slimit=%(limit)s&pageStart=%(pageStart)s""" % locals(
    )
    nextButtonUrl = nextButtonUrl.replace("index.py&", "index.py?")
    disabled = False
    if thisButtonIndex == totalButtons:
        disabled = True
    nextButton = khufu.a(
        content="&raquo;",
        href=nextButtonUrl,
        tableIndex=-1,
        triggerStyle=False  # [ False | "dropdown" | "tab" ]
    )
    nextButton = khufu.li(
        content=nextButton,  # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=disabled,
        submenuTitle=False,
        divider=False,
        navStyle=False,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )
    pageStart = (thisButtonIndex - 2) * limit
    prevButtonUrl = """%(thisUrl)s%(beginUrlWith)slimit=%(limit)s&pageStart=%(pageStart)s""" % locals(
    )
    prevButtonUrl = prevButtonUrl.replace("index.py&", "index.py?")
    disabled = False
    if thisButtonIndex == 1:
        disabled = True
    prevButton = khufu.a(
        content="&laquo;",
        href=prevButtonUrl,
        tableIndex=-1,
        triggerStyle=False  # [ False | "dropdown" | "tab" ]
    )
    prevButton = khufu.li(
        content=prevButton,  # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=disabled,
        submenuTitle=False,
        divider=False,
        navStyle=False,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    for i in range(displayRangeStart, displayRangeEnd):
        buttonNumber = i + 1
        disabled = False
        if buttonNumber == thisButtonIndex:
            disabled = True
        pageStart = i * limit
        buttonUrl = """%(thisUrl)s%(beginUrlWith)slimit=%(limit)s&pageStart=%(pageStart)s""" % locals(
        )
        link = khufu.a(
            content=buttonNumber,
            href=buttonUrl,
            tableIndex=-1,
            triggerStyle=False  # [ False | "dropdown" | "tab" ]
        )
        linkListItem = khufu.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=disabled,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        allButtons = """%(allButtons)s%(linkListItem)s""" % locals()

    allButtons = """%(prevButton)s%(allButtons)s%(nextButton)s""" % locals()

    pagination = khufu.pagination(
        listItems=allButtons,
        size='default',
        align=False
    )

    return pagination

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
