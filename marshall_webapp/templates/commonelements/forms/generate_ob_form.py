#!/usr/local/bin/python
# encoding: utf-8
"""
generate_ob_form.py
=========================
:Summary:
    The generate object form for the PESSTO Marshall

:Author:
    David Young

:Date Created:
    March 7, 2014

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
from ..tickets.single_ticket.ticket_building_blocks.lightcurve_block import lightcurve_block as lcb

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : March 7, 2014
# CREATED : March 7, 2014
# AUTHOR : DRYX


def generate_ob_form(
    log,
    request,
    discoveryDataDictionary,
    lightcurveData,
    objectAkas
):
    """generate object form

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data
        - ``lightcurveData`` -- lightcurve data

    **Return:**
        - ``generateOBForm``

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu
    import dryxPython.astrotools as dat

    from datetime import datetime, date, time
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    # Header Text
    if discoveryDataDictionary["classifiedFlag"] == 0:
        headerText = "Generate Classification OB for %(masterName)s" % discoveryDataDictionary

    # generate lightcurve info
    lightcurve_block = lcb(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        lightcurveData=lightcurveData,
        objectAkas=objectAkas,
        displayTitle=False,
        offset=0
    )

    if "/static/caches/transients" not in lightcurve_block:
        formSpan = 6
        lcSpan = 6
    else:
        formSpan = 5
        lcSpan = 7
    lightcurve_block = khufu.grid_column(
        span=lcSpan,  # 1-12
        offset=0,  # 1-12
        content=lightcurve_block,
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    seeingCG = khufu.checkbox(
        optionText='seeing > 1.5 arcsec',
        inline=True,
        htmlId="badSeeing",
        optionNumber=1,
        inlineHelpText=False,
        blockHelpText=False,
        disabled=False
    )
    # seeingCG = khufu.controlRow(
    #     inputList=[seeingInput, ]
    # )
    # seeingLabel = khufu.horizontalFormControlLabel(
    #     labelText='seeing > 1.5 arcsec',
    #     forId="badSeeing"
    # )
    # seeingCG = khufu.horizontalFormControlGroup(
    #     content="%(seeingInput)s" % locals(),
    #     validationLevel=False
    # )

    defaultValue = discoveryDataDictionary["currentMagnitude"]
    if defaultValue:
        defaultValue = """%(defaultValue)5.2f""" % locals()
    else:
        defaultValue = "?"

    magnitudeInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='text',
        placeholder='',
        span=3,
        htmlId="currentMag",
        pull=False,
        prepend=False,
        append=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        rightText="current mag estimate",
        required=False,
        disabled=False,
        defaultValue=defaultValue
    )
    magnitudeInput = """%(magnitudeInput)s""" % locals()
    magnitudeInput = khufu.controlRow(
        inputList=[magnitudeInput, ]
    )

    magnitudeCG = khufu.horizontalFormControlGroup(
        content="%(magnitudeInput)s" % locals(),
        validationLevel=False
    )

    magnitudeCG = "%(magnitudeCG)s magnitude" % locals()

    # x-tmpx-form-control-group
    downloadButton = khufu.button(
        buttonText="""<i class="icon-download-alt"></i>""",
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='info',
        buttonSize='default',  # [ large | default | small | mini ]
        htmlId="generateOBForm%(transientBucketId)s" % discoveryDataDictionary,
        htmlClass="generateOBSubmitButton",
        href=False,
        pull=False,  # right, left, center
        submit=True,
        block=False,
        disable=False,
        dataToggle=False,
        close=False
    )
    cancelbutton = khufu.button(
        buttonText='cancel',
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='danger',
        buttonSize='default',  # [ large | default | small | mini ]
        htmlId=False,
        href=False,
        pull=False,  # right, left, center
        submit=False,
        block=False,
        disable=False,
        dataToggle=False,
        close=True
    )
    buttonGroup = khufu.buttonGroup(
        buttonList=[cancelbutton, downloadButton],
        format='default',  # [ default | toolbar | vertical ]
        pull="left"
    )

    prefix = request.registry.settings["apache prefix"]
    ra = dat.ra_to_sex(
        ra=discoveryDataDictionary["raDeg"],
        delimiter=':'
    )
    ra = khufu.formInput(
        ttype='text',
        htmlId="ra",
        hidden=True,
        defaultValue=ra
    )

    dec = dat.dec_to_sex(
        dec=discoveryDataDictionary["decDeg"],
        delimiter=':'
    )
    dec = khufu.formInput(
        ttype='text',
        htmlId="dec",
        hidden=True,
        defaultValue=dec
    )
    objectName = khufu.formInput(
        ttype='text',
        htmlId="objectName",
        hidden=True,
        defaultValue=discoveryDataDictionary["masterName"]
    )
    objectClass = khufu.formInput(
        ttype='text',
        htmlId="objectClass",
        hidden=True,
        defaultValue="SN"
    )
    grism = khufu.formInput(
        ttype='text',
        htmlId="grism",
        hidden=True,
        defaultValue=13
    )
    instrument = khufu.formInput(
        ttype='text',
        htmlId="instrument",
        hidden=True,
        defaultValue="efosc"
    )
    spectrumOrImage = khufu.formInput(
        ttype='text',
        htmlId="spectrumOrImage",
        hidden=True,
        defaultValue="spectrum"
    )

    # currentMag = 15.2 & ra = 12:
    #     34:
    #         54.3 & dec = -32:
    #             23:
    # 12.23 & objectName = ps1 - ghf & seeing = 1.5 & objectClass = SN & grism
    # = 13 & instrument = efosc & spectrumOrImage = spectrum

    generateOBForm = khufu.form(
        content="%(seeingCG)s %(magnitudeCG)s %(ra)s  %(dec)s  %(objectName)s  %(objectClass)s  %(grism)s  %(instrument)s  %(spectrumOrImage)s %(buttonGroup)s" % locals(
        ),
        # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
        formType='inline',
        navBarPull=False,  # [ false | right | left ]
        postToScript="%(prefix)s/marshall/ob_generator.py" % locals(),
        span=11,
        offset=1,
    )

    generateOBForm = khufu.grid_column(
        span=formSpan,  # 1-12
        offset=0,  # 1-12
        content=generateOBForm,
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    generateOBForm = khufu.modals.modal(
        modalHeaderContent="%(headerText)s" % locals(),
        modalBodyContent=lightcurve_block + generateOBForm,
        modalFooterContent="",
        htmlId="generateOBForm%(transientBucketId)s" % discoveryDataDictionary,
        htmlClass="generateOBForm"
    )

    return generateOBForm

# use the tab-trigger below for new function
# x-def-with-logger

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
