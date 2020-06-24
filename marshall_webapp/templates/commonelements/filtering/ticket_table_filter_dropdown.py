#!/usr/local/bin/python
# encoding: utf-8
"""
*The filter dropdown used to filter the tickets displayed in the marshall*

:Author:
    David Young
"""
import sys
import os
import re
import khufu


def ticket_table_filter_dropdown(
    log,
    request,
    filterBy=False,
    filterValue=False,
    filterOp=False
):
    """ticket table filter dropdown

    **Key Arguments**

    - ``log`` -- the logger
    - ``request`` -- the request
    - ``filterBy`` -- what parameter to filter by
    - ``filterValue`` -- the value to filter the parameter with
    - ``filterOp`` -- the filter operator

    **Return**

    - ``filterDropdown`` -- the filter dropdown for the transient listing pages
    """
    buttonfilterBy = ""

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

    # GENERATE THE FILTER OPTION LIST
    filterList = [
        "predicted SN",
        "predicted NT",
        "predicted AGN",
        "predicted orphan",
        "predicted CV",
        u"predicted Var★"
    ]

    filterList = sorted(filterList)
    filterList = ["remove filter"] + filterList
    if filterBy == "sherlockClassification":
        buttonfilterBy = "predicted " + filterValue
        try:
            filterList.remove("predicted " + filterValue)
        except:
            pass
    if not filterBy:
        try:
            filterList.remove("remove filter")
        except:
            pass

    # ADD LINKS TO OPTIONS
    linkList = []
    for option in filterList:
        if "predicted" in option:
            dbValue = option.replace("predicted ", "")
            theseParams["filterBy2"] = "sherlockClassification"
            theseParams["filterValue2"] = dbValue
            theseParams["filterOp2"] = 'eq'
        if "remove filter" in option:
            theseParams["filterBy2"] = False
            theseParams["filterValue2"] = False
            theseParams["filterOp2"] = False

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

    topButtonLink = request.route_path(
        routename, elementId=elementId, _query=theseParams)

    # add text color
    if filterBy:
        color = "red"
    else:
        color = "black"
    filterIcon = khufu.coloredText(
        text="""<i class="icon-filter"></i>""",
        color=color,
        size=False,  # 1-10
        pull=False,  # "left" | "right"
    )

    popover = khufu.popover(
        tooltip=True,
        placement="left",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="filter tickets by a given transient parameter",
        content=False,
        delay=20
    )

    sortDropdown = khufu.dropdown(
        buttonSize='default',
        buttonColor='default',  # [ default | sucess | error | warning | info ]
        menuTitle=" %(filterIcon)s %(buttonfilterBy)s" % locals(),
        linkList=linkList,
        pull="right",
        # use javascript to explode contained links
        direction='down',  # [ down | up ]
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        popover=popover
    )

    return sortDropdown
