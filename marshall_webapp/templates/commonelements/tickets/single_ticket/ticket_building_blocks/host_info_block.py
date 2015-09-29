#!/usr/local/bin/python
# encoding: utf-8
"""
host_info_block.py
=================
:Summary:
    The host info block for the object ticket

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
import datetime
from docopt import docopt
import khufu
import dryxPython.mysql as dms
from dryxPython import commonutils as dcu
from .....commonelements import commonutils as cu


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : November 20, 2013
# CREATED : November 20, 2013
# AUTHOR : DRYX


def host_info_block(
        log,
        request,
        discoveryDataDictionary):
    """get ticket host info block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.

    **Return:**
        - ``host_info_block`` -- the ticket identity block for the pesssto object

    """
    log.info('starting the ``host_info_block`` function')

    title = cu.block_title(
        log,
        title="host info"
    )

    masterName = discoveryDataDictionary["masterName"]
    sherlockClassification = discoveryDataDictionary["sherlockClassification"]

    nearestObjectUrl = ""
    exactLocationUrl = ""
    ogleStamp = ""
    ra = discoveryDataDictionary["raDeg"]
    dec = discoveryDataDictionary["decDeg"]
    transientBucketId = discoveryDataDictionary["transientBucketId"]
    if discoveryDataDictionary["sdss_coverage"] == 1:
        nearestObjectUrl = "http://skyserver.sdss3.org/public/en/tools/explore/obj.aspx?ra=%(ra)s&dec=%(dec)s" % locals(
        )
        exactLocationUrl = """http://skyserver.sdss3.org/public/en/tools/chart/image.aspx?ra=%(ra)s&dec=%(dec)s&scale=0.25&opt=GS&width=512&height=512""" % locals(
        )
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%s/sdss_stamp.jpeg" % (
            discoveryDataDictionary["transientBucketId"],))
        contextStamp = request.static_path(
            "marshall_webapp:static/caches/transients/%s/sdss_stamp.jpeg" % (
                discoveryDataDictionary["transientBucketId"],))
        stampName = "%(masterName)s_sdss_context_image" % locals()
    elif discoveryDataDictionary["ogle_color_context_stamp"] == 1:
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%(transientBucketId)s/ogle_color_context_stamp.png" % locals(
        ))
        contextStamp = request.static_path(
            "marshall_webapp:static/caches/transients/%(transientBucketId)s/ogle_color_context_stamp.png" % locals(
            ))
        ogleStamp = "OGLE context stamp"
        stampName = "%(masterName)s_ogle_context_image" % locals()
    elif discoveryDataDictionary["sdss_coverage"] == 0:
        contextStamp = 'holder.js/500x500/auto/industrial/text:not in sdss footprint'
        downloadContextStamp = contextStamp
        stampName = False
    else:
        contextStamp = 'holder.js/500x500/auto/industrial/text:sdss stamp not ready yet'
        downloadContextStamp = contextStamp
        stampName = False
    sdssUrl = """http://skyserver.sdss3.org/public/en/tools/chart/image.aspx?ra=%(ra)s&dec=%(dec)s&scale=0.25&opt=GSP&width=512&height=512&query=G""" % locals(
    )

    sdssLinkRow = ""
    if len(nearestObjectUrl):
        nearestObjectUrl = khufu.a(
            content='sdss nearest object',
            href=nearestObjectUrl,
            openInNewTab=True
        )
        nearestObjectUrl = khufu.coloredText(
            text=nearestObjectUrl,
            color="cyan",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )
        exactLocationUrl = khufu.a(
            content='exact sdss location',
            href=exactLocationUrl,
            openInNewTab=True
        )
        exactLocationUrl = khufu.coloredText(
            text=exactLocationUrl,
            color="blue",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )
        sdssLinkRow = khufu.grid_row(
            responsive=True,
            columns="&nbsp&nbsp&nbsp&nbsp%(ogleStamp)s%(exactLocationUrl)s<br>&nbsp&nbsp&nbsp&nbsp%(nearestObjectUrl)s" % locals(
            ),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

    if len(ogleStamp):
        ogleStamp = khufu.coloredText(
            text="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp%(ogleStamp)s" % locals(),
            color="blue"
        )

    sdssLink = khufu.a(
        content='sdss dr10 location',
        href=sdssUrl,
    )

    if stampName:
        href = request.route_path(
            'download', _query={'url': downloadContextStamp, "webapp": "marshall_webapp", "filename": stampName})
    else:
        href = False

    imageModal = khufu.imagingModal(
        log=log,
        imagePath=contextStamp,
        display="polaroid",  # [ rounded | circle | polaroid | False ]
        modalHeaderContent="Context Stamp for %(masterName)s" % locals(),
        modalFooterContent=sdssLink,
        stampWidth=180,
        modalImageWidth=400,
        downloadLink=href)
    imageModal = imageModal.get()

    redshift = ""
    if discoveryDataDictionary["hostRedshift"]:
        redshift = discoveryDataDictionary["hostRedshift"]
        littleTitle = cu.little_label(
            text="host redshift:"
        )

        redshift = khufu.coloredText(
            text=redshift,
            color="yellow",
            size=False,  # 1-10
        )

        redshift = khufu.grid_row(
            responsive=True,
            columns="%(littleTitle)s %(redshift)s" % locals(),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

    if sherlockClassification:
        littleTitle = cu.little_label(
            text="contextual classification:"
        )

        sherlockClassification = khufu.coloredText(
            text=sherlockClassification,
            color="violet",
            size=6,  # 1-10
        )

        sherlockClassification = khufu.grid_row(
            responsive=True,
            columns="%(littleTitle)s %(sherlockClassification)s" % locals(),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
    else:
        sherlockClassification = ""

    return "%(title)s %(imageModal)s %(sdssLinkRow)s %(redshift)s %(sherlockClassification)s" % locals()


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
