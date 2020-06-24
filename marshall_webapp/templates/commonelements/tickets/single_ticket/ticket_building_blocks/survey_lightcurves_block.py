#!/usr/local/bin/python
# encoding: utf-8
"""
*The master lightcurve block for the object ticket*

:Author:
    David Young
"""
import sys
import os
import re
import datetime as datetime
from marshall_webapp.templates.commonelements import commonutils as cu
import khufu

def survey_lightcurves_block(
        log,
        request,
        discoveryDataDictionary,
        lightcurveData,
        displayTitle=True):
    """get ticket lightcurve block

    **Key Arguments**

    - ``log`` -- logger
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
    - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
    - ``displayTitle`` -- display the title for this block?
    

    **Return**

    - ``survey_lightcurves_block`` -- the ticket identity block for the pesssto object
    
    """
    log.debug('starting the ``survey_lightcurves_block`` function')

    ## VARIABLES ##
    lightCurveImages = []
    tinyDict = {}
    transientBucketId = discoveryDataDictionary["transientBucketId"]

    # TURNING THE TITLE FOR THE BLOCK ON OR OFF
    if displayTitle:
        title = cu.block_title(
            log,
            title="survey lightcurves"
        )
    else:
        title = ""

    # THE SURVEYS AND LIGHTCURVE EXTENSIONS USED
    surveyList = [{"lsq": "gif"}, {"ogle": "png"},
                  {"css": "png"}, {"mls": "png"}, {"sss": "png"}]

    # FOR EACH POSSIBLE SURVEY WITH LIGHTCURVE INFO ...
    for survey in surveyList:
        thisSurvey = list(survey.keys())[0]
        thisExt = list(survey.values())[0]
        lightCurveFlag = "%(thisSurvey)s_lightcurve" % locals()

        # IF THE SURVEY LIGHTCURVE EXISTS
        if discoveryDataDictionary[lightCurveFlag]:
            tinyDict = {}
            tinyDict["url"] = ""
            tinyDict["survey"] = thisSurvey
            tinyDict[
                "lc"] = '/marshall/static/caches/transients/%(transientBucketId)s/%(thisSurvey)s_lightcurve.%(thisExt)s' % locals()
            tinyDict[
                "filename"] = "%(thisSurvey)s_lightcurve.%(thisExt)s" % locals()

            for row in lightcurveData:
                if row["survey"] and thisSurvey.lower() in row["survey"].lower() and row["surveyObjectUrl"] and transientBucketId == row["transientBucketId"]:
                    tinyDict["url"] = row["surveyObjectUrl"]
                    if thisSurvey.lower() == "lsq":
                        user = request.registry.settings[
                            "credentials"]["lsq"]["username"]
                        pwd = request.registry.settings[
                            "credentials"]["lsq"]["password"]
                        tinyDict["url"] = tinyDict["url"].replace(
                            "portal.", "%(user)s:%(pwd)s@portal." % locals())
            lightCurveImages.append(tinyDict)

    surveyLightcurves = ""
    colors = ["blue", "green", "orange", "magenta", "cyan", "red"]
    for i, tinyDict in enumerate(lightCurveImages):
        count = i
        while count > len(colors):
            count = count - len(colors)
        # add text color
        link = khufu.a(
            content=tinyDict["survey"].upper(),
            href=tinyDict["url"]
        )
        link = khufu.coloredText(
            text=link,
            color=colors[i],
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        survey = tinyDict["survey"].upper()
        masterName = discoveryDataDictionary["masterName"]
        filename = tinyDict["filename"]
        filename = """%(masterName)s_%(survey)s_lightcurve""" % locals()

        imageSource = khufu.a(
            content='lightcurve source',
            href=tinyDict["url"],
        )

        href = request.route_path(
            'download', _query={'url': tinyDict["lc"], "webapp": "marshall_webapp", "filename": filename})

        log.debug("""image download link: `%(href)s`""" % locals())

        imageModal = khufu.imagingModal(
            log=log,
            imagePath=tinyDict["lc"],
            display="polaroid",  # [ rounded | circle | polaroid | False ]
            modalHeaderContent="%(survey)s lightcurve for %(masterName)s" % locals(
            ),
            modalFooterContent=imageSource,
            stampWidth="100%",
            modalImageWidth=400,
            downloadLink=href)
        imageModal = imageModal.get()

        surveyLightcurves = "%(surveyLightcurves)s%(link)s%(imageModal)s" % locals(
        )

    return "%(title)s %(surveyLightcurves)s" % locals()
