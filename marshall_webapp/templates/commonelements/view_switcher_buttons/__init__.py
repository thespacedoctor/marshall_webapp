#!/usr/local/bin/python
# encoding: utf-8
"""
*View switcher buttons for ticket table toolbar*

:Author:
    David Young
"""


def view_switcher_buttons(
    log,
    params,
    request,
    elementId=False,
    tcsTableName=False
):
    """view_switcher_buttons

    **Key Arguments**

    - ``log`` -- logger
    - ``params`` -- the request params (defaults added if not populated)
    - ``request`` -- the pyramid request
    - ``elementId`` -- the transientBucketId


    **Return**

    - ``viewSwitcherButton`` + ``downloadsButton``

    """
    import khufu
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
        delay=20
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
        delay=20
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

    **Key Arguments**

    - ``log`` -- logger
    - ``params`` -- the request params (defaults added if not populated)
    - ``request`` -- the pyramid request


    **Return**

    - ``viewSwitcherButton`` -- the view switching button

    """
    import khufu
    theseLinks = ""
    match = False

    if "filterBy1" in params and "filterValue1" in params and "filterOp1" in params:

        if params["filterBy1"] == "decDeg" and params["filterValue1"] in ["30", 30] and params["filterOp1"] in ["lt", "<"]:

            htmlClass = "on"
            content = "show targets > +30&deg;"
            params["filterBy1"] = None
            params["filterValue1"] = None
            params["filterOp1"] = None
            match = True

    if match == False:
        htmlClass = False
        content = "hide targets > +30&deg;"
        params["filterBy1"] = "decDeg"
        params["filterValue1"] = 30
        params["filterOp1"] = "lt"

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
        delay=20
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

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- pyramid request object
    - ``format`` -- format of view to return
    - ``linkText`` - text for link if different than format
    - ``elementId`` -- the transientBucketId


    **Return**

    - ``thisLink`` -- the link for the popover

    """
    import khufu
    log.debug('starting the ``_link_for_popover`` function')

    params["format"] = format
    params["method"] = "get"

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
            elif "filterBy1" in params:
                params["filename"] += "filtered"
            elif elementId:
                sqlQuery = u"""
                    select masterName from transientBucketSummaries where transientBucketId = %(elementId)s 
                """ % locals()
                objectDataTmp = request.db.execute(sqlQuery).fetchall()
                objectData = []
                objectData[:] = [dict(list(zip(list(row.keys()), row)))
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

    import copy
    p = copy.deepcopy(params)
    if format == "html_table":
        p["limit"] = 100
    elif format == "html_tickets":
        p["limit"] = 10

    # IF PLAIN TEXT DOWNLOAD (JSON, CSV ...) REMOVE LIMITS
    if "html" not in p["format"]:
        p = dict(p)
        log.debug("""p1: `%(p)s`""" % locals())
        log.debug("""p2: `%(p)s`""" % locals())

    routename = request.matched_route.name
    if "q" in p:
        href = request.route_path('transients_search', _query=p)
    else:
        href = request.route_path(
            routename, elementId=elementId, _query=p)

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

    log.debug('completed the ``_link_for_popover`` function')
    return thisLink
