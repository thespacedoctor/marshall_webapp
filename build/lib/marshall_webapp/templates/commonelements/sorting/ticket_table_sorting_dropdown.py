#!/usr/local/bin/python
# encoding: utf-8
"""
*The sort dropdown used to sort the tickets displayed in the marshall*

:Author:
    David Young
"""
import sys
import os
import re
import khufu

def ticket_table_sorting_dropdown(
    log,
    request,
    sortBy=False,
    sortDesc=False
):
    """ticket_table_sorting_dropdown

    **Key Arguments**

    - ``log`` -- the logger
    - ``request`` -- the request
    - ``sortBy`` -- the incoming sortBy
    - ``sortDesc`` -- incoming sort direction
    

    **Return**

    - ``sortDropdown`` -- the sort dropdown for the transient listing pages
    
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

    # GENERATE THE SORT OPTION LIST
    optionList = [
        "ra",
        "dec",
        "name",
        "date added to marshall",
        "date of last observation",
        "discovery date",
        "pre-discovery non-detection date",
        "absolute peak magnitude",
        "spectral type",
        "classification date",
        "redshift",
        "latest comment date",
        "current magnitude",
        "pi",
        "priority",
        "galactic latitude",
        "contextual classification",
        "association separation"
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
    if sortBy == "glat":
        sortBy = "galactic latitude"
    if sortBy == "sherlockClassification":
        sortBy = "contextual classification"
    if sortBy == "separationArcsec":
        sortBy = "association separation"

    optionList = sorted(optionList)
    if sortBy:
        try:
            optionList.remove(sortBy)
        except:
            pass

    # ADD LINKS TO OPTIONS
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
        if option == "galactic latitude":
            dbOption = "glat"
        if option == "contextual classification":
            dbOption = "sherlockClassification"
        if option == "association separation":
            dbOption = "separationArcsec"

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

    # SET SORT ARROW DIRECTION
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

    # ADD TEXT COLOR
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
    if sortBy == "galactic latitude":
        dbSortBy = "glat"
    if sortBy == "contextual classification":
        dbSortBy = "sherlockClassification"
    if sortBy == "association separation":
        dbSortBy = "separationArcsec"

    popover = khufu.popover(
        tooltip=True,
        placement="left",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="click to reserve sort or select dropdown to change sort attribute",
        content=False,
        delay=20
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
