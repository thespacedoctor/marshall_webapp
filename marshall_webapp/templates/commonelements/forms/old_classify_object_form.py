#!/usr/local/bin/python
# encoding: utf-8
"""
classify_object_form.py
=========================
:Summary:
    The classify object form for the PESSTO Marshall

:Author:
    David Young

:Date Created:
    December 11, 2013

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

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : December 11, 2013
# CREATED : December 11, 2013
# AUTHOR : DRYX


def classify_object_form(
    log,
    request,
    discoveryDataDictionary
):
    """classify object form

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    **Return:**
        - ``classifyObjectForm``

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    from datetime import datetime, date, time
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    sourceInput = khufu.select(
        optionList=["pessto", "atel", "cbat", "private comm."],
        multiple=False,
        span=4,
        htmlId="clsSource",
        inlineHelpText=False,
        blockHelpText=False,
        required=True,
        disabled=False
    )
    sourceInput = khufu.controlRow(
        inputList=[sourceInput, ]
    )
    sourceLabel = khufu.horizontalFormControlLabel(
        labelText='source',
        forId="clsSource"
    )
    sourceCG = khufu.horizontalFormControlGroup(
        content="""%(sourceLabel)s %(sourceInput)s""" % locals(),
        validationLevel=False
    )
    obsDateInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='text',
        placeholder='YYYY-MM-DD or mjd',
        span=4,
        htmlId="clsObsdate",
        pull=False,
        prepend=False,
        append=False,
        inlineHelpText="YYYY-MM-DD or mjd",
        blockHelpText=False,
        focusedInputText=now,
        required=True,
        disabled=False
    )
    obsDateInput = khufu.controlRow(
        inputList=[obsDateInput, ]
    )
    obsDateLabel = khufu.horizontalFormControlLabel(
        labelText='classification date',
        forId="clsObsdate"
    )
    obsDateCG = khufu.horizontalFormControlGroup(
        content="%(obsDateLabel)s %(obsDateInput)s" % locals(),
        validationLevel=False
    )
    typeInput = khufu.select(
        optionList=["supernova", "agn", "variable star",
                    "galaxy", "cv", "LBV", "imposter", "unknown"],
        multiple=False,
        span=4,
        htmlId="clsType",
        inlineHelpText=False,
        blockHelpText=False,
        required=True,
        disabled=False
    )
    typeInput = khufu.controlRow(
        inputList=[typeInput, ]
    )
    typeLabel = khufu.horizontalFormControlLabel(
        labelText='object type',
        forId="clsType"
    )
    typeCG = khufu.horizontalFormControlGroup(
        content="%(typeLabel)s %(typeInput)s" % locals(),
        validationLevel=False
    )
    snClassificationInput = khufu.select(
        optionList=["Ia", "Ib", "Ic", "Ibc", "Ibn", "I-CSM", "I",
                    "IIb", "IIL", "IIP", "IIn", "II"],
        multiple=False,
        span=4,
        htmlId="clsSnClassification",
        inlineHelpText=False,
        blockHelpText=False,
        required=False,
        disabled=False
    )
    peculiarInput = khufu.checkbox(
        optionText='peculiar',
        inline=True,
        htmlId="clsPeculiar",
        optionNumber=1,
        inlineHelpText=False,
        blockHelpText=False,
        disabled=False
    )

    snClassificationInput = khufu.controlRow(
        inputList=[
            """%(snClassificationInput)s  &nbsp %(peculiarInput)s""" %
            locals()]
    )
    snClassificationLabel = khufu.horizontalFormControlLabel(
        labelText='sn classification',
        forId="clsSnClassification"
    )

    snClassificationCG = khufu.horizontalFormControlGroup(
        content="""%(snClassificationLabel)s %(snClassificationInput)s""" % locals(
        ),
        validationLevel=False
    )
    redshiftInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='float',
        placeholder='',
        span=4,
        htmlId="clsRedshift",
        pull=False,
        prepend=False,
        append=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=False,
        disabled=False
    )
    redshiftInput = khufu.controlRow(
        inputList=[redshiftInput, ]
    )
    redshiftLabel = khufu.horizontalFormControlLabel(
        labelText='redshift',
        forId="clsRedshift"
    )
    redshiftCG = khufu.horizontalFormControlGroup(
        content="%(redshiftLabel)s %(redshiftInput)s" % locals(),
        validationLevel=False
    )
    sendToInput1 = khufu.radio(
        optionText='yes',
        optionNumber=1,
        htmlId="clsSendTo",
        inlineHelpText=False,
        blockHelpText=False,
        disabled=False,
        checked=True
    )
    sendToInput2 = khufu.radio(
        optionText='no',
        optionNumber=2,
        htmlId="clsSendTo",
        inlineHelpText=False,
        blockHelpText=False,
        disabled=False
    )
    sendToInput = khufu.controlRow(
        inputList=[sendToInput1, sendToInput2]
    )
    sendToLabel = khufu.horizontalFormControlLabel(
        labelText='send to atel queue',
        forId="clsSendTo"
    )
    sendToCG = khufu.horizontalFormControlGroup(
        content="%(sendToLabel)s %(sendToInput)s" % locals(),
        validationLevel=False
    )
    transientBucketIdInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='number',
        placeholder='',
        span=4,
        htmlId="clsTransientBucketId",
        pull=False,
        prepend=False,
        append=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=False,
        disabled=False,
        defaultValue=discoveryDataDictionary["transientBucketId"]
    )
    transientBucketIdInput = khufu.controlRow(
        inputList=[transientBucketIdInput, ]
    )
    transientBucketIdLabel = khufu.horizontalFormControlLabel(
        labelText='transientBucketId',
        forId="clsTransientBucketId"
    )
    transientBucketIdCG = khufu.horizontalFormControlGroup(
        content="%(transientBucketIdLabel)s %(transientBucketIdInput)s" % locals(
        ),
        validationLevel=False,
        hidden=True
    )

    classificationPhaseInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='number',
        span=7,
        htmlId="clsClassificationPhase",
        pull=False,
        required=False,
        disabled=True,
        placeholder='unknown',
        prepend="?"
    )

    classificationPhaseInput = khufu.controlRow(
        inputList=[classificationPhaseInput]
    )
    classificationPhaseLabel = khufu.horizontalFormControlLabel(
        labelText='days from max',
        forId="clsClassificationPhase"
    )
    classificationPhaseCG = khufu.horizontalFormControlGroup(
        content=classificationPhaseLabel + classificationPhaseInput,
        validationLevel=False
    )
    classificationWRTMaxInput = khufu.select(
        optionList=["unknown", "pre-max", "at max", "post-max"],
        multiple=False,
        span=4,
        htmlId="clsClassificationWRTMax",
        inlineHelpText=False,
        blockHelpText=False,
        required=True,
        disabled=False
    )
    classificationWRTMaxInput = khufu.controlRow(
        inputList=[classificationWRTMaxInput, ]
    )
    classificationWRTMaxLabel = khufu.horizontalFormControlLabel(
        labelText='classifcation phase',
        forId="clsClassificationWRTMax"
    )
    classificationWRTMaxCG = khufu.horizontalFormControlGroup(
        content=classificationWRTMaxLabel + classificationWRTMaxInput,
        validationLevel=False
    )

    # x-tmpx-form-control-group
    classifyButton = khufu.button(
        buttonText='classify',
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='info',
        buttonSize='default',  # [ large | default | small | mini ]
        htmlId="classifyFormSubmitButton",
        href=False,
        pull=False,  # right, left, center
        submit=True,
        block=False,
        disable=False,
        dataToggle=False
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
        buttonList=[cancelbutton, classifyButton],
        format='default'  # [ default | toolbar | vertical ]
    )

    prefix = request.registry.settings["apache prefix"]

    href = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"], _query={'method': 'post'})
    classificationForm = khufu.form(
        content="%(sourceCG)s %(obsDateCG)s %(typeCG)s %(snClassificationCG)s %(redshiftCG)s %(classificationWRTMaxCG)s %(classificationPhaseCG)s %(sendToCG)s %(transientBucketIdCG)s %(buttonGroup)s" % locals(
        ),
        # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
        formType='horizontal',
        navBarPull=False,  # [ false | right | left ]
        postToScript=href,
        span=10,
        offset=2,
        htmlClass="classificationForm"
    )

    classifyObjectForm = khufu.modals.modal(
        modalHeaderContent="Add a classification for %(masterName)s" % discoveryDataDictionary,
        modalBodyContent=classificationForm,
        modalFooterContent="",
        htmlId="classifyForm%(transientBucketId)s" % discoveryDataDictionary
    )

    return classifyObjectForm

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
