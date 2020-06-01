#!/usr/local/bin/python
# encoding: utf-8
"""
*The host info block for the object ticket*

:Author:
    David Young

:Date Created:
    November 20, 2013
"""
import sys
import os
import re
import datetime
import numpy as np
import khufu
import collections
from marshall_webapp.templates.commonelements import commonutils as cu


def host_info_block(
        log,
        request,
        discoveryDataDictionary,
        transientCrossmatches):
    """get ticket host info block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
        - ``transientCrossmatches`` -- info from the transient crossmatcher

    **Return:**
        - ``host_info_block`` -- the ticket identity block for the pesssto object
    """
    log.debug('starting the ``host_info_block`` function')

    title = cu.block_title(
        log,
        title="host info"
    )

    transientBucketId = discoveryDataDictionary["transientBucketId"]
    masterName = discoveryDataDictionary["masterName"]
    sherlockClassification = discoveryDataDictionary["classification"]
    sherlockAnnotation = discoveryDataDictionary["annotation"]

    if sherlockAnnotation:

        sherlockAnnotation = khufu.coloredText(
            text=" - " + sherlockAnnotation,
            color="green",
            size=2,
        )

    else:
        sherlockAnnotation = ""

    nearestObjectUrl = ""
    exactLocationUrl = ""
    ogleStamp = ""
    ra = discoveryDataDictionary["raDeg"]
    dec = discoveryDataDictionary["decDeg"]

    contextMaps = {}

    contextMaps = collections.OrderedDict(sorted(contextMaps.items()))

    if discoveryDataDictionary["sdss_coverage"] == 1:
        nearestObjectUrl = "http://skyserver.sdss3.org/public/en/tools/explore/obj.aspx?ra=%(ra)s&dec=%(dec)s" % locals(
        )
        exactLocationUrl = """http://skyserver.sdss3.org/public/en/tools/chart/image.aspx?ra=%(ra)s&dec=%(dec)s&scale=0.25&opt=GS&width=512&height=512""" % locals(
        )

    if discoveryDataDictionary["ps1_map"] == 1:
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%s/ps1_map_color.jpeg" % (
            discoveryDataDictionary["transientBucketId"],))
        contextStamp = downloadContextStamp
        contextMaps["PS1"] = contextStamp
        stampName = "%(masterName)s_ps1_context_image" % locals()
    if discoveryDataDictionary["sdss_coverage"] == 1:
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%s/sdss_stamp.jpeg" % (
            discoveryDataDictionary["transientBucketId"],))
        contextStamp = downloadContextStamp
        contextMaps["SDSS DR12"] = contextStamp
        stampName = "%(masterName)s_sdss_context_image" % locals()
    if discoveryDataDictionary["ogle_color_context_stamp"] == 1:
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%(transientBucketId)s/ogle_color_context_stamp.png" % locals(
        ))
        contextStamp = downloadContextStamp
        contextMaps["OGLE"] = contextStamp
        ogleStamp = "OGLE context stamp"
        ogleStamp = khufu.coloredText(
            text="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp%(ogleStamp)s" % locals(),
            color="blue"
        )
        stampName = "%(masterName)s_ogle_context_image" % locals()

    if len(contextMaps) == 0:
        downloadContextStamp = 'holder.js/500x500/auto/industrial/text:no context stamp'
        contextStamp = downloadContextStamp
        contextMaps["PLACEHOLDER"] = contextStamp
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

    sdssLink = khufu.a(
        content='sdss dr12 location',
        href=sdssUrl,
    )

    if len(contextMaps) > 0:
        for k, v in contextMaps.items():
            stampName = "%(masterName)s_%(k)s_context_image" % locals()
            stampName = stampName.lower()
            contextStamp = v
            break
        noModal = False

        href = request.route_path(
            'download', _query={'url': downloadContextStamp, "webapp": "marshall_webapp", "filename": stampName})
    else:
        href = False
        contextStamp = contextMaps["PLACEHOLDER"]
        noModal = True

    allImage = ""
    count = 0
    for k, v in contextMaps.items():
        count += 1
        reminderImages = len(contextMaps) % 3
        if reminderImages == 0:
            span = 4
            offset = 0
        elif count < (len(contextMaps) - reminderImages):
            span = 4
            offset = 0
        elif reminderImages == 2:
            span = 6
            offset = 0
        else:
            span = 6
            offset = 3

        thisImage = khufu.image(
            src=v,  # [ industrial | gray | social ]
            href=False,
            display="rounded",  # [ rounded | circle | polaroid | False ]
            pull=False,  # [ "left" | "right" | "center" | False ]
            htmlClass=False,
            width="90%"
        )
        thisImage = khufu.grid_row(
            responsive=True,
            columns=thisImage,
        )
        # add text color
        name = khufu.coloredText(
            text=k,
            color="blue",
            size=7,  # 1-10
            pull=False,  # "left" | "right",
            addBackgroundColor=False
        )

        name = khufu.grid_row(
            responsive=True,
            columns=name,
        )
        column = khufu.grid_column(
            span=span,  # 1-12
            offset=offset,  # 1-12
            content=thisImage + name,
            pull=False,  # ["right", "left", "center"]
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        allImage += column

    grid_row = khufu.grid_row(
        responsive=True,
        columns=allImage,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    randNum = int(np.random.rand() * 10000)
    modal = khufu.modal(
        modalHeaderContent="Context Maps for %(masterName)s" % locals(
        ),
        modalBodyContent=grid_row,
        modalFooterContent="",
        htmlId="hookId%(randNum)s" % locals(),
        centerContent=True
    )
    imageModal = khufu.image(
        src=contextStamp,  # [ industrial | gray | social ]
        href="#hookId%(randNum)s" % locals(),
        display="rounded",  # [ rounded | circle | polaroid | False ]
        pull=False,  # [ "left" | "right" | "center" | False ]
        htmlClass=False,
        width="100%",
        modal=True
    )
    if noModal == False:
        imageModal = imageModal + modal

    if sherlockClassification:
        littleTitle = cu.little_label(
            text="contextual classification:"
        )

        sherlockClassification = khufu.coloredText(
            text=sherlockClassification,
            color="red",
            size=4,  # 1-10
        )

        sherlockClassification = khufu.grid_row(
            responsive=True,
            columns="%(littleTitle)s %(sherlockClassification)s %(sherlockAnnotation)s" % locals(
            ),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
    else:
        sherlockClassification = ""

    return "%(title)s %(imageModal)s %(sdssLinkRow)s %(sherlockClassification)s" % locals()
