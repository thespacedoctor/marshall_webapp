#!/usr/local/bin/python
# encoding: utf-8
"""
*The create followup OB object form for the SOXS Marshall*

:Author:
    David Young
"""
import sys
import os
from datetime import datetime, date, time
import khufu


def followup_ob_form(
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
    #Route that will receive the data
    postToScript = request.route_path(
        'transients_element_followup_obs', elementId=discoveryDataDictionary["transientBucketId"], _query={'method': 'post'})

    href = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"])

    # MODAL TITLE DEPENDS ON WHETHER THE OBJECT HAS BEEN PREVIOUSLY CLASSIFIED
    # OR NOT
    # formClassName -> followupobForm (HTML id)
    thisModal = khufu.modals.modalForm(
        log=log,
        title='Create a new Followup OB',
        postToScriptUrl=postToScript,
        reloadToUrl=href,
        formClassName="followupobForm"
    )

    sourceInput = khufu.select(
        optionList=["1.0x11", "1.5x11+", "5.0x11"],
        multiple=False,
        span=4,
        htmlId="slitWidth",
        required=True,
        defaultOption="1.0x11"
    )
    thisModal.add_form_object(
        formObject=sourceInput,
        label="Slit Width"
    )
    obsDateInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='text',
        placeholder='100',
        span=4,
        htmlId="expTime",
        inlineHelpText="Set the exposure time",
        required=True,
    )
    thisModal.add_form_object(
        formObject=obsDateInput,
        label="Exposure time"
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

    icon = """<i class="icon-sun2"></i>&nbsp"""
    thisButton = khufu.button(
        buttonText=icon,
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='danger',
        buttonSize='large',  # [ large | default | small | mini ]
        href=modalTrigger,
        pull=False,  # right, left, center
        dataToggle="modal",  # [ modal ]
        popover=popover
    )

    return thisButton, modalForm
