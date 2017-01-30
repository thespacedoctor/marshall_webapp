#!/usr/local/bin/python
# encoding: utf-8
"""
dryx.py
===========
:Summary:
    The dryx tab for the PESSTO Object tickets

:Author:
    David Young

:Date Created:
    January 7, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

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

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 7, 2014
# CREATED : January 7, 2014
# AUTHOR : DRYX


def dryx_tab(
        log,
        request,
        discoveryDataDictionary,
        objectAkas,
        atelData,
        objectHistories):
    """dryx tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectAkas`` -- object akas
        - ``objectHistories`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage

    **Return:**
        - ``dryx_tab`` -- for each transient ticket in the transient listings pages

    **Todo**
    """
    ################ > IMPORTS ################
    from time import strftime
    from .. import ticket_building_blocks
    from .. import tabs
    from ... import single_ticket
    from .....commonelements import forms

    log.info('starting the ``dryx_tab`` function')

    group = ""
    for item in request.effective_principals:
        if "group:" in item:
            group = item.replace("group:", "")
    if group not in ["superadmin"]:
        return None

    lastReviewedMag = discoveryDataDictionary["lastReviewedMag"]
    lastReviewDate = discoveryDataDictionary["lastTimeReviewed"]
    currentMagnitudeDate = discoveryDataDictionary["currentMagnitudeDate"]
    currentMagnitudeEstimate = discoveryDataDictionary[
        "currentMagnitudeEstimate"]

    # add text color
    currentMagnitude = khufu.coloredText(
        text="currentMagnitudeEstimate: %(currentMagnitudeEstimate)s (%(currentMagnitudeDate)s)" % locals(
        ),
        color="grey",
        size=3,  # 1-10
        pull=False,  # "left" | "right",
        addBackgroundColor=False
    )

    # add text color
    lastReviewedMag = khufu.coloredText(
        text="lastReviewMag: %(lastReviewedMag)s (%(lastReviewDate)s)" % locals(
        ),
        color="grey",
        size=3,  # 1-10
        pull=False,  # "left" | "right",
        addBackgroundColor=False
    )

    dryx_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=False,
        blockList=[lastReviewedMag, currentMagnitude],
        tabFooter=False,
        htmlId="dryxtab"
    )

    # convert bytes to unicode
    if isinstance(dryx_tab, str):
        dryx_tab = unicode(
            dryx_tab, encoding="utf-8", errors="replace")

    log.info('completed the ``dryx_tab`` function')
    return dryx_tab

# use the tab-trigger below for new function
# xt-def-with-logger


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
