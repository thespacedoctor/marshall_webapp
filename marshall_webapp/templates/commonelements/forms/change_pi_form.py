#!/usr/local/bin/python
# encoding: utf-8
"""
change_pi_form.py
=================
:Summary:
    Create the change PI form

:Author:
    David Young

:Date Created:
    February 21, 2014

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
# LAST MODIFIED : February 21, 2014
# CREATED : February 21, 2014
# AUTHOR : DRYX


def change_pi_form(
    log,
    request,
    discoveryDataDictionary
):
    """change_pi_form

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    **Return:**
        - None

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu

    nameInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='text',
        placeholder='first and last name',
        span=12,
        htmlId="piName",
        pull=False,
        prepend=False,
        append=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=True,
        disabled=False
    )
    nameInput = khufu.controlRow(
        inputList=[nameInput, ]
    )
    nameLabel = khufu.horizontalFormControlLabel(
        labelText='Name',
        forId="piName"
    )
    nameCG = khufu.horizontalFormControlGroup(
        content=nameLabel + nameInput,
        validationLevel=False
    )
    emailInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='email',
        placeholder='PI email address',
        span=12,
        htmlId="piEmail",
        prepend=False,
        append=False,
        pull=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=True,
        disabled=False
    )
    emailInput = khufu.controlRow(
        inputList=[emailInput, ]
    )
    emailLabel = khufu.horizontalFormControlLabel(
        labelText='Email',
        forId="piEmail"
    )
    emailCG = khufu.horizontalFormControlGroup(
        content=emailLabel + emailInput,
        validationLevel=False
    )

    numberInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='number',
        htmlId="transientBucketId",
        hidden=True,
        defaultValue=discoveryDataDictionary["transientBucketId"]
    )

    nameInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='text',
        htmlId="masterName",
        hidden=True,
        defaultValue=discoveryDataDictionary["masterName"]
    )

    # BUTTON GROUP
    updateButton = khufu.button(
        buttonText='update',
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='info',
        buttonSize='default',  # [ large | default | small | mini ]
        htmlId="changePiFormSubmitButton",
        href=False,
        pull=False,  # right, left, center
        submit=True,
        block=False,
        disable=False,
        dataToggle=False
    )
    cancelbutton = khufu.button(
        buttonText='cancel',
        buttonStyle='danger',
        buttonSize='default',  # [ large | default | small | mini ]
        close=True
    )
    buttonGroup = khufu.buttonGroup(
        buttonList=[cancelbutton, updateButton],
        format='default'  # [ default | toolbar | vertical ]
    )

    prefix = request.registry.settings["apache prefix"]
    href = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"], _query={'method': 'put'})
    changePiForm = khufu.form(
        content='%(nameCG)s %(emailCG)s %(numberInput)s %(nameInput)s %(buttonGroup)s' % locals(
        ),
        formType='horizontal',
        navBarPull=False,  # [ false | right | left ],
        postToScript=href,
        span=8,
        offset=2,
        redirectUrl=request.url
    )

    changePiForm = khufu.modals.modal(
        modalHeaderContent="Update PI details for %(masterName)s" % discoveryDataDictionary,
        modalBodyContent=changePiForm,
        modalFooterContent="",
        htmlId="changePiForm%(transientBucketId)s" % discoveryDataDictionary
    )

    return changePiForm


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
