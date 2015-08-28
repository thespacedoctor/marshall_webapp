#!/usr/local/bin/python
# encoding: utf-8
"""
master_lightcurve_block.py
===========================
:Summary:
    The master lightcurve block for the object ticket

:Author:
    David Young

:Date Created:
    March 26, 2014 

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
import khufu
from dryxPython import commonutils as dcu
from .....commonelements import commonutils as cu
import dryxPython.mysql as dms

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : March 26, 2014
# CREATED : March 26, 2014
# AUTHOR : DRYX


def master_lightcurve_block(
        log,
        request,
        discoveryDataDictionary,
        lightcurveData,
        objectAkas,
        displayTitle=True):
    """get ticket lightcurve block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``objectAkas`` -- the transient object akas
        - ``displayTitle`` -- display the title for this block?

    **Return:**
        - ``master_lightcurve_block`` -- the ticket identity block for the pesssto object

    **Tasks:**
    """
    log.info('starting the ``master_lightcurve_block`` function')

    lsqExists = False
    if displayTitle:
        title = cu.block_title(
            log,
            title="master lightcurve"
        )
    else:
        title = ""

    name = discoveryDataDictionary["masterName"]

    if discoveryDataDictionary["master_pessto_lightcurve"]:
        lightCurveImage = request.static_path(
            'marshall_webapp:static/caches/transients/%s/master_lightcurve.png' % (
                discoveryDataDictionary["transientBucketId"],))
        dlightCurveImage = 'static/caches/transients/%s/master_lightcurve.png' % (
            discoveryDataDictionary["transientBucketId"],)
    else:
        lightCurveImage = ''
        dlightCurveImage = ''

    # Override for LSQ lightcurves
    lightcurveSwitchAttempt = True
    transientBucketId = discoveryDataDictionary["transientBucketId"]
    for row in lightcurveData:
        if row["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and "lsq-disc" in row["survey"].lower():
            lightcurveSwitchAttempt = False

    if lightcurveSwitchAttempt == True:
        filePath = request.registry.settings["downloads"][
            "transient cache directory"] + "/%(transientBucketId)s/lsq_lightcurve.gif" % locals()
        lsqExists = os.path.exists(filePath)

    if lsqExists:
        transientBucketId = discoveryDataDictionary["transientBucketId"]
        lightCurveImage = request.static_path(
            'marshall_webapp:static/caches/transients/%(transientBucketId)s/lsq_lightcurve.gif' % locals(
            ))
        dlightCurveImage = request.static_path('marshall_webapp:static/caches/transients/%(transientBucketId)s/lsq_lightcurve.gif' % locals(
        ))

    if len(lightCurveImage):
        href = request.route_path(
            'download', _query={'url': dlightCurveImage, "webapp": "marshall_webapp", "filename": "%(name)s_master_lightcurve" % locals()})
        lightCurveImage = khufu.imagingModal(
            log=log,
            imagePath=lightCurveImage,
            display="polaroid",  # [ rounded | circle | polaroid | False ]
            modalHeaderContent="Lightcurve for %(name)s" % locals(),
            modalFooterContent="",
            stampWidth=False,
            modalImageWidth=False,
            downloadLink=href)
        lightCurveImage = lightCurveImage.get()
    else:
        lightCurveImage = khufu.image(
            # [ industrial | gray | social ]
            src="""holder.js/190x190/auto/industrial/text:master lightcurve not ready""",
            display="polaroid",  # [ rounded | circle | polaroid | False ]
        )

    return "%(title)s %(lightCurveImage)s" % locals()


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
