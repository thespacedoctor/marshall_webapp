#!/usr/local/bin/python
# encoding: utf-8
"""
*The classify object form for the PESSTO Marshall*

:Author:
    David Young
"""
import sys
import os
from datetime import datetime, date, time
import khufu


def classify_object_form(
    log,
    request,
    discoveryDataDictionary
):
    """classify object form

    **Key Arguments**

    - ``log`` -- the logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data


    **Return**

    - ``classifyObjectForm`` -- the modal form used to classify transients

    """
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    postToScript = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"], _query={'method': 'post'})

    href = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"])

    # MODAL TITLE DEPENDS ON WHETHER THE OBJECT HAS BEEN PREVIOUSLY CLASSIFIED
    # OR NOT
    if discoveryDataDictionary["recentClassification"]:
        title = "Please Update the Classification Details for %(masterName)s" % discoveryDataDictionary
    else:
        title = "Please add Classification Details for %(masterName)s" % discoveryDataDictionary
    thisModal = khufu.modals.modalForm(
        log=log,
        title=title,
        postToScriptUrl=postToScript,
        reloadToUrl=href,
        formClassName="classificationForm"
    )

    if discoveryDataDictionary["classificationSurvey"]:
        defaultOption = discoveryDataDictionary["classificationSurvey"]
    else:
        defaultOption = False
    sourceInput = khufu.select(
        optionList=["atel", "ePESSTO+", "cbat",
                    "private comm.", "GCN", "AstroNote", "ePESSTO", "PESSTO"],
        multiple=False,
        span=4,
        htmlId="clsSource",
        required=True,
        defaultOption=defaultOption
    )
    thisModal.add_form_object(
        formObject=sourceInput,
        label="source"
    )

    if discoveryDataDictionary["classificationDate"]:
        focusedInputText = discoveryDataDictionary[
            "classificationDate"].strftime("%Y-%m-%d")
    else:
        focusedInputText = now
    obsDateInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='text',
        placeholder='YYYY-MM-DD or mjd',
        span=4,
        htmlId="clsObsdate",
        inlineHelpText="YYYY-MM-DD or mjd",
        focusedInputText=focusedInputText,
        required=True,
    )
    thisModal.add_form_object(
        formObject=obsDateInput,
        label="classification date"
    )

    optionList = ["supernova", "agn", "variable star",
                  "galaxy", "cv", "LBV", "imposter",  "TDE", "GRB", "kilonova", "light echo", "featureless", "unknown"]
    disabled = False
    if discoveryDataDictionary["recentClassification"]:
        defaultOption = "supernova"
        for o in optionList:
            if o in discoveryDataDictionary["recentClassification"].lower():
                disabled = True
                defaultOption = o
    else:
        defaultOption = False

    typeInput = khufu.select(
        optionList=optionList,
        multiple=False,
        span=4,
        htmlId="clsType",
        required=True,
        defaultOption=defaultOption
    )
    thisModal.add_form_object(
        formObject=typeInput,
        label="object type"
    )

    optionList = ["I", "Ia", "Ib", "Ic", "Ibc", "Ibn", "I-CSM",  "II",
                  "IIb", "IIL", "IIP", "IIn", "SLSN I", "SLSN Ic", "SLSN II"]
    if discoveryDataDictionary["recentClassification"] and defaultOption == "supernova":
        for o in optionList:
            if o.lower() in discoveryDataDictionary["recentClassification"].lower():
                defaultOption = o
    else:
        defaultOption = False

    snClassificationInput = khufu.select(
        optionList=optionList,
        multiple=False,
        span=4,
        htmlId="clsSnClassification",
        disabled=disabled,
        defaultOption=defaultOption
    )

    if discoveryDataDictionary["recentClassification"] and "-pec" in discoveryDataDictionary["recentClassification"]:
        checked = True
    else:
        checked = False
    peculiarInput = khufu.checkbox(
        optionText='peculiar',
        inline=True,
        htmlId="clsPeculiar",
        optionNumber=1,
        disabled=disabled,
        checked=checked
    )
    thisModal.add_form_object(
        formObject="""%(snClassificationInput)s  &nbsp %(peculiarInput)s""" %
        locals(),
        label="sn classification"
    )

    if discoveryDataDictionary["best_redshift"]:
        r = discoveryDataDictionary["best_redshift"]
    elif discoveryDataDictionary["recentClassification"] and discoveryDataDictionary["transientRedshift"]:
        r = discoveryDataDictionary["transientRedshift"]
    else:
        r = False

    redshiftInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='float',
        placeholder='',
        span=4,
        htmlId="clsRedshift",
        focusedInputText=r
    )
    thisModal.add_form_object(
        formObject=redshiftInput,
        label="redshift"
    )

    checked = True
    if discoveryDataDictionary["recentClassification"]:
        checked = False
    sendToInput1 = khufu.radio(
        optionText='yes',
        optionNumber=1,
        htmlId="clsSendTo",
        checked=checked
    )
    checked = False
    if discoveryDataDictionary["recentClassification"]:
        checked = True
    sendToInput2 = khufu.radio(
        optionText='no',
        optionNumber=2,
        htmlId="clsSendTo",
        checked=checked
    )
    thisModal.add_form_object(
        formObject="%(sendToInput1)s %(sendToInput2)s" % locals(),
        label="send to astronote queue"
    )

    optionList = ["unknown", "pre-max", "at max", "post-max"]
    disabled = True
    if discoveryDataDictionary["classificationWRTMax"]:
        for o in optionList:
            if o.lower() in discoveryDataDictionary["classificationWRTMax"].lower():
                defaultOption = o
                if "-" in o:
                    disabled = False
    else:
        defaultOption = False

    classificationWRTMaxInput = khufu.select(
        optionList=["unknown", "pre-max", "at max", "post-max"],
        multiple=False,
        span=4,
        htmlId="clsClassificationWRTMax",
        defaultOption=defaultOption
    )

    thisModal.add_form_object(
        formObject=classificationWRTMaxInput,
        label="classifcation phase"
    )

    focusedInputText = False
    if discoveryDataDictionary["classificationPhase"]:
        focusedInputText = abs(discoveryDataDictionary["classificationPhase"])

    classificationPhaseInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='number',
        span=7,
        htmlId="clsClassificationPhase",
        pull=False,
        required=False,
        disabled=disabled,
        placeholder='unknown',
        prepend="?",
        focusedInputText=focusedInputText
    )
    thisModal.add_form_object(
        formObject=classificationPhaseInput,
        label="days from max"
    )

    modalForm, modalTrigger = thisModal.get()

    if discoveryDataDictionary["classifiedFlag"] == 0:
        title = "add a spectral classification for this object"
    else:
        title = "reclassify this object"

    popover = khufu.popover(
        tooltip=True,
        placement="right",
        trigger="hover",
        title=title,
        content=False,
    )

    icon = """<i class="icon-target2"></i>&nbsp"""
    thisButton = khufu.button(
        buttonText=icon,
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='success',
        buttonSize='large',  # [ large | default | small | mini ]
        href=modalTrigger,
        pull=False,  # right, left, center
        dataToggle="modal",  # [ modal ]
        popover=popover
    )

    return thisButton, modalForm
