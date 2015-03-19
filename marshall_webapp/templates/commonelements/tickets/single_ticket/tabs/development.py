#!/usr/local/bin/python
# encoding: utf-8
"""
development.py
===========
:Summary:
    The development tab for the PESSTO Object tickets

:Author:
    David Young

:Date Created:
    January 7, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import datetime
from docopt import docopt
import khufu
from dryxPython import commonutils as dcu
import dryxPython.mysql as dms


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 7, 2014
# CREATED : January 7, 2014
# AUTHOR : DRYX


def development_tab(
        log,
        request,
        discoveryDataDictionary,
        objectAkas,
        atelData,
        objectHistories):
    """development tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectAkas`` -- object akas
        - ``objectHistories`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage

    **Return:**
        - ``development_tab`` -- for each transient ticket in the transient listings pages

    **Todo**
    """
    ################ > IMPORTS ################
    from time import strftime
    from .. import ticket_building_blocks
    from .. import tabs
    from ... import single_ticket
    from .....commonelements import forms

    log.info('starting the ``development_tab`` function')

    group = ""
    for item in request.effective_principals:
        if "group:" in item:
            group = item.replace("group:", "")
    if group not in ["superadmin"]:
        return None

    lightcurve = transient_d3_lightcurve(
        log=log
    )

    development_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=False,
        blockList=[lightcurve],
        tabFooter=False,
        htmlId="developmenttab"
    )

    # convert bytes to unicode
    if isinstance(development_tab, str):
        development_tab = unicode(
            development_tab, encoding="utf-8", errors="replace")

    log.info('completed the ``development_tab`` function')
    return development_tab

# use the tab-trigger below for new function
# LAST MODIFIED : March 19, 2015
# CREATED : March 19, 2015
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def transient_d3_lightcurve(
        log):
    """transient d3 lightcurve

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        # copy usage method(s) here and select the following snippet from the command palette:
        # x-setup-docstring-keys-from-selected-usage-options

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean transient_d3_lightcurve function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``transient_d3_lightcurve`` function')

    svg = khufu.svg.svg(
        htmlClass=False,
        csvUrl="#",
        disable=False,
        htmlId=False,
        chartType="",
        span=12
    )

    log.info('completed the ``transient_d3_lightcurve`` function')
    return svg

# use the tab-trigger below for new function
# xt-def-with-logger


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
