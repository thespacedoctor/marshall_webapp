#!/usr/local/bin/python
# encoding: utf-8
"""
webpage.py
==========
:Summary:
    The webpage scaffolding for the pessto marshall

:Author:
    David Young

:Date Created:
    November 20, 2013

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import commonutils as dcu

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : September 30, 2014
# CREATED : July 1, 2013
# AUTHOR : DRYX


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

    **Todo**
        # @review: when complete, clean webpage function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu
    from .. import *

    log.info('starting the ``webpage`` function')
    ## VARIABLES ##

    if not bodyId:
        bodyId = "inbox"
    if not relativePathFromDocRoot:
        relativePathFromDocRoot = ""
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
        mainCssFileName='main_marshall.css',
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
        jsFileName="main-ck.js"
    )

    webpage = khufu.htmlDocument(
        contentType=False,
        content="%(head)s %(body)s" % locals()
    )

    # log.info('completed the ``webpage`` function')
    return webpage


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
