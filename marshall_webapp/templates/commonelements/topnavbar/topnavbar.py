#!/usr/local/bin/python
# encoding: utf-8
"""
*The top navigation bar for the PESSTO Marshall*

:Author:
    David Young
"""
import sys
import os
import khufu


def topnavbar(log,
              request):
    """
    Get a top navigation bar for the pessto marshall.

    **Key Arguments**

    - ``log`` -- logger


    **Return**

    - ``topNavBar`` -- the top navigation bar for the pessto marshall

    """
    log.debug('starting the ``topNavigationBar`` function')

    username = request.authenticated_userid
    username = username.replace(".", " ").title()
    if username:
        href = request.route_path('logout')
        logout = khufu.a(
            content="logout",
            href=href,
        )
        username = """%(username)s (%(logout)s)""" % locals()
    else:
        href = request.route_path('login')
        username = khufu.a(
            content="login",
            href=href,
        )

    src = request.static_path(
        'marshall_webapp:static/images/home_button_body.png')

    icon = khufu.image(
        src=src,
        href=False,
        display=False,  # [ rounded | circle | polaroid ]
        pull="left",  # [ "left" | "right" | "center" ]
        htmlClass=False,
        thumbnail=False,
        width=25,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    marshallHome = khufu.a(
        content='marshall',
        href=request.route_path('transients'))
    statsHome = khufu.a(
        content='stats',
        href=request.route_path('stats'))
    members = khufu.a(
        content='member list',
        href=request.route_path('members'))

    pesstoHome = khufu.a(
        content='pessto.org',
        href='https://www.pessto.org',
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]
    pesstoWiki = khufu.a(
        content="wiki",
        href='https://sites.google.com/a/pessto.org/wiki/',
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]
    pesstoGroups = khufu.a(
        content="groups",
        href='https://groups.google.com/a/pessto.org/forum/#!myforums',
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]
    pesstoDocs = khufu.a(
        content="drive",
        href='https://drive.google.com/a/pessto.org/?tab=go#home',
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]
    help = khufu.a(
        content='help & reference',
        href='https://github.com/thespacedoctor/marshall_webapp_wiki/wiki',
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]
    finderChartsRepo = khufu.a(
        content='finder charts',
        href='https://sites.google.com/a/pessto.org/wiki/home-page/observing-runs/finder-chart-repo',
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]
    externalData = khufu.a(
        content='external data',
        href='https://www.pessto.org/private/data/external',
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]
    observingCalendar = khufu.a(
        content='observing calendar',
        href=request.route_path('calendars'),
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]
    xmatches = khufu.a(
        content='xmatches',
        href=request.route_path('xmatches_catalogues'),
        tableIndex=False,
        # table index for the dropdown menus [ False | -1 ]
        triggerStyle=False)  # used as a dropdown or tab trigger? [ False | "dropdown" | "tab" ]

    popover = khufu.popover(
        tooltip=True,
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="report a bug or suggest a new feature",
        content=False,
        delay=20
    )

    bugTracker = khufu.a(
        content="""<i class="icon-bug3"></i>""",
        href="https://github.com/thespacedoctor/marshall_webapp_wiki/issues",
        openInNewTab=True,
        popover=popover
    )

    href = request.route_path('transients_search')
    searchbox = khufu.searchbox(
        size='xlarge',
        htmlId="q",
        placeHolder="search by object, gravity event or pi",
        navBar=True,
        pull='right',
        actionScript=href
    )

    insideNavList = khufu.nav_list(
        itemList=[
            marshallHome, xmatches, statsHome, pesstoHome, pesstoWiki, observingCalendar, pesstoGroups,
            pesstoDocs, finderChartsRepo, externalData, members, help, bugTracker],
        pull='left',  # [ False | 'right' | 'left' ]
        onPhone=True,
        onTablet=True,
        onDesktop=True,
    )

    outsideNavList = khufu.nav_list(
        itemList=[searchbox],
        pull='right',  # [ False | 'right' | 'left' ]
        onPhone=True,
        onTablet=True,
        onDesktop=True,
    )

    topNavBar = khufu.responsive_navigation_bar(
        shade='dark',
        brand=icon,
        loginDetails=username,
        outsideNavList=outsideNavList,
        insideNavList=insideNavList,
        htmlId=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.debug('completed the ``topNavigationBar`` function')

    return topNavBar
