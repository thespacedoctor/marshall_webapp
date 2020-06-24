#!/usr/local/bin/python
# encoding: utf-8
"""
*The classification block for the object ticket*

:Author:
    David Young
"""
import sys
import os
import re
import datetime
from fundamentals import times
import khufu
from marshall_webapp.templates.commonelements import commonutils as cu

def classification_block(
        log,
        request,
        discoveryDataDictionary):
    """get ticket classification block

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
    

    **Return**

    - ``classification_block`` -- the ticket identity block for the pesssto object
    
    """
    log.debug('starting the ``classification_block`` function')

    if not discoveryDataDictionary["recentClassification"]:
        return None

    title = cu.block_title(
        log,
        title="spectral classification"
    )

    # classification
    label = cu.little_label(
        text="classification:",
    )

    if len(discoveryDataDictionary["recentClassification"]) and discoveryDataDictionary["recentClassification"][0] == "I":
        discoveryDataDictionary["recentClassification"] = "SN " + \
            discoveryDataDictionary["recentClassification"]
    text = khufu.coloredText(
        text=discoveryDataDictionary["recentClassification"],
        color="magenta",
        size=6
    )
    spectralType = khufu.grid_row(
        responsive=True,
        columns="""%s   %s""" % (label, text,),
    )

    # classifcation survey
    label = cu.little_label(
        text="classifcation survey:",
    )
    text = khufu.coloredText(
        text=discoveryDataDictionary["classificationSurvey"],
        color="green",
        size=5
    )
    classificationSurvey = khufu.grid_row(
        responsive=True,
        columns="""%s   %s""" % (label, text,),
    )

    # classification date
    label = cu.little_label(
        text="classification date:",
    )
    text = khufu.coloredText(
        text=str(discoveryDataDictionary["classificationDate"])[0:10],
        color="orange",
        size=4
    )

    daysPast = discoveryDataDictionary["classificationDate"]
    if daysPast:

        daysPast = times.datetime_relative_to_now(daysPast)[1:]
        if "just" not in daysPast:
            daysPast = daysPast[1:]
        if daysPast[-1] == "d":
            daysPast = "(%s days ago)" % (daysPast[0:-1],)
        elif "just" not in daysPast:
            daysPast = "(+%s)" % (daysPast,)
        else:
            daysPast = "(%s)" % (daysPast,)
        daysPast = khufu.coloredText(
            text="<br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp%(daysPast)s" % locals(
            ),
            color="violet"
        )
    else:
        daysPast = ""
    classificationDate = khufu.grid_row(
        responsive=True,
        columns="""%s   %s %s""" % (label, text, daysPast),
    )

    # classifcation survey
    label = cu.little_label(
        text="classification phase:",
    )
    classificationWRTMax = discoveryDataDictionary["classificationWRTMax"]
    classificationPhase = discoveryDataDictionary["classificationPhase"]

    if classificationWRTMax is None:
        classificationWRTMax = "not set"

    if classificationPhase:
        if classificationWRTMax == "pre-max":
            classificationWRTMax = "-%(classificationPhase)sd" % locals()
        elif classificationWRTMax == "post-max":
            classificationWRTMax = "+%(classificationPhase)sd" % locals()
    classificationWRTMax = "&nbsp&nbsp%(classificationWRTMax)s" % locals()

    if "unknown" in classificationWRTMax:
        size = 4
    else:
        size = 5
    text = khufu.coloredText(
        text="""%(classificationWRTMax)s""" % locals(),
        color="blue",
        size=size
    )
    classificationPhase = khufu.grid_row(
        responsive=True,
        columns="""%s %s""" % (label, text,),
    )

    # redshift
    label = cu.little_label(
        text="redshift:",
    )

    redshift = ""
    if discoveryDataDictionary["best_redshift"]:
        text = khufu.coloredText(
            text="%6.4f" % (discoveryDataDictionary["best_redshift"]),
            color="yellow",
            size=6
        )
    else:
        text = khufu.coloredText(
            text="unknown",
            color="yellow",
            size=4
        )
    redshift = khufu.grid_row(
        responsive=True,
        columns="""%s   %s""" % (label, text,),
    )

    # distance
    label = cu.little_label(
        text="distance:",
    )

    distanceMpc = ""
    if discoveryDataDictionary["distanceMpc"]:
        text = khufu.coloredText(
            text="%10.2f Mpc" % (discoveryDataDictionary["distanceMpc"]),
            color="blue",
            size=6
        )
        distanceMpc = khufu.grid_row(
            responsive=True,
            columns="""%s   %s""" % (label, text,),
        )

    return "%(title)s %(spectralType)s %(classificationSurvey)s %(classificationDate)s %(classificationPhase)s %(redshift)s %(distanceMpc)s" % locals()
