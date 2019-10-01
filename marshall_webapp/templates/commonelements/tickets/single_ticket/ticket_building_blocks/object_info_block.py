#!/usr/local/bin/python
# encoding: utf-8
"""
*The Object Info block for the object ticket*

:Author:
    David Young

:Date Created:
    November 20, 2013
"""
import sys
import os
import re
import datetime
from marshall_webapp.templates.commonelements import commonutils as cu
import khufu
from fundamentals import times


def object_info_block(
        log,
        request,
        discoveryDataDictionary):
    """get ticket object info block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.

    **Return:**
        - ``object_info_block`` -- the ticket identity block for the pesssto object
    """
    log.debug('starting the ``object_info_block`` function')

    title = cu.block_title(
        log,
        title="object info"
    )

    raDecLabel = cu.little_label(
        text="ra & dec:"
    )

    ra = ""
    dec = ""
    if discoveryDataDictionary["raDeg"]:
        ra = khufu.coloredText(
            text="[ %8.5f" % (discoveryDataDictionary["raDeg"],),
            color="violet",
            size=3,
        )
        dec = khufu.coloredText(
            text="%8.5f ]" % (discoveryDataDictionary["decDeg"],),
            color="cyan",
            size=3
        )

    glat = ""
    glon = ""
    if discoveryDataDictionary["gLat"]:
        glat = khufu.coloredText(
            text="%8.5f" % (discoveryDataDictionary["gLat"],),
            color="blue",
            size=3,
        )
        glon = khufu.coloredText(
            text="%8.5f" % (discoveryDataDictionary["gLon"],),
            color="blue",
            size=3
        )

    raSex = khufu.coloredText(
        text=discoveryDataDictionary["raSex"][0:12],
        color="violet",
        size=3,

    )

    decSex = khufu.coloredText(
        text=discoveryDataDictionary["decSex"][0:12],
        color="cyan",
        size=3
    )

    raDecSex = khufu.grid_row(
        responsive=True,
        columns="""%(raDecLabel)s %(raSex)s %(decSex)s<br>&nbsp&nbsp&nbsp&nbsp&nbsp%(ra)s %(dec)s""" % locals(
        ),
    )
    raDec = raDecSex

    galCoordLabel = cu.little_label(
        text="galactic coords:"
    )
    galCoord = khufu.grid_row(
        responsive=True,
        columns="""%(galCoordLabel)s %(glon)s %(glat)s""" % locals(
        ),
    )

    # PEAK MAGNITUDE
    label = cu.little_label(
        text="abs peak mag:",
        lineBreak=True
    )
    absMag = ""
    if discoveryDataDictionary["absolutePeakMagnitude"]:
        text = khufu.coloredText(
            text="%4.2f" % (discoveryDataDictionary["absolutePeakMagnitude"],),
            color="yellow",
            size=6,
        )
        absMag = khufu.grid_row(
            responsive=True,
            columns="""%s   %s""" % (label, text,),
        )

    # PRE-DISCOVERY NON-DETECTION
    label = cu.little_label(
        text="pre-disc non-detection:",
        pull=False
    )
    lastNonDetectionDate = discoveryDataDictionary["lastNonDetectionDate"]
    if not lastNonDetectionDate:
        lastNonDetectionDate = "unknown"
        daysPast = "unknown"
    else:

        daysPast = times.datetime_relative_to_now(lastNonDetectionDate)[2:]

        if daysPast[-1] == "d":
            daysPast = "%s days ago" % (daysPast[0:-1],)
        else:
            daysPast = "(+%s)" % (daysPast,)
        lastNonDetectionDate = datetime.date.isoformat(lastNonDetectionDate)

    daysPast = khufu.coloredText(
        text=daysPast,
        color="green",
        size=5
    )
    if "unknown" not in lastNonDetectionDate:
        text = khufu.coloredText(
            text="""(%(lastNonDetectionDate)s)""" % locals(),
            color="red",
            size=3,
        )
        nonDect = khufu.grid_row(
            responsive=True,
            columns="""%s   %s<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp%s""" % (
                label, daysPast, text),
        )
    else:
        nonDect = khufu.grid_row(
            responsive=True,
            columns="""%s   %s""" % (
                label, daysPast),
        )

    label = cu.little_label(
        text="date added to marshall:"
    )
    dateAdded = discoveryDataDictionary["dateAdded"]
    daysPast = times.datetime_relative_to_now(dateAdded)[2:]
    if daysPast[-1] == "d":
        daysPast = "%s days ago" % (daysPast[0:-1],)
    else:
        daysPast = "(+%s)" % (daysPast,)
    dateAdded = datetime.date.isoformat(dateAdded)
    dateAdded = khufu.coloredText(
        text="""(%(dateAdded)s)""" % locals(),
        color="magenta",
        size=3,
    )
    daysPast = khufu.coloredText(
        text=daysPast,
        color="orange",
        size=4
    )

    dateAdded = khufu.grid_row(
        responsive=True,
        columns="""%s   %s<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp%s""" % (
            label, daysPast, dateAdded),
    )

    label = cu.little_label(
        text="discovery date:"
    )
    discoveryDate = discoveryDataDictionary["earliestDetection"]
    daysPast = times.datetime_relative_to_now(discoveryDate)[2:]
    if daysPast[-1] == "d":
        daysPast = "%s days ago" % (daysPast[0:-1],)
    else:
        daysPast = "(+%s)" % (daysPast,)
    discoveryDate = datetime.date.isoformat(discoveryDate)
    discoveryDate = khufu.coloredText(
        text="""(%(discoveryDate)s)""" % locals(),
        color="blue",
        size=3,
    )
    daysPast = khufu.coloredText(
        text=daysPast,
        color="yellow",
        size=4
    )

    discoveryDate = khufu.grid_row(
        responsive=True,
        columns="""%s   %s<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp%s""" % (
            label, daysPast, discoveryDate),
    )

    return "%(title)s %(raDec)s %(galCoord)s %(absMag)s %(nonDect)s %(discoveryDate)s %(dateAdded)s" % locals()
