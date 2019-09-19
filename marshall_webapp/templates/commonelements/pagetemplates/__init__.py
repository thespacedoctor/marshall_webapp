#!/usr/local/bin/python
# encoding: utf-8
"""
*The webpage scaffolding for the pessto marshall*

:Author:
    David Young

:Date Created:
    November 20, 2013
"""
import sys
import os
import khufu


def defaultpagetemplate(
        log,
        request,
        bodyId=False,
        pageTitle="PESSTO Marshall",
        topNavBar=False,
        sideBar=False,
        mainContent=False,
        relativePathFromDocRoot=False,
        thisPageName=""
):
    """Generate the webpage to be displayed

    **Key Arguments:**
        - ``log`` -- logger
        - ``bodyId`` -- the bodyId of the page
        - ``pageTitle`` -- the title for the page (shows in browser tab)
        - ``topNavBar`` -- topNavBar
        - ``sideBar`` -- sideBar
        - ``mainContent`` -- mainContent
        - ``relativePathFromDocRoot`` -- the path to the assets folder relative to the document root
        - ``thisPageName`` -- the name of the page currently displayed
        - ``params`` -- dictionary of parameters passed to via the url of webpage

    **Return:**
        - ``webpage`` -- the webpage to be displayed
    """
    log.debug('starting the ``webpage`` function')

    # imports
    from marshall_webapp.templates.commonelements import *

    # SET DEFAULT VARIABLES
    if not bodyId:
        bodyId = "inbox"
    if not relativePathFromDocRoot:
        relativePathFromDocRoot = ""

    # SELECT THE SIDEBAR FLAVOUR
    if not sideBar or sideBar == "marshall":
        sideBar = sidebar.marshall_sidebar(
            log=log,
            request=request,
            thisPageName=thisPageName
        )
    elif sideBar == "stats":
        sideBar = sidebar.stats_sidebar(
            log=log,
            request=request,
            thisPageName=thisPageName
        )
    elif sideBar == "xmatches":
        sideBar = sidebar.xmatches_sidebar(
            log=log,
            request=request,
            thisPageName=thisPageName
        )

    # SET DEFAULT TOP NAVBAR
    if not topNavBar:
        topNavBar = topnavbar.topnavbar(
            log=log,
            request=request
        )
    if not mainContent:
        mainContent = khufu.image(
            src='holder.js/900x700/auto/industrial/text:mainContent',
        )

    head = khufu.head(
        relativeUrlBase=relativePathFromDocRoot,
        mainCssFilePath=request.static_path(
            'marshall_webapp:static/styles/css/main_marshall.css'),
        pageTitle=pageTitle,
        extras=''
    )

    sideBar = """<div id="leftSidebar">%(sideBar)s</div>""" % locals()

    sideBarContainer = khufu.grid_column(
        span=2,  # 1-12
        offset=0,  # 1-12
        content=sideBar,
    )

    pageContent = khufu.grid_column(
        span=9,  # 1-12
        offset=0,  # 1-12
        content=mainContent
    )

    content = khufu.grid_row(
        responsive=True,
        columns="%(sideBarContainer)s %(pageContent)s" % locals(),
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    body = khufu.body(
        navBar=topNavBar,
        content=content,
        htmlId='',
        extraAttr='',
        relativeUrlBase=relativePathFromDocRoot,
        responsive=True,
        googleAnalyticsCode=False,
        jsFilePath=request.static_path(
            'marshall_webapp:static/js/main-ck.js')
    )

    webpage = khufu.htmlDocument(
        contentType=False,
        content="%(head)s %(body)s" % locals()
    )

    log.debug('completed the ``webpage`` function')
    return webpage
