#!/usr/local/bin/python
# encoding: utf-8
"""
*Create the change PI form*

:Author:
    David Young
"""
import sys
import os
import khufu

def change_pi_form(
    log,
    request,
    discoveryDataDictionary
):
    """change_pi_form

    **Key Arguments**

    - ``log`` -- the logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data
    

    **Return**

    - ``changePiForm`` -- the change PI modal form
    
    """
    postToScriptUrl = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"], _query={'method': 'put'})
    thisModal = khufu.modals.modalForm(
        log=log,
        title="Update PI details for %(masterName)s" % discoveryDataDictionary,
        postToScriptUrl=postToScriptUrl,
        reloadToUrl=request.path_qs
    )
    nameInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='text',
        placeholder='first and last name',
        span=6,
        htmlId="piName",
        required=True
    )
    thisModal.add_form_object(
        formObject=nameInput,
        label="Name"
    )

    emailInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='email',
        placeholder='PI email address',
        span=6,
        htmlId="piEmail",
        required=True
    )
    thisModal.add_form_object(
        formObject=emailInput,
        label="Email"
    )
    modalForm, modalTrigger = thisModal.get()

    if discoveryDataDictionary["pi_name"]:
        buttonText = """<i class="icon-user7"></i>&nbspPI"""
        details = "change the PI details"
    else:
        buttonText = """<i class="icon-user-add"></i>&nbspPI"""
        details = "add a PI for this object"

    popover = khufu.popover(
        tooltip=True,
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title=details,
        content=False,
        delay=20
    )

    icon = """<i class="icon-target2"></i>&nbsp"""
    thisButton = khufu.button(
        buttonText=buttonText,
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='success',
        buttonSize='large',  # [ large | default | small | mini ]
        href=modalTrigger,
        pull="right",  # right, left, center
        submit=False,
        block=False,
        disable=False,
        dataToggle="modal",  # [ modal ]
        popover=popover
    )

    return modalForm, thisButton
