#!/usr/local/bin/python
# encoding: utf-8
"""
*The photometry tab for the PESSTO Object tickets*

:Author:
    David Young

:Date Created:
    January 7, 2014
"""
import sys
import os
import datetime
import re
import khufu
from marshall_webapp.templates.commonelements.tickets.single_ticket import ticket_building_blocks


def photometry_tab(
        log,
        request,
        discoveryDataDictionary,
        objectAkas,
        atelData,
        lightcurveData):
    """photometry tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectAkas`` -- object akas
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage

    **Return:**
        - ``photometry_tab`` -- the lightcurve/photometry tab for a single ticket on the transient listings page
    """
    from marshall_webapp.templates.commonelements.tickets import single_ticket

    log.debug('starting the ``photometry_tab`` function')

    master_lightcurve_block = ticket_building_blocks.master_lightcurve_block.master_lightcurve_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        lightcurveData=lightcurveData,
        objectAkas=objectAkas
    )

    master_lightcurve_block = khufu.grid_column(
        span=6,  # 1-12
        offset=0,  # 1-12
        content=master_lightcurve_block,
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    latest_magnitudes_block = ticket_building_blocks.latest_magnitudes_block.latest_magnitudes_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        lightcurveData=lightcurveData
    )

    latest_magnitudes_block = khufu.grid_column(
        span=2,  # 1-12
        offset=0,  # 1-12
        content=latest_magnitudes_block,
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    survey_lightcurves_block = ticket_building_blocks.survey_lightcurves_block.survey_lightcurves_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        lightcurveData=lightcurveData,
    )

    survey_lightcurves_block = khufu.grid_column(
        span=2,  # 1-12
        offset=0,  # 1-12
        content=survey_lightcurves_block,
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass="surveyLightcurvesBlock",
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    photometry_block = """%(master_lightcurve_block)s%(latest_magnitudes_block)s%(survey_lightcurves_block)s""" % locals(
    )

    footer = photometry_footer_bar(
        log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas,
        lightcurveData=lightcurveData)

    photometry_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=False,
        blockList=[photometry_block],
        tabFooter=footer,
        htmlId="photometrytab"
    )

    log.debug('completed the ``photometry_tab`` function')
    return "%(photometry_tab)s" % locals()


def photometry_footer_bar(
        log,
        request,
        discoveryDataDictionary,
        objectAkas,
        lightcurveData):
    """get ticket footer bar

    **Key Arguments:**
        - ``log`` -- logger
        - ``discoveryData`` -- the discoveryData for the object
        - ``lightcurveData`` -- the lightcurve data for the object

    **Return:**
        - ``photometry_footer_bar`` -- the ticket footer bar for the pesssto object
    """
    lsqExists = False
    log.debug('starting the ``photometry_footer_bar`` function')
    ## VARIABLES ##
    transientBucketId = discoveryDataDictionary["transientBucketId"]
    name = discoveryDataDictionary["masterName"]
    format = ["json", "csv", "plain_table"]
    text = ["json", "csv", "plain text"]

    linkList = ""
    for f, t in zip(format, text):
        params = dict(request.params)
        params["format"] = f
        params["filename"] = "%(name)s_lightcurve" % locals()
        href = request.route_path(
            'transients_element_lightcurves', elementId=transientBucketId, _query=params)
        link = khufu.a(
            content=t,
            href=href
        )
        link = khufu.p(
            content=link,
            textAlign="center",  # [ left | center | right ]
        )
        linkList = """%(linkList)s%(link)s""" % locals()

    # Override for LSQ lightcurves
    href = ""
    lightcurveSwitchAttempt = True
    transientBucketId = discoveryDataDictionary["transientBucketId"]
    for row in lightcurveData:
        if row["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and row["survey"] and "lsq-disc" in row["survey"].lower():
            lightcurveSwitchAttempt = False

    if lightcurveSwitchAttempt == True:
        filePath = request.registry.settings["downloads"][
            "transient cache directory"] + "/%(transientBucketId)s/lsq_lightcurve.gif" % locals()
        if "lsq" in name.lower() and "lsq" in discoveryDataDictionary["survey"]:
            lsqname = name
        else:
            for aka in objectAkas:
                if aka["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and "lsq" in aka["name"].lower():
                    lsqname = aka["name"]
                    break
        if "lsqname" in locals():
            lsqExists = os.path.exists(filePath)

    if lsqExists:
        username = request.registry.settings["credentials"]["lsq"]["username"]
        password = request.registry.settings["credentials"]["lsq"]["password"]
        href = "http://%(username)s:%(password)s@portal.nersc.gov/project/lssn/ms_lcs/%(lsqname)s.extra_out_LSQgr" % locals()
        link = khufu.a(
            content="lsq plain text",
            href=href
        )
        link = khufu.p(
            content=link,
            textAlign="center",  # [ left | center | right ]
        )
        linkList = """%(linkList)s%(link)s""" % locals()

        thisImage = request.static_path("marshall_webapp:static/caches/transients/%(transientBucketId)s/lsq_lightcurve.gif" % locals(
        ))
        filename = "%(name)s_lsq_lightcurve" % locals()
        href = request.route_path(
            'download', _query={'url': thisImage, "webapp": "marshall_webapp", "filename": filename})

        link = khufu.a(
            content="lsq image",
            href=href
        )
        link = khufu.p(
            content=link,
            textAlign="center",  # [ left | center | right ]
        )
        linkList = """%(linkList)s%(link)s""" % locals()

    popover = khufu.popover(
        tooltip=False,
        placement="top",  # [ top | bottom | left | right ]
        trigger="click hover",  # [ False | click | hover | focus | manual ]
        title="download lightcurve",
        content=linkList,
        delay=20
    )

    downloadFileButton = khufu.button(
        buttonText="""<i class="icon-save"></i>""",
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='primary',
        buttonSize='small',  # [ large | default | small | mini ]
        popover=popover
    )

    footerColumn = khufu.grid_column(
        span=2,  # 1-12
        offset=0,  # 1-12
        content="%(downloadFileButton)s" % locals(
        )
    )

    photometry_footer_bar = khufu.grid_row(
        responsive=True,
        columns=footerColumn,
        htmlId=False,
        htmlClass="ticketFooter"
    )

    return photometry_footer_bar
