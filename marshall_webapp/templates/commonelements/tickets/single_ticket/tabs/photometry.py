#!/usr/local/bin/python
# encoding: utf-8
"""
photometry.py
=============
:Summary:
    The photometry tab for the PESSTO Object tickets

:Author:
    David Young

:Date Created:
    January 7, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import datetime
from docopt import docopt
from dryxPython import commonutils as dcu
import khufu
import dryxPython.mysql as dms
from .. import ticket_building_blocks


###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 7, 2014
# CREATED : January 7, 2014
# AUTHOR : DRYX


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
        - ``photometry_tab``

    **Todo**
        - @review: when complete, clean photometry_tab function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    from ... import single_ticket

    log.info('starting the ``photometry_tab`` function')

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

    # theseBlocks = [master_lightcurve_block]

    # thisRow = ""
    # blockCount = len(theseBlocks)
    # span = int(round(12. / (len(theseBlocks)) - 0.5))
    # remainingSpans = 12 - span * len(theseBlocks)
    # count = 1
    # for block in theseBlocks:
    #     thisSpan = span
    #     if count <= remainingSpans:
    #         thisSpan = span + 1
    #     count += 1
    #     block = khufu.grid_column(
    # span=thisSpan,  # 1-12
    # offset=0,  # 1-12
    #         content=block,
    # pull=False,  # ["right", "left", "center"]
    #         htmlId=False,
    #         htmlClass=False,
    #         onPhone=True,
    #         onTablet=True,
    #         onDesktop=True
    #     )
    #     thisRow = """%(thisRow)s %(block)s""" % locals()

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

    log.info('completed the ``photometry_tab`` function')
    return "%(photometry_tab)s" % locals()


# LAST MODIFIED : November 20, 2013
# CREATED : November 20, 2013
# AUTHOR : DRYX

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

    **Todo**
    # @review: when complete, clean photometry_footer_bar function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    import datetime
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu
    import dryxPython.mysql as dms
    import dryxPython.astrotools as dat
    import dryxPython.commonutils as dcu

    log.info('starting the ``photometry_footer_bar`` function')
    ## VARIABLES ##
    transientBucketId = discoveryDataDictionary["transientBucketId"]
    name = discoveryDataDictionary["masterName"]

    lightCurveImage = False
    # if lsqname:
    #     lightCurveImage = request.static_url('marshall_webapp:static/cache/transients/%s/master_lightcurve.pdf' % (
    #         discoveryDataDictionary["transientBucketId"],))
    # else:
    #     lightCurveImage = False

    # Override for LSQ lightcurves
    if discoveryDataDictionary["lsq_lightcurve"]:
        transientBucketId = discoveryDataDictionary["transientBucketId"]
        lightCurveImage = request.static_url('marshall_webapp:static/caches/transients/%(transientBucketId)s/lsq_lightcurve.gif' % locals(
        ))

    from datetime import datetime, date, time
    now = datetime.now()
    now = now.strftime("%Y%m%dt%H%M%S")
    fileName = """%(name)s_lightcurve_%(now)s.pdf""" % locals()

    if lightCurveImage is not False:
        popover = khufu.popover(
            tooltip=True,
            placement="top",  # [ top | bottom | left | right ]
            trigger="click",  # [ False | click | hover | focus | manual ]
            title="download lightcurve pdf",
            content=False,
            delay=100
        )

        downloadFileButton = khufu.button(
            buttonText="""<i class="icon-file-pdf"></i>""",
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='primary',
            buttonSize='small',  # [ large | default | small | mini ]
            htmlId=False,
            href="/marshall/scripts/python/download_file.py?url=%(lightCurveImage)s&fileName=%(fileName)s" % locals(
            ),
            pull=False,  # right, left, center
            submit=False,
            block=False,
            disable=False,
            dataToggle=False,  # [ modal ]
            popover=popover
        )
    else:
        downloadFileButton = ""

    ########

    format = ["json", "csv", "plain_table"]
    text = ["json", "csv", "plain text"]

    linkList = ""
    for f, t in zip(format, text):
        params = dict(request.params)
        params["format"] = f
        params["filename"] = "%(name)s_lightcurve" % locals()
        href = request.route_path(
            'transientLightcurves', elementId=transientBucketId, _query=params)
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
    lsqname = False
    href = ""
    lightcurveSwitchAttempt = True
    for row in lightcurveData:
        if row["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and "lsq-disc" in row["survey"].lower():
            lightcurveSwitchAttempt = False

    if lightcurveSwitchAttempt == True:
        if "lsq" in name.lower():
            lsqname = name
        else:
            for aka in objectAkas:
                if aka["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and "lsq" in aka["name"].lower():
                    lsqname = aka["name"]
                    break
    if lsqname:
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

        thisImage = "/static/caches/transients/%(transientBucketId)s/lsq_lightcurve.gif" % locals(
        )
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
        delay=200
    )

    downloadFileButton = khufu.button(
        buttonText="""<i class="icon-save"></i>""",
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='primary',
        buttonSize='small',  # [ large | default | small | mini ]
        htmlId=False,
        href=False,
        pull=False,  # right, left, center
        submit=False,
        block=False,
        disable=False,
        dataToggle=False,  # [ modal ]
        popover=popover
    )

    ########

    buttonGroup = khufu.buttonGroup(
        buttonList=[downloadFileButton],
        format='default'  # [ default | toolbar | vertical ]
    )

    footerColumn = khufu.grid_column(
        span=2,  # 1-12
        offset=0,  # 1-12
        content="%(buttonGroup)s" % locals(
        ),
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    photometry_footer_bar = khufu.grid_row(
        responsive=True,
        columns=footerColumn,
        htmlId=False,
        htmlClass="ticketFooter",
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    return photometry_footer_bar


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
