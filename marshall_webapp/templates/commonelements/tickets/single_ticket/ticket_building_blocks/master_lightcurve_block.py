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

    **Return:**
        - ``master_lightcurve_block`` -- the ticket identity block for the pesssto object

    **Todo**
    # @review: when complete, clean master_lightcurve_block function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu
    import dryxPython.mysql as dms

    log.info('starting the ``master_lightcurve_block`` function')
    ## VARIABLES ##

    if displayTitle:
        title = cu.block_title(
            log,
            title="master lightcurve"
        )
    else:
        title = ""

    name = discoveryDataDictionary["masterName"]

    if discoveryDataDictionary["master_pessto_lightcurve"]:
        lightCurveImage = '/static/caches/transients/%s/master_lightcurve.png' % (
            discoveryDataDictionary["transientBucketId"],)
    else:
        lightCurveImage = ''

    # Override for LSQ lightcurves
    lsqname = False
    lightcurveSwitchAttempt = True
    for row in lightcurveData:
        if row["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and "lsq-disc" in row["survey"].lower():
            lightcurveSwitchAttempt = False

    if lightcurveSwitchAttempt == True:
        if "lsq" in name:
            lsqname = name
        else:
            for aka in objectAkas:
                if aka["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and "lsq" in aka["name"].lower():
                    lsqname = aka["name"]
                    break

    if lsqname:
        transientBucketId = discoveryDataDictionary["transientBucketId"]
        lightCurveImage = '/static/caches/transients/%(transientBucketId)s/lsq_lightcurve.gif' % locals(
        )

    if len(lightCurveImage):
        lightCurveImage = khufu.imagingModal(
            log=log,
            imagePath=lightCurveImage,
            display="polaroid",  # [ rounded | circle | polaroid | False ]
            modalHeaderContent="Lightcurve for %(name)s" % locals(),
            modalFooterContent="",
            stampWidth=False,
            modalImageWidth=False,
            downloadFilename="%(name)s_master_lightcurve.png" % locals())
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
############################################
# CODE TO BE DEPECIATED                    #
############################################
if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
