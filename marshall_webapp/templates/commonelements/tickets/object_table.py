#!/usr/local/bin/python
# encoding: utf-8
"""
object_table.py
===============
:Summary:
    The block containing the tables and the toolbars associated with them

:Author:
    David Young

:Date Created:
    November 20, 2013

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import datetime
import re
from docopt import docopt
from dryxPython import commonutils as dcu
import khufu
import khufu.tables.sortable_table as sortable_table

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : November 20, 2013
# CREATED : November 20, 2013
# AUTHOR : DRYX


def object_table(
    log,
    objectData,
    pagination=False,
    notification=False,
    objectsPerPageDropdown=False,
    view_switcher_buttons=False,
    tableColumnNames=False,
    tableColumns=False,
    downloadButton=False,
    thisUrl=False,
):
    """create object_table

    **Key Arguments:**
        - ``log`` -- logger
        - ``objectData`` -- list of object data dictionaries
        - ``objectsPerPageDropdown`` -- dropdown to select number of tickets / page
        - ``notification`` -- some alert for the user
        - ``thisUrl`` -- the url of this webpage
        - ``view_switcher_buttons`` -- view switcher buttons
        - ``tableColumnNames`` -- the table columns to be displayed - name / mysql name dictionary
        - ``tableColumns`` -- the table columns to be displayed
        - ``downloadButton`` -- download current marshall view

    **Return:**
        - ``object_table``
    """
    tableColumns.append("plainName")

    # set default values
    if notification is False:
        notification = ""
    if downloadButton is False:
        downloadButton = ""
    if pagination is False:
        pagination = ""
    if objectsPerPageDropdown is False:
        objectsPerPageDropdown = ""
    if view_switcher_buttons is False:
        view_switcher_buttons = ""

    for obj in objectData:

        # clean data in the obj dictionary
        # set name font sizes
        size = 3
        numerator = 30.
        if "mwl" not in thisUrl or "mwl=inbox" in thisUrl:
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
    table = sortable_table.sortable_table(
        currentPageUrl=thisUrl,
        columnsToDisplay=tableColumns,
        tableRowsDictionary=objectData,
        log=log,
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
    if "mwl" not in thisUrl or "inbox" in thisUrl:
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
        contentList=[view_switcher_buttons, smallspace,
                     objectsPerPageDropdown, smallspace, downloadButton, space, pagination],
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

    return """%(object_table)s""" % locals()

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
