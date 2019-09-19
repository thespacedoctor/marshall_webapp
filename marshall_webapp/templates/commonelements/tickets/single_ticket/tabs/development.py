#!/usr/local/bin/python
# encoding: utf-8
"""
*The development tab for the PESSTO Object tickets*

:Author:
    David Young

:Date Created:
    January 7, 2014
"""
import sys
import os
import re
import datetime
import khufu


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
    """
    from time import strftime
    from marshall_webapp.templates.commonelements.tickets.single_ticket import ticket_building_blocks, tabs
    from marshall_webapp.templates.commonelements.tickets import single_ticket
    from marshall_webapp.templates.commonelements import forms

    log.debug('starting the ``development_tab`` function')

    group = ""
    for item in request.effective_principals:
        if "group:" in item:
            group = item.replace("group:", "")
    if group not in ["superadmin"]:
        return None

    lightcurve = transient_d3_lightcurve(
        log=log,
        discoveryDataDictionary=discoveryDataDictionary,
        request=request
    )

    development_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=False,
        blockList=[lightcurve],
        tabFooter=False,
        htmlId="developmenttab"
    )

    # CONVERT BYTES TO UNICODE
    if isinstance(development_tab, str):
        development_tab = unicode(
            development_tab, encoding="utf-8", errors="replace")

    log.debug('completed the ``development_tab`` function')
    return development_tab


def transient_d3_lightcurve(
        log,
        discoveryDataDictionary,
        request):
    """transient d3 lightcurve

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
    """
    log.debug('starting the ``transient_d3_lightcurve`` function')

    # print discoveryDataDictionary["transientBucketId"]

    href = request.route_path('transients_element_lightcurves', elementId=discoveryDataDictionary[
                              "transientBucketId"], _query={'format': 'd3'})

    svg = khufu.svg.svg(
        htmlClass="example01",
        dataUrl=href,
        dataFormat="json",
        disable=False,
        htmlId=False,
        chartType="lightcurve",
        span=7,
        height="square"
    )

    log.debug('completed the ``transient_d3_lightcurve`` function')
    return svg


# xt-def-with-logger
