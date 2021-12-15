#!/usr/local/bin/python
# encoding: utf-8
"""
*The create new ticket form for the PESSTO Marshall*

:Author:
    David Young
"""
import sys
import os
import khufu

def create_new_ticket_form(
    log,
    request
):
    """create_new_ticket_form

    **Key Arguments**

    - ``log`` -- the logger
    - ``request`` -- the pyramid request
    

    **Return**

    - ``createNewTicketForm``
    
    """
    postToScriptUrl = request.route_path(
        'transients', _query={'method': 'post'})
    reloadToUrl = href = request.route_path(
        'transients_search', _query={'q': 'value'})

    thisModal = khufu.modals.modalForm(
        log=log,
        title="Add a new object to the Marshall Inbox",
        postToScriptUrl=postToScriptUrl,
        reloadToUrl=False
    )

    textInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='text',
        placeholder='',
        span=5,
        htmlId="objectName",
        required=True
    )
    thisModal.add_form_object(
        formObject=textInput,
        label="object name"
    )

    urlInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='url',
        placeholder='url of object image',
        span=5,
        htmlId="objectImageStamp",
    )
    thisModal.add_form_object(
        formObject=urlInput,
        label="image"
    )

    urlInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='url',
        placeholder='url for survey page, ATel or CBET',
        span=5,
        htmlId="objectUrl",
    )
    thisModal.add_form_object(
        formObject=urlInput,
        label="object data url"
    )

    textInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='text',
        placeholder='lsq, BOSS ...',
        span=5,
        htmlId="objectSurvey",
        disabled=False,
        hidden=False,
        defaultValue=False
    )
    thisModal.add_form_object(
        formObject=textInput,
        label="survey"
    )

    textInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='text',
        placeholder='',
        span=5,
        htmlId="objectRa",
        inlineHelpText="e.g. <em>10:20:30.23</em> or <em>155.125958333</em>",
        required=True
    )
    thisModal.add_form_object(
        formObject=textInput,
        label="ra"
    )

    textInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='text',
        placeholder='',
        span=5,
        htmlId="objectDec",
        required=True,
        inlineHelpText="e.g. <em>-15:10:43.453</em> or <em>-15.1787369444</em>",
    )
    thisModal.add_form_object(
        formObject=textInput,
        label="dec"
    )

    floatInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='float',
        placeholder='',
        span=5,
        htmlId="objectRedshift"
    )
    thisModal.add_form_object(
        formObject=floatInput,
        label="redshift"
    )

    floatInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='float',
        placeholder='',
        span=5,
        htmlId="objectMagnitude",
        required=True
    )
    thisModal.add_form_object(
        formObject=floatInput,
        label="magnitude"
    )

    textInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='text',
        placeholder='date or mjd',
        span=5,
        htmlId="objectDate",
        inlineHelpText="e.g. 2013-12-01 or 56627.5",
        required=True,
    )
    thisModal.add_form_object(
        formObject=textInput,
        label="discovery date"
    )

    modalForm, modalTrigger = thisModal.get()

    popover = khufu.popover(
        tooltip=True,
        placement="right",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="manually create a ticket for a new object",
        content=False,
        delay=20
    )

    thisButton = khufu.button(
        buttonText='create<br>new ticket',
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='danger',
        buttonSize='default',  # [ large | default | small | mini ]
        href=modalTrigger,
        pull=False,  # right, left, center
        submit=False,
        block=True,
        disable=False,
        dataToggle="modal",  # [ modal ]
        htmlId="createNewTicketButton",
        popover=popover
    )

    thisButton = khufu.grid_column(
        span=11,  # 1-12
        offset=1,  # 1-12
        content=thisButton
    )

    return modalForm, thisButton
