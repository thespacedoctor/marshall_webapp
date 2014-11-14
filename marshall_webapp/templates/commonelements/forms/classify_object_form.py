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

    postToScript = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"], _query={'method': 'post'})

    href = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"])
    thisModal = khufu.modals.modalForm(
        log=log,
        title="Please add Classification Details for %(masterName)s" % discoveryDataDictionary,
        postToScriptUrl=postToScript,
        reloadToUrl=href,
        formClassName="classificationForm"
    )
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
    thisModal.add_form_object(
        formObject=sourceInput,
        label="source"
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
    thisModal.add_form_object(
        formObject=obsDateInput,
        label="classification date"
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
    thisModal.add_form_object(
        formObject=typeInput,
        label="object type"
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
    thisModal.add_form_object(
        formObject="""%(snClassificationInput)s  &nbsp %(peculiarInput)s""" %
        locals(),
        label="sn classification"
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
    thisModal.add_form_object(
        formObject=redshiftInput,
        label="redshift"
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
    thisModal.add_form_object(
        formObject="%(sendToInput1)s %(sendToInput2)s" % locals(),
        label="send to atel queue"
    )

    classificationWRTMaxInput = khufu.select(
        optionList=["unknown", "pre-max", "at max", "post-max"],
        multiple=False,
        span=4,
        htmlId="clsClassificationWRTMax",
        inlineHelpText=False,
        blockHelpText=False,
        required=False,
        disabled=False
    )

    thisModal.add_form_object(
        formObject=classificationWRTMaxInput,
        label="classifcation phase"
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
    thisModal.add_form_object(
        formObject=classificationPhaseInput,
        label="days from max"
    )

    # xdhf-add-form-object-to-modalForm
    # xdhf-add-hidden-parameter-to-modalForm

    modalForm, modalTrigger = thisModal.get()

    popover = khufu.popover(
        tooltip=True,
        placement="right",
        trigger="hover",
        title="add a spectral classification for this object",
        content=False,
    )

    icon = """<i class="icon-target2"></i>&nbsp"""
    thisButton = khufu.button(
        buttonText=icon,
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='success',
        buttonSize='small',  # [ large | default | small | mini ]
        href=modalTrigger,
        pull="right",  # right, left, center
        submit=False,
        block=False,
        disable=False,
        dataToggle="modal",  # [ modal ]
        popover=popover
    )

    return thisButton, modalForm

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
