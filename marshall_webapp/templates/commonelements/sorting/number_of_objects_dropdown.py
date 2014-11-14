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
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
from docopt import docopt
from dryxPython import commonutils as dcu
import khufu


###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : February 20, 2014
# CREATED : February 20, 2014
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def number_of_objects_dropdown(
    log,
    thisUrl,
    limit,
    tableView
):
    """number_of_objects_dropdown

    **Key Arguments:**
        - ``log`` -- the logger
        - ``thisUrl`` -- the current url for the page
        - ``limit`` -- current limit of objects per page
        - ``tableView`` -- the current tableView

    **Return:**
        - ``objectsPerPageDropdown``

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    # determine which icon to use:
    if tableView == "table":
        icon = """<i class="icon-reorder"></i>"""
    else:
        icon = """<i class="icon-ticket2"></i>"""

    urlCopy = thisUrl
    if "limit" in urlCopy:
        urlCopy = re.sub(r"&?limit=\d+", "", urlCopy)
    if "pageStart" in urlCopy:
        urlCopy = re.sub(r"&?pageStart=\d+", "", urlCopy)

    if "?" not in urlCopy:
        urlCopy = "%(urlCopy)s?" % locals()
    if "&" != urlCopy[-1:] and "?" != urlCopy[-1:]:
        urlCopy = "%(urlCopy)s&" % locals()

    numbers = ["10", "25", "50", "100"]
    listItems = []
    for number in numbers:
        item = "%(urlCopy)slimit=%(number)s&pageStart=0" % locals()
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
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="set the number of objects to be displayed on each page",
        content=False,
        delay=200
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
