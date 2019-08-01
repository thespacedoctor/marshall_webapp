#!/usr/local/bin/python
# encoding: utf-8
"""
marshall_sidebar.py
===============
:Summary:
    marshall_sidebar for the PESSTO Marshall

:Author:
    David Young

:Date Created:
    July 23, 2013

:Notes:
    - If you have any questions requiring this script please email me: davidrobertyoung@gmail.com
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from marshall_webapp.models.transients import models_transients_count
from marshall_webapp.templates.commonelements import forms


def marshall_sidebar(
        log,
        request,
        thisPageName
):
    """Get the left navigation bar for the pessto marshall

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``thisPageName`` -- the name of the page currently displayed

    **Return:**
        - ``leftNavBar`` -- the left navigation bar for the pessto marshall
    """
    log.debug('starting the ``marshall_sidebar`` function')
    ## VARIABLES ##
    leftColumnContent = ""

    header = _marshall_sidebar_header(
        log=log,
        request=request
    )

    targetSelectionQueue = _get_target_selection_queue(
        log,
        request=request,
        thisPageName=thisPageName
    )

    observationQueues = _get_observation_queues(
        log,
        request=request,
        thisPageName=thisPageName
    )

    classificationQueues = _get_classification_queues(
        log,
        request=request,
        thisPageName=thisPageName
    )

    referenceLists = _get_reference_lists(
        log,
        request=request,
        thisPageName=thisPageName
    )

    developmentLinks = _get_development_links(
        log,
        thisPageName=thisPageName
    )

    marshall_sidebar = """
%s
%s <br>
%s <br>
%s <br>
%s <br>""" % (
        header,
        targetSelectionQueue,
        observationQueues,
        classificationQueues,
        referenceLists,
        # developmentLinks
    )

    log.debug('completed the ``marshall_sidebar`` function')
    return marshall_sidebar


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

def _marshall_sidebar_header(
        log,
        request):
    """Generate the left navigation bar header content

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request

    **Return:**
        - ``content`` -- the left nav bar header content

    **Todo**
    """

    log.debug('starting the ``_marshall_sidebar_header`` function')
    ## VARIABLES ##

    href = request.route_path('transients')

    pesstoIcon = khufu.image(
        src=request.static_path(
            'marshall_webapp:static/images/pessto_icon.png'),
        href=href,
        display="rounded",  # [ rounded | circle | polaroid ]
        pull=False,  # [ "left" | "right" | "center" ]
        htmlClass=False,
        thumbnail=False,
        # width=25,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        htmlId="marshall_sideBarPesstoIcon"
    )

    padding = khufu.grid_column(
        span=1,  # 1-12
        offset=0,  # 1-12
        content="",
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
    )

    pesstoIcon = khufu.grid_column(
        span=4,  # 1-12
        offset=8,  # 1-12
        content=pesstoIcon,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
    )

    pesstoIcon = khufu.grid_row(
        responsive=True,
        columns=pesstoIcon,
        htmlId="marshall_sideBarPesstoIconRow",
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    createNewTicketForm, createNewButton = forms.create_new_ticket_form.create_new_ticket_form(
        log=log,
        request=request,
    )

    popover = khufu.popover(
        tooltip=True,
        placement="right",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="manually create a ticket for a new object",
        content=False,
        delay=20
    )

    createNewButton = khufu.grid_row(
        responsive=True,
        columns="%(createNewButton)s %(createNewTicketForm)s" % locals(),
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.debug('completed the ``_marshall_sidebar_header`` function')
    return "%(pesstoIcon)s %(createNewButton)s" % locals()


def _get_development_links(
        log,
        thisPageName):
    """get development links

    **Key Arguments:**
        - ``log`` -- logger
        - ``thisPageName`` -- the name of the current page

    **Return:**
        - ``developmentLinks`` -- the development queue - a list of links

    **Todo**
    """
    log.debug('starting the ``_get_development_links`` function')
    ## VARIABLES ##

    title = khufu.li(
        content="development",
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle="header",  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    loggingLink = khufu.a(
        content='logging',
        href='/marshall/logs/styled_log.html',
        tableIndex=False,
        triggerStyle=False
    )

    loggingLink = khufu.li(
        content=loggingLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=False,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    # documentationLink = khufu.a(
    #     content='documentation',
    #     href='/pessto/private/marshall/documentation/_build/html/index.html',
    #     tableIndex=False,
    #     triggerStyle=False
    # )

    # documentationLink = khufu.li(
    #     content=documentationLink,
    # if a subMenu for dropdown this should be <ul>
    # span=False,  # [ False | 1-12 ]
    #     disabled=False,
    #     submenuTitle=False,
    #     divider=False,
    # navStyle=False,  # [ active | header ]
    #     navDropDown=False,
    # pager=False  # [ False | "previous" | "next" ]
    # )

    linkList = khufu.ul(
        itemList=[title, loggingLink, ],  # e.g a list links
        unstyled=False,
        inline=False,
        dropDownMenu=False,  # [ false | true ]
        navStyle="list",  # [ nav | tabs | pills | list ]
        navPull="right",  # [ false | left | right ]
        navDirection=False,  # [ 'default' | 'stacked' | 'horizontal' ]
        breadcrumb=False,  # [ False | True ]
        pager=False,
        thumbnails=False,
        mediaList=False
    )

    column = khufu.grid_column(
        span=12,  # 1-12
        offset=0,  # 1-12
        content=linkList,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    developmentLinks = khufu.grid_row(
        responsive=True,
        columns=column,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.debug('completed the ``_get_development_links`` function')
    return developmentLinks


def _get_observation_queues(
        log,
        request,
        thisPageName):
    """get observation queues

    **Key Arguments:**
        - ``log`` -- logger
        - ``thisPageName`` -- the name of the current page

    **Return:**
        - ``observationQueues`` -- the observation queue - a list of links

    **Todo**
    """
    log.debug('starting the ``_get_observation_queues`` function')
    ## VARIABLES ##

    title = khufu.li(
        content="observation queues",
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle="header",  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"pending observation"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'pending observation'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    theseParams["filterBy1"] = False

    classificationTargetsLink = khufu.a(
        content='<i class="icon-target2"></i> classification targets (%s)' % (
            count,),
        href=request.route_path(
            'transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "pending observation"
    )

    classificationTargetsLink = khufu.li(
        content=classificationTargetsLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"following"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'following'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    theseParams["filterBy1"] = False

    followupTargetsLink = khufu.a(
        content='<i class="icon-pin"></i> + followup targets (%s)' % (count,),
        href=request.route_path('transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "following"
    )

    followupTargetsLink = khufu.li(
        content=followupTargetsLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"pending observation" OR listName="following"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'allObsQueue'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    theseParams["filterBy1"] = False

    allTargetsLink = khufu.a(
        content='= all targets (%s)' % (count,),
        href=request.route_path('transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "allObsQueue"
    )

    allTargetsLink = khufu.li(
        content=allTargetsLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    linkList = khufu.ul(
        itemList=[title, classificationTargetsLink,
                  followupTargetsLink, allTargetsLink, ],  # e.g a list links
        unstyled=False,
        inline=False,
        dropDownMenu=False,  # [ false | true ]
        navStyle="list",  # [ nav | tabs | pills | list ]
        navPull="right",  # [ false | left | right ]
        navDirection=False,  # [ 'default' | 'stacked' | 'horizontal' ]
        breadcrumb=False,  # [ False | True ]
        pager=False,
        thumbnails=False,
        mediaList=False
    )

    column = khufu.grid_column(
        span=12,  # 1-12
        offset=0,  # 1-12
        content=linkList,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    observationQueues = khufu.grid_row(
        responsive=True,
        columns=column,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.debug('completed the ``_get_observation_queues`` function')
    return observationQueues


def _get_classification_queues(
        log,
        request,
        thisPageName):
    """get classification queues

    **Key Arguments:**
        - ``log`` -- logger
        - ``thisPageName`` -- the name of the current page

    **Return:**
        - ``classificationQueues`` -- the classification queue - a list of links

    **Todo**
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    log.debug('starting the ``_get_classification_queues`` function')
    ## VARIABLES ##

    title = khufu.li(
        content="classification & atel queues",
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle="header",  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"pending classification"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'pending classification'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    theseParams["filterBy1"] = False

    queuedForClassificationLink = khufu.a(
        content='queued for classification (%s)' % (count,),
        href=request.route_path(
            'transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "pending classification"
    )

    queuedForClassificationLink = khufu.li(
        content=queuedForClassificationLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag=None,
        awfFlag='"queued for atel"',
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["awl"] = 'queued for atel'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "mwl", "pageStart", "q"]
    )

    theseParams["filterBy1"] = False

    queuedForAtelLink = khufu.a(
        content='queued for atel (%s)' % (count,),
        href=request.route_path(
            'transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "queued for atel"
    )

    queuedForAtelLink = khufu.li(
        content=queuedForAtelLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    linkList = khufu.ul(
        # e.g a list links
        itemList=[title, queuedForClassificationLink, queuedForAtelLink, ],
        unstyled=False,
        inline=False,
        dropDownMenu=False,  # [ false | true ]
        navStyle="list",  # [ nav | tabs | pills | list ]
        navPull="right",  # [ false | left | right ]
        navDirection=False,  # [ 'default' | 'stacked' | 'horizontal' ]
        breadcrumb=False,  # [ False | True ]
        pager=False,
        thumbnails=False,
        mediaList=False
    )

    column = khufu.grid_column(
        span=12,  # 1-12
        offset=0,  # 1-12
        content=linkList,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    classificationQueues = khufu.grid_row(
        responsive=True,
        columns=column,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.debug('completed the ``_get_classification_queues`` function')
    return classificationQueues


def _get_reference_lists(
        log,
        request,
        thisPageName):
    """get reference lists

    **Key Arguments:**
        - ``log`` -- logger
        - ``thisPageName`` -- the name of the current page

    **Return:**
        - ``referenceLists`` -- the reference queue - a list of links

    **Todo**
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    log.debug('starting the ``_get_reference_lists`` function')
    ## VARIABLES ##

    title = khufu.li(
        content="reference",
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle="header",  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag=None,
        awfFlag=None,
        cFlag='"NOT NULL"'
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'all'
    theseParams["cf"] = 1
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "awl", "pageStart", "q"]
    )

    classifiedLink = khufu.a(
        content='classified (%s)' % (count,),
        href=request.route_path('transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "classified"
    )

    classifiedLink = khufu.li(
        content=classifiedLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"followup complete"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'followup complete'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    followupCompleteLink = khufu.a(
        content='<i class="icon-checkmark-circle"></i> followup complete (%s)' % (
            count,),
        href=request.route_path(
            'transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "followup complete"
    )

    followupCompleteLink = khufu.li(
        content=followupCompleteLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"archive"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'archive'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    allArchivedLink = khufu.a(
        content='<i class="icon-archive5"></i>  all archived (%s)' % (count,),
        href=request.route_path('transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "archive"
    )

    allArchivedLink = khufu.li(
        content=allArchivedLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"all"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'all'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    allLink = khufu.a(
        content='all  (%s)' % (count,),
        href=request.route_path('transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "all"
    )

    allLink = khufu.li(
        content=allLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    linkList = khufu.ul(
        # e.g a list links
        itemList=[title, allLink, classifiedLink,
                  followupCompleteLink, allArchivedLink],
        unstyled=False,
        inline=False,
        dropDownMenu=False,  # [ false | true ]
        navStyle="list",  # [ nav | tabs | pills | list ]
        navPull="right",  # [ false | left | right ]
        navDirection=False,  # [ 'default' | 'stacked' | 'horizontal' ]
        breadcrumb=False,  # [ False | True ]
        pager=False,
        thumbnails=False,
        mediaList=False
    )

    column = khufu.grid_column(
        span=12,  # 1-12
        offset=0,  # 1-12
        content=linkList,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    referenceLists = khufu.grid_row(
        responsive=True,
        columns=column,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.debug('completed the ``_get_reference_lists`` function')
    return referenceLists


# LAST MODIFIED : July 3, 2013
# CREATED : July 3, 2013
# AUTHOR : DRYX
def _get_target_selection_queue(
        log,
        request,
        thisPageName):
    """get tagert selection queue

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - ``targetSelectionQueue`` -- the target selection queue - a list of links

    **Todo**
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    log.debug('starting the ``_get_tagert_selection_queue`` function')
    ## VARIABLES ##

    placeHolder = khufu.image(
        src='holder.js/300x200/auto/industrial/text:hello world',
    )

    title = khufu.li(
        content="target selection queues",
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle="header",  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"inbox"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)

    theseParams["mwl"] = 'inbox'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    theseParams["filterBy1"] = "decDeg"
    theseParams["filterValue1"] = 30
    theseParams["filterOp1"] = "<"

    inboxLink = khufu.a(
        content='<i class="icon-inbox"></i>  inbox (%s)' % (count,),
        href=request.route_path('transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "inbox"
    )

    inboxLink = khufu.li(
        content=inboxLink,  # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag=None,
        awfFlag=None,
        cFlag=None,
        snoozed=1
    ).get()

    theseParams = dict(request.params)
    theseParams["snoozed"] = 1
    theseParams["mwl"] = "all"
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["cf", "awl", "pageStart", "q"]
    )

    theseParams["filterBy1"] = "decDeg"
    theseParams["filterValue1"] = 30
    theseParams["filterOp1"] = "<"

    snoozedLink = khufu.a(
        content='<i class="icon-alarm3"></i>  snoozed (%s)' % (count,),
        href=request.route_path('transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "snoozed"
    )

    snoozedLink = khufu.li(
        content=snoozedLink,  # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag='"review for followup"',
        awfFlag=None,
        cFlag=None
    ).get()

    theseParams = dict(request.params)
    theseParams["mwl"] = 'review for followup'
    theseParams = _remove_parameters(
        log=log,
        params=theseParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q"]
    )

    theseParams["filterBy1"] = "decDeg"
    theseParams["filterValue1"] = 30
    theseParams["filterOp1"] = "<"

    reviewForFollowupLink = khufu.a(
        content='<i class="icon-eye"></i>  review for followup (%s)' % (
            count,),
        href=request.route_path(
            'transients', _query=theseParams),
        tableIndex=False,
        triggerStyle=False
    )

    navStyle = khufu.is_navStyle_active(
        log,
        thisPageName,
        "review for followup"
    )

    reviewForFollowupLink = khufu.li(
        content=reviewForFollowupLink,
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=navStyle,  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    linkList = khufu.ul(
        # e.g a list links
        itemList=[title, inboxLink, snoozedLink, reviewForFollowupLink, ],
        unstyled=False,
        inline=False,
        dropDownMenu=False,  # [ false | true ]
        navStyle="list",  # [ nav | tabs | pills | list ]
        navPull="right",  # [ false | left | right ]
        navDirection=False,  # [ 'default' | 'stacked' | 'horizontal' ]
        breadcrumb=False,  # [ False | True ]
        pager=False,
        thumbnails=False,
        mediaList=False
    )

    column = khufu.grid_column(
        span=12,  # 1-12
        offset=0,  # 1-12
        content=linkList,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    targetSelectionQueue = khufu.grid_row(
        responsive=True,
        columns=column,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.debug('completed the ``get_tagert_selection_queue`` function')
    return targetSelectionQueue


def _remove_parameters(
        log,
        params,
        paramsToRemove
):
    """Get the left navigation bar for the pessto marshall

    **Key Arguments:**
        - ``log`` -- logger
        - ``params`` -- the parameters of the request
        - ``paramsToRemove`` -- the parameters to remove from the incoming request

    **Return:**
        - ``params`` -- the clean parameters
    """
    log.debug('starting the ``_remove_parameter`` function')
    ## VARIABLES ##

    # for key in params.keys():
    #     if key != paramToKeep:
    #         del params[key]

    if isinstance(paramsToRemove, str):
        paramsToRemove = [paramsToRemove]

    for key in paramsToRemove:
        if key in params:
            del params[key]

    log.debug('completed the ``_remove_parameters  `` function')
    return params
