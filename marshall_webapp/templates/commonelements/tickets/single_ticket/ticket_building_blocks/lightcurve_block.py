#!/usr/local/bin/python
# encoding: utf-8
"""
lightcurve_block.py
=================
:Summary:
    The lightcurve block for the object ticket

:Author:
    David Young

:Date Created:
    November 20, 2013

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import datetime as datetime
from docopt import docopt
from dryxPython import commonutils as dcu
from .....commonelements import commonutils as cu
import khufu
import dryxPython.mysql as dms


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : November 20, 2013
# CREATED : November 20, 2013
# AUTHOR : DRYX


def lightcurve_block(
        log,
        request,
        discoveryDataDictionary,
        lightcurveData,
        objectAkas,
        displayTitle=True,
        offset=2):
    """get ticket lightcurve block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``objectAkas`` -- the transient object akas
        - ``displayTitle`` -- display the title for this block?
        - ``offset`` -- the offset for the block

    **Return:**
        - ``lightcurve_block`` -- the ticket identity block for the pesssto object

    **Todo**
    """
    log.info('starting the ``lightcurve_block`` function')

    masterName = discoveryDataDictionary["masterName"]

    if displayTitle:
        title = cu.block_title(
            log,
            title="lightcurve"
        )
    else:
        title = ""

    lightCurveImage = ""
    dlightCurveImage = ""

    if discoveryDataDictionary["master_pessto_lightcurve"]:
        lightCurveImage = request.static_url(
            'marshall_webapp:static/caches/transients/%s/master_lightcurve.png' % (
                discoveryDataDictionary["transientBucketId"],))
        dlightCurveImage = '/static/caches/transients/%s/master_lightcurve.png' % (
            discoveryDataDictionary["transientBucketId"],)

    # Override for LSQ lightcurves
    lsqname = False
    lightcurveSwitchAttempt = True
    for row in lightcurveData:
        if row["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and "lsq-disc" in row["survey"].lower():
            lightcurveSwitchAttempt = False

    if lightcurveSwitchAttempt == True:
        if "lsq" in masterName.lower():
            lsqname = masterName
        else:
            for aka in objectAkas:
                if aka["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and "lsq" in aka["name"].lower():
                    lsqname = aka["name"]
                    break

    if lsqname:
        transientBucketId = discoveryDataDictionary["transientBucketId"]
        lightCurveImage = request.static_url(
            'marshall_webapp:static/caches/transients/%(transientBucketId)s/lsq_lightcurve.gif' % locals(
            ))
        dlightCurveImage = '/static/caches/transients/%(transientBucketId)s/lsq_lightcurve.gif' % locals(
        )

    if len(lightCurveImage):
        href = request.route_path(
            'download', _query={'url': dlightCurveImage, "webapp": "marshall_webapp", "filename": "%(masterName)s_master_lightcurve" % locals()})
        lightCurveImage = khufu.imagingModal(
            log=log,
            imagePath=lightCurveImage,
            display="polaroid",  # [ rounded | circle | polaroid | False ]
            modalHeaderContent="Lightcurve for %(masterName)s" % locals(),
            modalFooterContent="",
            stampWidth=180,
            modalImageWidth=400,
            downloadLink=href)
        lightCurveImage = lightCurveImage.get()

    else:
        lightCurveImage = khufu.image(
            # [ industrial | gray | social ]
            src="""holder.js/190x190/auto/industrial/text:master lightcurve not ready""",
            display="polaroid",  # [ rounded | circle | polaroid | False ]
        )

    # get current magnitude estimate
    currentMagEstimate = discoveryDataDictionary["currentMagnitudeEstimate"]
    currentMagEstimateUpdated = discoveryDataDictionary[
        "currentMagnitudeEstimateUpdated"]

    now = datetime.datetime.now()
    if currentMagEstimate == 9999:
        for dataPoint in lightcurveData:
            if dataPoint["transientBucketId"] == discoveryDataDictionary["transientBucketId"]:
                break
        if now - dataPoint["observationDate"] < datetime.timedelta(days=7):
            currentMagEstimate = dataPoint["magnitude"]
    if currentMagEstimateUpdated and currentMagEstimate != 9999:

        if now - currentMagEstimateUpdated < datetime.timedelta(days=2):
            littleTitle = cu.little_label(
                text="current mag estimate:"
            )
            # add text color
            if currentMagEstimate > 21.:
                text = "&nbsp&nbsp> 21.0"
            else:
                text = "&nbsp&nbsp%(currentMagEstimate)0.2f" % locals()
            currentMagEstimate = khufu.coloredText(
                text=text,
                color="violet",
                size=7,  # 1-10
                pull=False,  # "left" | "right"
            )
            currentMagEstimateUpdated = khufu.coloredText(
                text=currentMagEstimateUpdated,
                color="red",
                size=False,  # 1-10
                pull=False,  # "left" | "right"
            )
            currentMagEstimate = khufu.grid_row(
                responsive=True,
                columns="%(littleTitle)s %(currentMagEstimate)s" % locals()
            )
        else:
            currentMagEstimate = ""

    else:
        currentMagEstimate = ""

    # get three latest magnitudes
    littleTitle = """<span class="colortext grey littlelabel  ">lastest magnitude:</span>"""
    numOfPointsToDisplay = 1
    count = 0
    rows = []
    magnitudes = ""
    for dataPoint in lightcurveData:
        if dataPoint["transientBucketId"] == discoveryDataDictionary["transientBucketId"]:
            row = dataPoint
            rows.append(row)
            count += 1
            if count >= numOfPointsToDisplay:
                break

    for row in rows:
        ffilter = ""
        if row["filter"]:
            ffilter = row["filter"]
            ffilter = """%(ffilter)s-band""" % locals()

        survey = khufu.coloredText(
            text="""%s %s""" % (row["survey"], ffilter, ),
            color="orange",
            size=3,
            pull="left"
        )
        relDate = dcu.pretty_date(
            date=row["observationDate"]
        )
        dateObs = khufu.coloredText(
            text="""%s""" % (
                str(row["observationDate"])[0:10],),
            color="violet",
            pull="left",
            size=2
        )
        relDate = khufu.coloredText(
            text="""  %s""" % (relDate[1:]),
            color="magenta",
            pull="left",
            size=2
        )
        survey = khufu.grid_row(
            responsive=True,
            columns=survey
        )
        dateObs = khufu.grid_row(
            responsive=True,
            columns="%(dateObs)s %(relDate)s" % locals()
        )
        info = khufu.grid_column(
            span=6,  # 1-12
            offset=0,  # 1-12
            content="%(survey)s %(dateObs)s" % locals(),
            pull="left",  # ["right", "left", "center"]
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        if row["magnitude"]:
            mag = khufu.coloredText(
                text="""%4.2f""" % (row["magnitude"],),
                color="green",
                size=6,
                pull="right"
            )
        else:
            mag = khufu.coloredText(
                text="""%s""" % (row["magnitude"],),
                color="green",
                size=6,
                pull="right"
            )

        mag = khufu.grid_column(
            span=3,  # 1-12
            offset=offset,  # 1-12
            content=mag,
            pull=False,  # ["right", "left", "center"]
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        thisMag = khufu.grid_row(
            responsive=True,
            columns="%(mag)s %(info)s" % locals(),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        magnitudes = "%(magnitudes)s %(thisMag)s" % locals()

    magnitudes = "%(littleTitle)s<span>%(magnitudes)s</span>" % locals()

    return "%(title)s %(lightCurveImage)s %(magnitudes)s %(currentMagEstimate)s" % locals()


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
