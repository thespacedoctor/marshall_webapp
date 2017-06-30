#!/usr/local/bin/python
# encoding: utf-8
"""
object_info_block.py
=================
:Summary:
    The Object Info block for the object ticket

:Author:
    David Young

:Date Created:
    November 20, 2013

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
from dryxPython import commonutils as dcu
from .....commonelements import commonutils as cu
import khufu
import dryxPython.astrotools as dat

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : November 20, 2013
# CREATED : November 20, 2013
# AUTHOR : DRYX


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
    log.info('starting the ``object_info_block`` function')

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

    raSex = khufu.coloredText(
        text=discoveryDataDictionary["raSex"],
        color="violet",
        size=3,

    )

    decSex = khufu.coloredText(
        text=discoveryDataDictionary["decSex"],
        color="cyan",
        size=3
    )

    raDecSex = khufu.grid_row(
        responsive=True,
        columns="""%(raDecLabel)s %(raSex)s %(decSex)s<br>&nbsp&nbsp&nbsp&nbsp&nbsp%(ra)s %(dec)s""" % locals(
        ),
    )
    raDec = raDecSex

    # peak magnitude
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

    # pre-discovery non-detection
    label = cu.little_label(
        text="pre-disc non-detection:",
        pull=False
    )
    lastNonDetectionDate = discoveryDataDictionary["lastNonDetectionDate"]
    if not lastNonDetectionDate:
        lastNonDetectionDate = "unknown"
        daysPast = "unknown"
    else:
        daysPast = dcu.pretty_date(lastNonDetectionDate)[2:]
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
    daysPast = dcu.pretty_date(dateAdded)[2:]
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
    daysPast = dcu.pretty_date(discoveryDate)[2:]
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

    return "%(title)s %(raDec)s %(absMag)s %(nonDect)s %(discoveryDate)s %(dateAdded)s" % locals()


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
