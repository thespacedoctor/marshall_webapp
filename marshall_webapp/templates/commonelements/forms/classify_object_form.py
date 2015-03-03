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
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from datetime import datetime, date, time
from docopt import docopt
import khufu
from dryxPython import commonutils as dcu


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
        - ``classifyObjectForm`` -- the modal form used to classify transients

    **Todo**
    """
    # get the datetime for now
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
        required=True
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
        inlineHelpText="YYYY-MM-DD or mjd",
        focusedInputText=now,
        required=True,
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
        required=True,
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
        htmlId="clsSnClassification"
    )
    peculiarInput = khufu.checkbox(
        optionText='peculiar',
        inline=True,
        htmlId="clsPeculiar",
        optionNumber=1
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
        htmlId="clsRedshift"
    )
    thisModal.add_form_object(
        formObject=redshiftInput,
        label="redshift"
    )

    sendToInput1 = khufu.radio(
        optionText='yes',
        optionNumber=1,
        htmlId="clsSendTo",
        checked=True
    )
    sendToInput2 = khufu.radio(
        optionText='no',
        optionNumber=2,
        htmlId="clsSendTo",
    )
    thisModal.add_form_object(
        formObject="%(sendToInput1)s %(sendToInput2)s" % locals(),
        label="send to atel queue"
    )

    classificationWRTMaxInput = khufu.select(
        optionList=["unknown", "pre-max", "at max", "post-max"],
        multiple=False,
        span=4,
        htmlId="clsClassificationWRTMax"
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
        buttonSize='default',  # [ large | default | small | mini ]
        href=modalTrigger,
        pull=False,  # right, left, center
        dataToggle="modal",  # [ modal ]
        popover=popover
    )

    return thisButton, modalForm

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
