#!/usr/local/bin/python
# encoding: utf-8
"""
stats_sidebar.py
===============
:Summary:
    stats_sidebar for the PESSTO Marshall

:Author:
    David Young

:Date Created:
    April 29, 2014

:Notes:
    - If you have any questions requiring this script please email me: davidrobertyoung@gmail.com

:Tasks:
    - [ ] when complete, extract all code out of the main function and add cl commands
    - [ ] make internal function private
    - [ ] pull all general functions and classes into dryxPythonModules
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################


# LAST MODIFIED : July 2, 2013
# CREATED : July 2, 2013
# AUTHOR : DRYX
def stats_sidebar(
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

    **Todo**
    - [ ] when complete, clean stats_sidebar function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    log.info('starting the ``stats_sidebar`` function')
    ## VARIABLES ##

    leftColumnContent = ""

    header = _stats_sidebar_header(
        log=log,
        request=request
    )

    esoPhaseIIILinks = _get_esoPhaseIII_links(
        log,
        request=request,
        thisPageName=thisPageName
    )

    stats_sidebar = """
%(header)s
%(esoPhaseIIILinks)s <br>
""" % locals()

    log.info('completed the ``stats_sidebar`` function')
    return stats_sidebar


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


# LAST MODIFIED : July 2, 2013
# CREATED : July 2, 2013
# AUTHOR : DRYX
def _stats_sidebar_header(
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
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    log.info('starting the ``_stats_sidebar_header`` function')
    ## VARIABLES ##

    pesstoIcon = khufu.image(
        src=request.static_path(
            'marshall_webapp:static/images/pessto_icon.png'),
        href=request.route_path('transients'),
        display=False,  # [ rounded | circle | polaroid ]
        pull=False,  # [ "left" | "right" | "center" ]
        htmlClass=False,
        thumbnail=False,
        # width=25,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        htmlId="stats_sideBarPesstoIcon"
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
        htmlId="stats_sideBarPesstoIconRow",
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.info('completed the ``_stats_sidebar_header`` function')
    # return "%(pesstoIcon)s %(createNewButton)s" % locals()
    return "%(pesstoIcon)s" % locals()


# LAST MODIFIED : July 3, 2013
# CREATED : July 3, 2013
# AUTHOR : DRYX
def _get_esoPhaseIII_links(
        log,
        request,
        thisPageName):
    """get development links

    **Key Arguments:**
        - ``log`` -- logger
        - ``thisPageName`` -- the name of the current page

    **Return:**
        - ``developmentLinks`` -- the development queue - a list of links

    **Todo**
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import os
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    log.info('starting the ``_get_development_links`` function')
    ## VARIABLES ##

    title = khufu.li(
        content="ESO Phase III",
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle="header",  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    releaseLinks = []
    releaseVersions = ["SSDR1", "SSDR2"]
    for releaseVersion in releaseVersions:
        SSDRLink = khufu.a(
            content=releaseVersion,
            href=request.route_path('stats_element', elementId=releaseVersion),
            tableIndex=False,
            triggerStyle=False
        )
        SSDRLink = khufu.li(
            content=SSDRLink,
        )
        releaseLinks.append(SSDRLink)

    releaseLinks.insert(0, title)

    linkList = khufu.ul(
        itemList=releaseLinks,  # e.g a list links
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

    log.info('completed the ``_get_development_links`` function')
    return developmentLinks


if __name__ == '__main__':
    main()
