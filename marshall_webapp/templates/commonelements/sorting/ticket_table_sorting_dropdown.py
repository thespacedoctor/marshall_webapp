#!/usr/local/bin/python
# encoding: utf-8
"""
ticket_table_sorting_dropdown.py
============================
:Summary:
    The sort dropdown used to sort the tickets displayed in the marshall

:Author:
    David Young

:Date Created:
    January 22, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
from docopt import docopt
import khufu
from dryxPython import commonutils as dcu

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 22, 2014
# CREATED : January 22, 2014
# AUTHOR : DRYX


def ticket_table_sorting_dropdown(
    log,
    request,
    sortBy=False,
    sortDesc=False
):
    """ticket_table_sorting_dropdown

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the request
        - ``sortBy`` -- the incoming sortBy
        - ``sortDesc`` -- incoming sort direction

    **Return:**
        - ``sortDropdown`` -- the sort dropdown for the transient listing pages

    **Todo**
    """
    routename = request.matched_route.name
    if "elementId" in request.matchdict:
        elementId = request.matchdict["elementId"]
    else:
        elementId = False

    theseParams = dict(request.params)
    alist = ["sortBy", "sortDesc"]
    for i in alist:
        if i in theseParams:
            del theseParams[i]

    # thisUrl = re.sub(r"(\&|\?)sortBy=[a-zA-Z_]*", "", thisUrl)
    # thisUrl = re.sub(r"(\&|\?)sortDesc=[a-zA-Z]*", "", thisUrl)
    # thisUrl = re.sub(r"(\&|\?)=\d*", "", thisUrl)
    # thisUrl = re.sub(r"(\&|\?)pageStart=\d*", "", thisUrl)
    # thisUrl = re.sub(r"index.py&", "index.py?", thisUrl)
    # if thisUrl[-3:] == ".py":
    #     thisUrl = "%(thisUrl)s?" % locals()
    # elif thisUrl[-1:] not in ["?", "&"]:
    #     thisUrl = "%(thisUrl)s&" % locals()

    # GENERATE THE SORT OPTION LIST
    optionList = [
        "ra",
        "dec",
        "name",
        "date added to marshall",
        "date of last observation",
        "discovery date",
        "predicted type",
        "pre-discovery non-detection date",
        "absolute peak magnitude",
        "spectral type",
        "classification date",
        "redshift",
        "latest comment date",
        "current magnitude",
        "pi",
        "priority"
    ]

    # remove options not available for inbox items
    if "mwl" not in theseParams or theseParams["mwl"] == "inbox":
        optionList.remove("classification date")
        optionList.remove("spectral type")
        optionList.remove("pi")

    if "mwl" not in theseParams or theseParams["mwl"] not in ["pending observation", "allObsQueue", "following"]:
        optionList.remove("priority")

    dbSortBy = sortBy
    if sortBy == "raDeg":
        sortBy = "ra"
    if sortBy == "decDeg":
        sortBy = "dec"
    if sortBy == "masterName":
        sortBy = "name"
    if sortBy == "dateAdded":
        sortBy = "date added to marshall"
    if sortBy == "currentMagnitudeDate":
        sortBy = "date of last observation"
    if sortBy == "earliestDetection":
        sortBy = "discovery date"
    if sortBy == "transientTypePrediction":
        sortBy = "predicted type"
    if sortBy == "lastNonDetectionDate":
        sortBy = "pre-discovery non-detection date"
    if sortBy == "absolutePeakMagnitude":
        sortBy = "absolute peak magnitude"
    if sortBy == "spectralType" or sortBy == "recentClassification":
        sortBy = "spectral type"
    if sortBy == "classificationDate":
        sortBy = "classification date"
    if sortBy == "redshift":
        sortBy = "redshift"
    if sortBy == "latestComment":
        sortBy = "latest comment date"
    if sortBy == "currentMagnitude":
        sortBy = "current magnitude"
    if sortBy == "pi_name":
        sortBy = "pi"
    if sortBy == "observationPriority":
        sortBy = "priority"

    optionList = sorted(optionList)
    if sortBy:
        try:
            optionList.remove(sortBy)
        except:
            pass

    # add links to options
    linkList = []
    for option in optionList:
        if option == "ra":
            dbOption = "raDeg"
        if option == "dec":
            dbOption = "decDeg"
        if option == "name":
            dbOption = "masterName"
        if option == "date added to marshall":
            dbOption = "dateAdded"
        if option == "date of last observation":
            dbOption = "currentMagnitudeDate"
        if option == "discovery date":
            dbOption = "earliestDetection"
        if option == "predicted type":
            dbOption = "transientTypePrediction"
        if option == "pre-discovery non-detection date":
            dbOption = "lastNonDetectionDate"
        if option == "absolute peak magnitude":
            dbOption = "absolutePeakMagnitude"
        if option == "spectral type":
            dbOption = "recentClassification"
        if option == "classification date":
            dbOption = "classificationDate"
        if option == "redshift":
            dbOption = "redshift"
        if option == "latest comment date":
            dbOption = "latestComment"
        if option == "current magnitude":
            dbOption = "currentMagnitude"
        if option == "pi":
            dbOption = "pi_name"
        if option == "priority":
            dbOption = "observationPriority"

        theseParams["sortBy"] = dbOption
        theseParams["sortDesc"] = False

        thisLink = request.route_path(
            routename, elementId=elementId, _query=theseParams)
        thisLink = khufu.a(
            content=option,
            href=thisLink,
        )
        thisLink = khufu.li(
            content=thisLink,  # if a subMenu for dropdown this should be <ul>
        )
        linkList.append(thisLink)

    # set sort arrow direction
    if sortDesc != "True":
        arrow = """<i class="icon-arrow-down4"></i>"""
        theseParams["sortBy"] = dbSortBy
        theseParams["sortDesc"] = True
        topButtonLink = request.route_path(
            routename, elementId=elementId, _query=theseParams)
    else:
        arrow = """<i class="icon-arrow-up4"></i>"""
        theseParams["sortBy"] = dbSortBy
        theseParams["sortDesc"] = False
        topButtonLink = request.route_path(
            routename, elementId=elementId, _query=theseParams)

    # add text color
    arrow = khufu.coloredText(
        text=arrow,
        color="red",
        size=False,  # 1-10
        pull=False,  # "left" | "right"
    )

    if sortBy == "ra":
        dbSortBy = "raDeg"
    if sortBy == "dec":
        dbSortBy = "decDeg"
    if sortBy == "name":
        dbSortBy = "masterName"
    if sortBy == "date added to marshall":
        dbSortBy = "dateAdded"
    if option == "date of last observation":
        dbSortBy = "currentMagnitudeDate"
    if sortBy == "discovery date":
        dbSortBy = "earliestDetection"
    if sortBy == "predicted type":
        dbSortBy = "transientTypePrediction"
    if sortBy == "pre-discovery non-detection date":
        dbSortBy = "lastNonDetectionDate"
    if sortBy == "absolute peak magnitude":
        dbSortBy = "absolutePeakMagnitude"
    if sortBy == "spectral type":
        dbSortBy = "spectralType"
    if sortBy == "classification date":
        dbSortBy = "classificationDate"
    if sortBy == "redshift":
        dbSortBy = "redshift"
    if sortBy == "latest comment date":
        dbSortBy = "latestComment"
    if sortBy == "current magnitude":
        dbSortBy = "currentMagnitude"

    popover = khufu.popover(
        tooltip=True,
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="click to reserve sort or select dropdown to change sort attribute",
        content=False,
        delay=600
    )

    sortDropdown = khufu.dropdown(
        buttonSize='default',
        buttonColor='default',  # [ default | sucess | error | warning | info ]
        menuTitle=" %(arrow)s %(sortBy)s" % locals(),
        splitButton=True,
        splitButtonHref=topButtonLink,
        linkList=linkList,
        separatedLinkList=False,
        pull=False,
        # use javascript to explode contained links
        htmlClass=False,
        direction='down',  # [ down | up ]
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        popover=popover
    )

    return sortDropdown


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
