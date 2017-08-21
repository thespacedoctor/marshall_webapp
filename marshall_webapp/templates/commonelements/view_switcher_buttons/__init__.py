#!/usr/local/bin/python
# encoding: utf-8
"""
view_switcher_buttons.py
===========
:Summary:
    View switcher buttons for ticket table toolbar

:Author:
    David Young

:Date Created:
    March 4, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import re
import os
from docopt import docopt
from dryxPython import commonutils as dcu
import khufu


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : March 4, 2014
# CREATED : March 4, 2014
# AUTHOR : DRYX
def view_switcher_buttons(
    log,
    params,
    request,
    elementId=False,
    tcsTableName=False
):
    """view_switcher_buttons

    **Key Arguments:**
        - ``log`` -- logger
        - ``params`` -- the request params (defaults added if not populated)
        - ``request`` -- the pyramid request
        - ``elementId`` -- the transientBucketId

    **Return:**
        - None

    **Todo**
    """
    theseLinks = ""

    # The various view options
    format = ["html_tickets", "html_table", "csv", "json", "plain_table"]
    linkText = ["tickets", "table", "csv", "json", "plain text"]

    for f, l in zip(format, linkText):
        # skip the current view
        if params["format"] == f:
            continue
        thisLink = _link_for_popover(
            log=log,
            request=request,
            format=f,
            params=params,
            linkText=l,
            elementId=elementId
        )
        theseLinks = "%(theseLinks)s %(thisLink)s" % locals()

    popover = khufu.popover(
        tooltip=False,
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="view switcher",
        content=theseLinks,
        delay=200
    )
    viewSwitcherButton = khufu.button(
        buttonText="""<i class="icon-eye3"></i>""" % locals(),
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='default',
        buttonSize='default',  # [ large | default | small | mini ]
        htmlId=False,
        href=False,
        pull=False,  # right, left, center
        submit=False,
        block=False,
        disable=False,
        dataToggle=False,  # [ modal ]
        popover=popover
    )

    theseLinks = ""

    # The various download options
    format = ["csv", "json", "plain_table"]
    linkText = ["csv", "json", "plain text"]

    for f, l in zip(format, linkText):
        # skip the current view
        if params["format"] == f:
            continue
        thisLink = _link_for_popover(
            log=log,
            request=request,
            format=f,
            params=params,
            linkText=l,
            download=True,
            elementId=elementId,
            tcsTableName=tcsTableName
        )
        theseLinks = "%(theseLinks)s %(thisLink)s" % locals()
    popover = khufu.popover(
        tooltip=False,
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="download options",
        content=theseLinks,
        delay=200
    )
    downloadsButton = khufu.button(
        buttonText="""<i class="icon-save"></i>""" % locals(),
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='default',
        buttonSize='default',  # [ large | default | small | mini ]
        htmlId=False,
        href=False,
        pull=False,  # right, left, center
        submit=False,
        block=False,
        disable=False,
        dataToggle=False,  # [ modal ]
        popover=popover
    )

    return viewSwitcherButton + downloadsButton


def ntt_view_button(
    log,
    params,
    elementId,
    request
):
    """ntt_view_button

    **Key Arguments:**
        - ``log`` -- logger
        - ``params`` -- the request params (defaults added if not populated)
        - ``request`` -- the pyramid request

    **Return:**
        - None

    **Todo**
    """
    theseLinks = ""
    match = False

    if "filterBy" in params and "filterValue" in params and "filterOp" in params:

        if params["filterBy"] == "decDeg" and params["filterValue"] in ["30", 30] and params["filterOp"] in ["lt", "<"]:

            htmlClass = "on"
            content = "show targets > +30&deg;"
            params["filterBy"] = None
            params["filterValue"] = None
            params["filterOp"] = None
            match = True

    if match == False:
        htmlClass = False
        content = "hide targets > +30&deg;"
        params["filterBy"] = "decDeg"
        params["filterValue"] = 30
        params["filterOp"] = "lt"

    routename = request.matched_route.name
    if "q" in params:
        href = request.route_path('transients_search', _query=params)
    else:
        href = request.route_path(
            routename, elementId=elementId, _query=params)

    popover = khufu.popover(
        tooltip=False,
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="Target Filter",
        content=content,
        delay=200
    )
    viewSwitcherButton = khufu.button(
        buttonText="""<i class="icon-globe"></i>&nbspNTT""" % locals(),
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='default',
        buttonSize='default',  # [ large | default | small | mini ]
        htmlId=False,
        htmlClass=htmlClass,
        href=href,
        pull=False,  # right, left, center
        submit=False,
        block=False,
        disable=False,
        dataToggle=False,  # [ modal ]
        popover=popover
    )

    return viewSwitcherButton

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
# LAST MODIFIED : November 7, 2014
# CREATED : November 7, 2014
# AUTHOR : DRYX


def _link_for_popover(
        log,
        request,
        format,
        params,
        linkText=False,
        download=False,
        elementId=False,
        tcsTableName=False):
    """ link for popover

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- pyramid request object
        - ``format`` -- format of view to return
        - ``linkText`` - text for link if different than format
        - ``elementId`` -- the transientBucketId

    **Return:**
        - ``thisLink`` -- the link for the popover

    **Todo**
    """
    log.info('starting the ``_link_for_popover`` function')

    params["format"] = format
    params["method"] = "get"

    if ("limit" not in params or not params["limit"]):
        if format == "html_table":
            params["limit"] = 100
        elif format == "html_tickets":
            params["limit"] = 10

    if download:
        if "html" not in format:
            params["filename"] = ""
            if tcsTableName:
                params["filename"] = tcsTableName
            elif "snoozed" in params and params["snoozed"]:
                params["filename"] += "snoozed"
            elif "cf" in params and params["cf"]:
                params["filename"] += "classifications"
            elif "awl" in params and params["awl"]:
                params["filename"] += params["awl"]
            elif "mwl" in params and params["mwl"]:
                params["filename"] += params["mwl"]

            elif "q" in params:
                params["filename"] += "search_" + params["q"]
            elif "snoozed" in params:
                params["filename"] += "snoozed"
            elif "filterBy" in params:
                params["filename"] += "filtered"
            elif elementId:
                sqlQuery = u"""
                    select masterName from transientBucketSummaries where transientBucketId = %(elementId)s 
                """ % locals()
                objectDataTmp = request.db.execute(sqlQuery).fetchall()
                objectData = []
                objectData[:] = [dict(zip(row.keys(), row))
                                 for row in objectDataTmp]
                params["filename"] = "search_" + objectData[0]["masterName"]

            oldnames = ["pending obs", "following", "allObsQueue"]
            newnames = ["classification targets", "followup targets",
                        "classification and followup targets"]

            for o, n in zip(oldnames, newnames):
                if o in params["filename"]:
                    params["filename"] = n
                    break

            params["filename"] = "pessto_marshall_" + params["filename"]

    # if plain text download (json, csv ...) remove limits
    if "html" not in params["format"]:
        params = dict(params)
        log.debug("""params1: `%(params)s`""" % locals())
        log.debug("""params2: `%(params)s`""" % locals())

    routename = request.matched_route.name
    if "q" in params:
        href = request.route_path('transients_search', _query=params)
    else:
        href = request.route_path(
            routename, elementId=elementId, _query=params)

    if linkText:
        format = linkText
    thisLink = khufu.a(
        content=format,
        href=href
    )
    thisLink = khufu.p(
        content=thisLink,
        textAlign="center",  # [ left | center | right ]
    )

    log.info('completed the ``_link_for_popover`` function')
    return thisLink

# use the tab-trigger below for new function
# xt-def-with-logger


if __name__ == '__main__':
    main()
