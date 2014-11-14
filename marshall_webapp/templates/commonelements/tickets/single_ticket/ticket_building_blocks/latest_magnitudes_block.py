#!/usr/local/bin/python
# encoding: utf-8
"""
latest_magnitudes_block.py
===========================
:Summary:
    The latest magnitudes block for the object ticket

:Author:
    David Young

:Date Created:
    March 26, 2014 

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import commonutils as dcu
from .....commonelements import commonutils as cu
import datetime as datetime

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : March 26, 2014
# CREATED : March 26, 2014
# AUTHOR : DRYX


def latest_magnitudes_block(
        log,
        request,
        discoveryDataDictionary,
        lightcurveData,
        displayTitle=True):
    """get ticket lightcurve block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage

    **Return:**
        - ``latest_magnitudes_block`` -- the ticket identity block for the pesssto object

    **Todo**
    # @review: when complete, clean latest_magnitudes_block function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu
    import dryxPython.mysql as dms

    log.info('starting the ``latest_magnitudes_block`` function')
    ## VARIABLES ##

    if displayTitle:
        title = cu.block_title(
            log,
            title="latest magnitudes"
        )
    else:
        title = ""

    # get current magnitude estimate
    currentMagEstimate = discoveryDataDictionary["currentMagnitudeEstimate"]
    currentMagEstimateUpdated = discoveryDataDictionary[
        "currentMagnitudeEstimateUpdated"]

    if currentMagEstimateUpdated and currentMagEstimate != 9999:
        now = datetime.datetime.now()
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

    # get latest magnitudes
    littleTitle = """<span class="colortext grey littlelabel  ">lastest magnitude:</span>"""
    numOfPointsToDisplay = 5
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
            offset=1,  # 1-12
            content=mag,
            pull=False,  # ["right", "left", "center"]
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        # if len(magnitudes) < 1:
        #     mag = """%(littleTitle)s %(mag)s""" % locals()

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

    return "%(title)s %(magnitudes)s %(currentMagEstimate)s" % locals()


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
