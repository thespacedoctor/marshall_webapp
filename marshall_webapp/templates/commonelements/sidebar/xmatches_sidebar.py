#!/usr/local/bin/python
# encoding: utf-8
"""
*xmatches_sidebar for the PESSTO Marshall*

:Author:
    David Young
"""
import sys
import os
import khufu

def xmatches_sidebar(
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
    import khufu

    log.debug('starting the ``xmatches_sidebar`` function')

    leftColumnContent = ""

    header = _xmatches_sidebar_header(
        log=log,
        request=request
    )

    esoPhaseIIILinks = _get_xmatches_links(
        log,
        request=request,
        thisPageName=thisPageName
    )

    xmatches_sidebar = """
%(header)s
%(esoPhaseIIILinks)s <br>
""" % locals()

    log.debug('completed the ``xmatches_sidebar`` function')
    return xmatches_sidebar

def _xmatches_sidebar_header(
        log,
        request):
    """Generate the left navigation bar header content

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    

    **Return**

    - ``content`` -- the left nav bar header content
    
    """
    import khufu

    log.debug('starting the ``_xmatches_sidebar_header`` function')

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
        htmlId="xmatches_sideBarPesstoIcon"
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
        htmlId="xmatches_sideBarPesstoIconRow",
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.debug('completed the ``_xmatches_sidebar_header`` function')
    # return "%(pesstoIcon)s %(createNewButton)s" % locals()
    return "%(pesstoIcon)s" % locals()

def _get_xmatches_links(
        log,
        request,
        thisPageName):
    """get development links

    **Key Arguments**

    - ``log`` -- logger
    - ``thisPageName`` -- the name of the current page
    

    **Return**

    - ``developmentLinks`` -- the development queue - a list of links
    
    """
    import os
    import khufu

    log.debug('starting the ``_get_development_links`` function')

    title = khufu.li(
        content="Catalogue Crossmatches",
        # if a subMenu for dropdown this should be <ul>
        span=False,  # [ False | 1-12 ]
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle="header",  # [ active | header ]
        navDropDown=False,
        pager=False  # [ False | "previous" | "next" ]
    )

    theseLinks = []
    linkTitles = ["catalogues", "sub-catalogues", "searches", "associations"]
    linkTitles = ["catalogues"]
    for ltitle in linkTitles:
        thisLink = khufu.a(
            content=ltitle,
            href=request.route_path("xmatches_" + ltitle),
            tableIndex=False,
            triggerStyle=False
        )
        thisLink = khufu.li(
            content=thisLink,
        )
        theseLinks.append(thisLink)

    theseLinks.insert(0, title)

    linkList = khufu.ul(
        itemList=theseLinks,  # e.g a list links
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
