#!/usr/local/bin/python
# encoding: utf-8
"""
*A ticket for a single PESSTO Object give all info known about it*

:Author:
    David Young

:Date Created:
    November 20, 2013
"""
import sys
import os
import ticket_building_blocks
import datetime
import khufu
import tabs


def single_ticket(
        log,
        request,
        discoveryDataDictionary,
        objectComments,
        objectAkas,
        lightcurveData,
        atelData,
        objectHistories,
        transientCrossmatches):
    """A single ticket for a transient object tin the pessto marshall

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectComments`` -- the comments for the object
        - ``objectAkas`` -- the akas with surveyUrls
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage
        - ``objectHistories`` -- history log for object
        - ``transientCrossmatches`` -- catalogue crossmatches (from sherlock)

    **Return:**
        - ``ticket`` -- a single transient's info in one HTML ticket
    """

    log.debug('starting the ``inbox_ticket`` function')

    tabDictionary = {}

    observationPriority = False
    if discoveryDataDictionary["marshallWorkflowLocation"] in ["following", "pending observation"]:
        observationPriority = discoveryDataDictionary["observationPriority"]

    import collections
    tabDictionary = collections.OrderedDict(sorted(tabDictionary.items()))

    developmentTab = tabs.development.development_tab(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas,
        atelData=atelData,
        objectHistories=objectHistories
    )
    if developmentTab:
        pass
        # tabDictionary["development"] = developmentTab

    # GRAB THE VARIOUS TABS THAT MAKE UP A SINGLE TICKET
    overviewTab = tabs.overview.overview_tab(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectComments=objectComments,
        objectAkas=objectAkas,
        atelData=atelData,
        lightcurveData=lightcurveData,
        objectHistories=objectHistories,
        transientCrossmatches=transientCrossmatches
    )
    tabDictionary["overview"] = overviewTab

    commentCount, commentsTab = tabs.comments.comments_tab(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectComments=objectComments,
        objectAkas=objectAkas,
        atelData=atelData,
        lightcurveData=lightcurveData,
        transientCrossmatches=transientCrossmatches
    )
    tabDictionary["comments"] = commentsTab

    photometryTab = tabs.photometry.photometry_tab(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas,
        atelData=atelData,
        lightcurveData=lightcurveData
    )

    tabDictionary["photometry"] = photometryTab

    contextTab = tabs.context.context_tab(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas,
        atelData=atelData,
        lightcurveData=lightcurveData,
        transientCrossmatches=transientCrossmatches
    )

    tabDictionary["context"] = contextTab

    historyTab = tabs.history.history_tab(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas,
        atelData=atelData,
        objectHistories=objectHistories
    )
    tabDictionary["ticket history"] = historyTab

    dryxTab = tabs.dryx.dryx_tab(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas,
        atelData=atelData,
        objectHistories=objectHistories
    )
    if dryxTab:
        tabDictionary["dryx"] = dryxTab

    transientBucketId = discoveryDataDictionary["transientBucketId"]

    # build the single ticket
    ticket = _single_ticket_template(
        log=log,
        transientBucketId=transientBucketId,
        tabDictionary=tabDictionary,
        htmlId="ticket%(transientBucketId)s" % locals(),
        commentCount=commentCount,
        obsPriority=observationPriority
    )

    log.debug('completed the ``inbox_ticket`` function')
    return ticket


def _single_ticket_template(
        log,
        transientBucketId,
        tabDictionary={},  # { "title": tabcontent, }
        htmlId=False,
        commentCount=False,
        obsPriority=False
):
    """single_ticket

    **Key Arguments:**
        - ``log`` -- the logger
        - ``transientBucketId`` -- the transientBucketId of the object to be displayed
        - ``tabDictionary`` -- a dictionary of { "title": tabcontent, }

    **Return:**
        - ``single_ticket`` -- build the single ticket
    """
    if commentCount is not False:
        contentCount = {"comments": commentCount}
    else:
        contentCount = {}

    if obsPriority:
        for n, c in zip([1, 2, 3, 4], ["green", "yellow", "red", "cream"]):
            if obsPriority == n:
                borderColor = c
    else:
        borderColor = False

    single_ticket = khufu.tabbableNavigation(
        contentDictionary=tabDictionary,  # { name : content, }
        fadeIn=False,
        direction='top',  # [ 'top' | 'bottom' | 'left' | 'right' ]
        htmlClass="singleTicket border-%(borderColor)s" % locals(),
        uniqueNavigationId=transientBucketId,
        htmlId=htmlId,
        contentCount=contentCount
    )

    return single_ticket


def _ticket_tab_template(
        log,
        request,
        tabHeader=False,
        blockList=[],
        tabFooter=False,
        actionsBlock=False,
        htmlId=False
):
    """ticket tab - build a tab on a ticket from a few sub-block of object data

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the pyramid request
        - ``tabHeader`` -- header bar for the tab
        - ``blockList`` -- the list of asset 'blocks' to be included in this ticket tab
        - ``tabFooter`` -- footer bar for the tab
        - ``actionsBlock`` -- to consume skinny column at right side

    **Return:**
        - ``ticket_tab`` -- template for each ticket tab
    """
    theseBlocks = ""

    # REMOVE EMPTY BLOCKS
    newBlockList = []
    for block in blockList:
        if block is not None:
            newBlockList.append(block)
    blockList = newBlockList

    actionsExist = 0
    if actionsBlock is not False:
        actionsExist = 1

    # EXPAND AND CONTRACT BLOCK SIZES DEPENDING ON HOW MANY BLOCKS THERE ARE
    span = int(round(12. / (len(blockList) + actionsExist) - 0.5))
    remainingSpans = 12 - span * len(blockList) - actionsExist

    count = 1
    for block in blockList:
        thisSpan = span
        if count < remainingSpans:
            thisSpan = span + 1
        count += 1
        if thisSpan == 12:
            if "overviewWell" in block:
                thisSpan = 11

        block = khufu.grid_column(
            span=thisSpan,
            offset=0,  # 1-12
            content=block,
            htmlId=False,
            htmlClass="ticketBlocks",
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        theseBlocks = "%(theseBlocks)s%(block)s" % locals()

    # CONVERT BYTES TO UNICODE
    if isinstance(theseBlocks, ("".__class__, u"".__class__)):
        theseBlocks = unicode(theseBlocks, encoding="utf-8", errors="replace")

    if actionsBlock is not False:
        actionsBlock = khufu.grid_column(
            span=1,
            offset=0,  # 1-12
            content=actionsBlock,
            htmlId=False,
            htmlClass="ticketBlocks",
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        theseBlocks = "%(theseBlocks)s%(actionsBlock)s" % locals()

    if tabHeader == False:
        tabHeader = u""
    if tabFooter == False:
        tabFooter = ""

    if htmlId is False:
        htmlId = ""

    ticket_tab = khufu.grid_row(
        responsive=True,
        columns=u"%(tabHeader)s %(theseBlocks)s %(tabFooter)s" % locals(
        ),
        htmlId=False,
        htmlClass=htmlId,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    return ticket_tab
