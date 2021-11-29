#!/usr/local/bin/python
# encoding: utf-8
"""
*marshall_sidebar for the Marshall*

:Author:
    David Young
"""
import sys
import os
import khufu
from marshall_webapp.models.transients import models_transients_count
from marshall_webapp.templates.commonelements import forms
import copy
import yaml


def marshall_sidebar(
        log,
        request,
        thisPageName
):
    """Get the left navigation bar for the pessto marshall

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``thisPageName`` -- the name of the page currently displayed

    **Return**

    - ``leftNavBar`` -- the left navigation bar for the pessto marshall

    """
    log.debug('starting the ``marshall_sidebar`` function')

    leftColumnContent = ""

    # MAKE SURE PARAMETERS PERSIST IF REQUEST COMING FROM A TRANSIENT RESOURCE
    if request.referer and "transients" not in request.referer:
        params = {}
    else:
        params = dict(request.params)

    header = _marshall_sidebar_header(
        log=log,
        request=request,
        params=params
    )

    theseParams = copy.deepcopy(params)
    # theseParams["filterBy1"] = "decDeg"
    # theseParams["filterValue1"] = 30
    # theseParams["filterOp1"] = "<"

    sidebarNavigationSettings = request.registry.settings["sidebar"]
    sidebarBlocks = []
    for blockTitle, linkSettings in sidebarNavigationSettings.items():
        title = khufu.li(
            content=blockTitle,
            navStyle="header",  # [ active | header ]
        )
        blockLinks = []
        for linkName, ls in linkSettings.items():
            defaults = {
                "mwf": None,
                "awl": None,
                "classified": None,
                "snoozed": None,
                "icon": None
            }
            for k, v in defaults.items():
                if k not in ls:
                    ls[k] = v
            nextLink = list_link(
                log=log,
                name=linkName,
                mwl=ls["mwf"],
                awl=ls["awl"],
                classified=ls["classified"],
                snoozed=ls["snoozed"],
                request=request,
                initialParams=theseParams,
                currentPageName=thisPageName,
                icon=ls["icon"]
            )
            blockLinks.append(nextLink)
        itemList = [title] + blockLinks
        linkList = khufu.ul(
            # e.g a list links
            itemList=itemList,
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
        sidebarListBlock = khufu.grid_row(
            responsive=True,
            columns=column,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        sidebarBlocks.append(sidebarListBlock)

    sidebarBlocks = ("<br>").join(sidebarBlocks)

    marshall_sidebar = """
%s
%s <br>""" % (
        header,
        sidebarBlocks
    )

    log.debug('completed the ``marshall_sidebar`` function')
    return marshall_sidebar


def _marshall_sidebar_header(
        log,
        request,
        params):
    """Generate the left navigation bar header content

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``params`` -- params required for links


    **Return**

    - ``content`` -- the left nav bar header content

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


def _remove_parameters(
        log,
        params,
        paramsToRemove
):
    """Get the left navigation bar for the pessto marshall

    **Key Arguments**

    - ``log`` -- logger
    - ``params`` -- the parameters of the request
    - ``paramsToRemove`` -- the parameters to remove from the incoming request


    **Return**

    - ``params`` -- the clean parameters

    """
    log.debug('starting the ``_remove_parameter`` function')

    if isinstance(paramsToRemove, ("".__class__, u"".__class__)):
        paramsToRemove = [paramsToRemove]

    for key in paramsToRemove:
        if key in params:
            del params[key]

    log.debug('completed the ``_remove_parameters  `` function')
    return params


def list_link(
        log,
        request,
        name,
        mwl=None,
        awl=None,
        classified=None,
        snoozed=None,
        initialParams={},
        currentPageName="",
        icon=False):
    """*create a link to a specific view of the data*

    **Key Arguments:**

    - ``log`` -- logger
    - ``request`` -- the page request
    - ``name`` -- the name of the list
    - ``mwl`` -- the marshall workflow location. Default *inbox*. [inbox|archive|pending observation|review for followup|following|followup complete]
    - ``awl`` -- the alert workflow location. Default *None*. [archived without alert|external alert released|Pending Classification|pessto classification released]
    - ``classified`` -- classified or not? Default *None*. [True|False|None]
    - ``initialParams`` -- the initial parameters passed from the current browser page. Default *{}*.
    - ``currentPageName`` -- name of the current page (used to set the active link in sidebar).
    - ``icon`` -- the name of the icon to add to left of link name. Default *False*.

    **Usage:**

    ```eval_rst
    .. todo::

            add usage info
            create a sublime snippet for usage
    ```

    ```python
    usage code 
    ```           
    """
    log.debug('starting the ``list_link`` function')

    linkParams = initialParams
    linkParams = _remove_parameters(
        log=log,
        params=linkParams,
        paramsToRemove=["snoozed", "cf", "awl", "pageStart", "q", "mwl"]
    )
    if mwl:
        linkParams["mwl"] = mwl
    if awl:
        linkParams["awl"] = awl
    if snoozed:
        linkParams["snoozed"] = 1
    if classified:
        linkParams["cf"] = 1

    # IS LINKED LIST THE CURENT PAGE - IF SO HIGHLIGHT IN SIDEBAR
    navStyle = khufu.is_navStyle_active(
        log=log,
        thisPageId=currentPageName,
        thisPageName=name
    )

    count = models_transients_count(
        log,
        request=request,
        mwfFlag=mwl,
        awfFlag=awl,
        cFlag=classified,
        snoozed=snoozed
    ).get()

    if icon:
        name = f"<i class='{icon}'></i>  {name}"

    if count or count == 0:
        name = f"{name} ({count})"

    link = khufu.a(
        content=name,
        href=request.route_path('transients', _query=linkParams),
        tableIndex=False,
        triggerStyle=False
    )

    link = khufu.li(
        content=link,  # if a subMenu for dropdown this should be <ul>
        navStyle=navStyle  # [ active | header ]
    )

    log.debug('completed the ``list_link`` function')
    return link

# use the tab-trigger below for new function
# xt-def-function
