#!/usr/local/bin/python
# encoding: utf-8
"""
number_of_objects_dropdown.py
=============================
:Summary:
    Dropdown to select the numnber of objects to be displayed on a page

:Author:
    David Young

:Date Created:
    February 20, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
from docopt import docopt
from dryxPython import commonutils as dcu
import khufu


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : February 20, 2014
# CREATED : February 20, 2014
# AUTHOR : DRYX

def number_of_objects_dropdown(
    log,
    request,
    limit,
    tableView
):
    """number_of_objects_dropdown

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the request
        - ``limit`` -- current limit of objects per page
        - ``tableView`` -- the current tableView

    **Return:**
        - ``objectsPerPageDropdown``

    **Todo**
    """
    routename = request.matched_route.name
    if "elementId" in request.matchdict:
        elementId = request.matchdict["elementId"]
    else:
        elementId = False

    theseParams = dict(request.params)

    alist = ["limit", "pageStart"]
    for i in alist:
        if i in theseParams:
            del theseParams[i]

    # determine which icon to use:
    if tableView == "table":
        icon = """<i class="icon-reorder"></i>"""
    else:
        icon = """<i class="icon-ticket2"></i>"""

    numbers = ["10", "25", "50", "100"]
    listItems = []
    for number in numbers:
        theseParams["limit"] = number
        theseParams["pageStart"] = 0
        item = request.route_path(
            routename, elementId=elementId, _query=theseParams)
        item = khufu.a(
            content="""%(icon)s x %(number)s""" % locals(),
            href=item,
        )
        item = khufu.li(
            content=item,
        )
        listItems.append(item)

    popover = khufu.popover(
        tooltip=True,
        placement="left",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="set the number of objects to be displayed on each page",
        content=False,
        delay=2000
    )

    objectsPerPageDropdown = khufu.dropdown(
        buttonSize='default',
        buttonColor='default',  # [ default | sucess | error | warning | info ]
        menuTitle="""%(icon)s x %(limit)s""" % locals(),
        linkList=listItems,
        pull="right",
        direction='down',  # [ down | up ]
        htmlId="objectsPerPageDropdown",
        popover=popover
    )

    return objectsPerPageDropdown

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
