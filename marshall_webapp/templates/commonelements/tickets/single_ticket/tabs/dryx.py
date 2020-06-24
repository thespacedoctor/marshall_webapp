#!/usr/local/bin/python
# encoding: utf-8
"""
*The dryx tab for the PESSTO Object tickets*

:Author:
    David Young
"""
import sys
import os
import re
import datetime
import khufu

def dryx_tab(
        log,
        request,
        discoveryDataDictionary,
        objectAkas,
        atelData,
        objectHistories):
    """dryx tab

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
    - ``objectAkas`` -- object akas
    - ``objectHistories`` -- the lightcurve data for the objects displayed on the webpage
    - ``atelData`` -- the atel matches for the objects displayed on the webpage
    

    **Return**

    - ``dryx_tab`` -- for each transient ticket in the transient listings pages
    
    """
    from time import strftime
    from marshall_webapp.templates.commonelements.tickets.single_ticket import ticket_building_blocks, tabs
    from marshall_webapp.templates.commonelements.tickets import single_ticket
    from marshall_webapp.templates.commonelements import forms

    log.debug('starting the ``dryx_tab`` function')

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

    # ADD TEXT COLOR
    currentMagnitude = khufu.coloredText(
        text="currentMagnitudeEstimate: %(currentMagnitudeEstimate)s (%(currentMagnitudeDate)s)" % locals(
        ),
        color="grey",
        size=3,  # 1-10
        pull=False,  # "left" | "right",
        addBackgroundColor=False
    )

    # ADD TEXT COLOR
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

    log.debug('completed the ``dryx_tab`` function')
    return dryx_tab

# xt-def-with-logger
