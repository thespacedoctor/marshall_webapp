#!/usr/local/bin/python
# encoding: utf-8
"""
actions_block.py
================
:Summary:
    The actions block for the marshall object tickets

:Author:
    David Young

:Date Created:
    January 10, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from datetime import datetime, date, time
from docopt import docopt
from dryxPython import commonutils as dcu
import khufu
from .....commonelements import commonutils as cu


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 10, 2014
# CREATED : January 10, 2014
# AUTHOR : DRYX
def actions_block(
        log,
        request,
        discoveryDataDictionary,
        lightcurveData,
        objectAkas):
    """get ticket action block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``lightcurveData`` -- the lightdata for the object
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.

    **Return:**
        - ``action_block`` -- the ticket identity block for the pesssto object

    **Todo**
    """
    from .....commonelements import forms
    title = cu.block_title(
        log,
        title="actions"
    )

    buttonList = []

    moveToDropdown = _get_move_to_dropdown(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )
    moveToDropdown = khufu.grid_row(
        responsive=True,
        columns=moveToDropdown,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
    )

    alertDropdown = _get_alert_dropdown(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )
    alertDropdown = khufu.grid_row(
        responsive=True,
        columns=alertDropdown,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
    )

    classifyButton = _get_classify_button(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )

    if classifyButton:
        classifyButton = khufu.grid_row(
            responsive=True,
            columns=classifyButton,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True,
        )

    if not classifyButton:
        classifyButton = ""

    changePiButton = ""
    if discoveryDataDictionary["classifiedFlag"] == 1:
        changePiButton = _get_change_pi_button(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
        )

    generateOBButton = ""
    if discoveryDataDictionary["classifiedFlag"] == 0:
        generateOBButton = _generate_ob_button(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
            lightcurveData=lightcurveData,
            objectAkas=objectAkas,
        )

    return "%(title)s %(moveToDropdown)s %(alertDropdown)s %(classifyButton)s %(changePiButton)s %(generateOBButton)s" % locals()


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
# LAST MODIFIED : November 29, 2013
# CREATED : November 29, 2013
# AUTHOR : DRYX


def _get_classify_button(
        log,
        request,
        discoveryDataDictionary,
):
    """ get classify button for the ticket topbar

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request object
        - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    **Return:**
        - ``button`` -- the classification button with hidden modal form

    **Todo**
    """
    from .....commonelements import forms
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    log.info('starting the ``_get_classify_button`` function')
    # TEST THE ARGUMENTS

    ## VARIABLES ##
    if discoveryDataDictionary["classifiedFlag"] == 0:

        popover = khufu.popover(
            tooltip=True,
            placement="right",
            trigger="hover",
            title="add a spectral classification for this object",
            content=False,
        )

        button = khufu.button(
            buttonText='<i class="icon-target2"></i>',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='success',
            buttonSize='small',  # [ large | default | small | mini ]
            href="#classifyForm%(transientBucketId)s" % discoveryDataDictionary,
            pull="right",
            submit=False,
            block=False,
            disable=False,
            dataToggle="modal",
            popover=popover
        )
        button, thisForm = forms.classify_object_form.classify_object_form(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary
        )
        button = "%(button)s %(thisForm)s" % locals()
    else:
        button = None

    log.info('completed the ``_get_classify_button`` function')
    return button

# LAST MODIFIED : November 29, 2013
# CREATED : November 29, 2013
# AUTHOR : DRYX


def _get_move_to_dropdown(
        log,
        request,
        discoveryDataDictionary,
):
    """ get move to dropdown for the ticket

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    **Return:**
        - ``thisDropdown`` -- the move to other list dropdown

    **Todo**
    """
    import datetime

    log.info('starting the ``_get_move_to_dropdown`` function')

    dropdownTitle = """<i class="icon-list-ul"></i>"""

    thisMwl = discoveryDataDictionary["marshallWorkflowLocation"].lower()
    if thisMwl == "inbox":
        linkTitleList = ["classification targets", "archive"]
    elif thisMwl == "review for followup":
        linkTitleList = ["followup targets", "archive"]
    elif thisMwl == "pending observation":
        linkTitleList = ["inbox", "observed", "archive"]
    elif thisMwl == "following":
        linkTitleList = ["followup complete"]
    elif thisMwl == "followup complete":
        linkTitleList = ["followup targets"]
    elif thisMwl == "archive":
        linkTitleList = ["inbox"]
    elif thisMwl == "pending classification":
        dropdownTitle = "fail"
        linkTitleList = ["classification targets", "archive"]

    linkList = []

    for title in linkTitleList:

        mwl = title
        if title == "classification targets":
            mwl = "pending observation"
        elif title == "followup targets":
            mwl = "following"
        elif title == "observed":
            mwl = "pending classification"

        discoveryDataDictionary["mwl"] = mwl

        prefix = request.registry.settings["apache prefix"]
        discoveryDataDictionary["prefix"] = prefix

        name = discoveryDataDictionary["masterName"]
        name = khufu.a(
            content=name,
            href="/marshall/index.py?searchString=%(name)s" % locals(),
        )
        newListLink = khufu.a(
            content=title,
            href="/marshall/index.py?mwl=%(mwl)s" % locals(),
        )

        # GENERATE THE UNDO LINK
        href = request.route_path('transients_element', elementId=discoveryDataDictionary[
                                  "transientBucketId"], _query={'mwl': discoveryDataDictionary["marshallWorkflowLocation"], "method": "put"})
        undoLink = khufu.a(
            content='undo.',
            href=href,
            htmlClass="ticketMoveToLinkUndo",
            htmlId="ticket%(transientBucketId)s" % discoveryDataDictionary,
            postInBackground=True,
        )

        notification = "%(name)s was moved to the %(newListLink)s list. %(undoLink)s" % locals(
        )
        notification = khufu.alert(
            alertText=notification,
            alertHeading='',
            extraPadding=False,
            alertLevel='info'  # [ "warning" | "error" | "success" | "info" ]
        )
        import urllib
        notification = urllib.quote(notification)
        discoveryDataDictionary["notification"] = notification

        href = request.route_path('transients_element', elementId=discoveryDataDictionary[
                                  "transientBucketId"], _query={'mwl': mwl, "method": "put"})
        link = khufu.a(
            content=title,
            href=href,
            tableIndex=-1,
            triggerStyle=False,  # [ False | "dropdown" | "tab" ]
            htmlClass="ticketMoveToLink",
            notification=notification,
            postInBackground=True,
        )
        linkListItem = khufu.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        linkList.append(linkListItem)

    popover = khufu.popover(
        tooltip=True,
        placement="right",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="move object to another list",
        content=False,
        delay=200
    )

    thisDropdown = khufu.dropdown(
        buttonSize='small',
        buttonColor='success',  # [ default | sucess | error | warning | info ]
        menuTitle=dropdownTitle,
        splitButton=False,
        linkList=linkList,
        separatedLinkList=False,
        pull="right",
        direction=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        popover=popover
    )

    log.info('completed the ``_get_move_to_dropdown`` function')
    return thisDropdown

# LAST MODIFIED : November 29, 2013
# CREATED : November 29, 2013
# AUTHOR : DRYX


def _get_alert_dropdown(
        log,
        request,
        discoveryDataDictionary,
):
    """ get alert dropdown for the ticket

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    **Return:**
        - ``thisDropdown`` -- the move to other alert list dropdown

    **Todo**
    """
    import datetime

    log.info('starting the ``_get_alert_dropdown`` function')

    dropdownTitle = "alert"

    cf = discoveryDataDictionary["classifiedFlag"]
    awl = discoveryDataDictionary["alertWorkflowLocation"]

    thisDropdown = ""
    linkList = []
    if cf == 1 and awl == "queued for atel":
        linkTitleList = ["atel released", "no atel to be released"]

        for title in linkTitleList:

            awl = title
            if title == "atel released":
                awl = "pessto classification released"
            elif title == "no atel to be released":
                awl = "archived without alert"

            discoveryDataDictionary["awl"] = awl

            prefix = request.registry.settings["apache prefix"]
            discoveryDataDictionary["prefix"] = prefix

            href = request.route_path('transients_element', elementId=discoveryDataDictionary[
                "transientBucketId"], _query={'awl': awl, "method": "put"})
            link = khufu.a(
                content=title,
                href=href,
                tableIndex=-1,
                triggerStyle=False,  # [ False | "dropdown" | "tab" ]
                htmlClass="ticketMoveToLink",
                postInBackground=True,
            )
            linkListItem = khufu.li(
                content=link,  # if a subMenu for dropdown this should be <ul>
                span=False,  # [ False | 1-12 ]
                disabled=False,
                submenuTitle=False,
                divider=False,
                navStyle=False,  # [ active | header ]
                navDropDown=False,
                pager=False  # [ False | "previous" | "next" ]
            )
            linkList.append(linkListItem)

        thisDropdown = khufu.dropdown(
            buttonSize='small',
            # [ default | sucess | error | warning | info ]
            buttonColor='default',
            menuTitle=dropdownTitle,
            splitButton=False,
            linkList=linkList,
            separatedLinkList=False,
            pull="right",
            direction=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

    log.info('completed the ``_get_alert_dropdown`` function')
    return thisDropdown


# LAST MODIFIED : February 21, 2014
# CREATED : February 21, 2014
# AUTHOR : DRYX

def _get_change_pi_button(
        log,
        request,
        discoveryDataDictionary,
):
    """ get change pi for the ticket action block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    **Return:**
        - ``button`` -- the change PI button and hidden modal form

    **Todo**
    """
    from .....commonelements import forms

    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    log.info('starting the ``_get_change_pi_button`` function')
    # TEST THE ARGUMENTS

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
        delay=200
    )

    ## VARIABLES ##
    button = khufu.button(
        buttonText=buttonText,
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='success',
        buttonSize='small',  # [ large | default | small | mini ]
        href="#changePiForm%(transientBucketId)s" % discoveryDataDictionary,
        pull="right",
        submit=False,
        block=False,
        disable=False,
        dataToggle="modal",
        popover=popover
    )
    changePiForm = forms.change_pi_form.change_pi_form(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )
    button = "%(button)s %(changePiForm)s" % locals()

    log.info('completed the ``_get_change_pi_button`` function')
    return button


# LAST MODIFIED : March 7, 2014
# CREATED : March 7, 2014
# AUTHOR : DRYX


def _generate_ob_button(
        log,
        request,
        discoveryDataDictionary,
        lightcurveData,
        objectAkas,
):
    """ get generate OB button for the ticket action block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data
        - ``lightcurveData`` -- lightcurve data for the object
        - ``objectAkas`` -- the akas of the object

    **Return:**
        - ``button`` - the generate OB button with hidden modal form

    **Todo**
    """
    from .....commonelements import forms
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    log.info('starting the ``_get_classify_button`` function')
    # TEST THE ARGUMENTS

    ## VARIABLES ##
    if discoveryDataDictionary["classifiedFlag"] == 0:

        thisForm, button = forms.generate_ob_form.generate_ob_form(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
            lightcurveData=lightcurveData,
            objectAkas=objectAkas,
        )
        button = "%(button)s %(thisForm)s" % locals()
    else:
        button = None

    log.info('completed the ``_get_classify_button`` function')
    return button


if __name__ == '__main__':
    main()
