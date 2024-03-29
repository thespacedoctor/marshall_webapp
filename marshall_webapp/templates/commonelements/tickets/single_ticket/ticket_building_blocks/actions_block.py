#!/usr/local/bin/python
# encoding: utf-8
"""
*The actions block for the marshall object tickets*

:Author:
    David Young
"""
import sys
import os
from datetime import datetime, date, time
import khufu
from marshall_webapp.templates.commonelements import commonutils as cu
import urllib.parse


def actions_block(
        log,
        request,
        discoveryDataDictionary,
        lightcurveData,
        objectAkas):
    """return a ticket action block

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
    - ``lightcurveData`` -- the lightdata for the object
    - ``objectAkas`` -- the transients names from various surveys
    """
    from marshall_webapp.templates.commonelements import forms
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

    alertDropdown = _get_alert_dropdown(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )

    classifyButton, classifyForm = _get_classify_button(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )

    if not classifyButton:
        classifyButton = ""
        classifyForm = ""

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

    changePriorityDropdown = ""
    if discoveryDataDictionary["marshallWorkflowLocation"] in ["pending observation", "allObsQueue", "following"]:
        changePriorityDropdown = _get_priority_switcher_dropdown(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
        )

    snoozeButton = ""
    if discoveryDataDictionary["marshallWorkflowLocation"].lower() == "inbox":
        snoozeButton = _snooze_button(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
        )

    buttonGroup = khufu.buttonGroup(
        buttonList=[
            changePriorityDropdown,
            moveToDropdown,
            alertDropdown,
            classifyButton,
            changePiButton,
            generateOBButton,
            snoozeButton
        ],
        format='vertical'  # [ default | toolbar | vertical ]
    )

    return "%(title)s %(buttonGroup)s %(classifyForm)s" % locals()


def _get_classify_button(
        log,
        request,
        discoveryDataDictionary,
):
    """return a classification button with hidden modal form

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request object
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data
    """
    log.debug('starting the ``_get_classify_button`` function')

    from marshall_webapp.templates.commonelements import forms
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    ## VARIABLES ##
    button, thisForm = forms.classify_object_form.classify_object_form(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary
    )

    log.debug('completed the ``_get_classify_button`` function')
    return button, thisForm


def _get_move_to_dropdown(
        log,
        request,
        discoveryDataDictionary,
):
    """return the 'move to' dropdown for the ticket (from defined workflow in yaml settings)

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    """
    import datetime

    log.debug('starting the ``_get_move_to_dropdown`` function')

    dropdownTitle = """<i class="icon-list-ul"></i>"""
    icon = """<i class="icon-circle-arrow-up"></i>"""
    prefix = request.registry.settings["apache prefix"]
    discoveryDataDictionary["prefix"] = prefix

    # SET OBSERVATIONAL PRIORITY NUMBERS
    priorityList = ["high", "medium", "low"]
    priorityColor = ["green", "yellow", "red"]
    priorityNumberList = [1, 2, 3]

    # GET CURRENT STATE OF TICKET
    currentMwl = discoveryDataDictionary["marshallWorkflowLocation"].lower()
    currentCf = discoveryDataDictionary["classifiedFlag"]
    currentSnoozed = discoveryDataDictionary["snoozed"]
    currentPriority = discoveryDataDictionary["observationPriority"]
    name = discoveryDataDictionary["masterName"]

    linkTitleList = []
    linkList = []
    if currentMwl in request.registry.settings[
            "workflow-buttons"]:

        for title, buttonSetting in request.registry.settings["workflow-buttons"][currentMwl].items():

            if currentCf and "hide for classified" in buttonSetting and buttonSetting["hide for classified"]:
                continue
            elif not currentCf and "hide for unclassified" in buttonSetting and buttonSetting["hide for unclassified"]:
                continue
            elif currentSnoozed and "hide for snoozed" in buttonSetting and buttonSetting["hide for snoozed"]:
                continue
            elif not currentSnoozed and "hide for non-snoozed" in buttonSetting and buttonSetting["hide for non-snoozed"]:
                continue

            linkTitleList.append(title)
            # SET NEW LOCATION
            discoveryDataDictionary["mwl"] = buttonSetting["mwf"]
            # SET BUTTON TITLE (WITH ICON AND PRIORITY COLOUR)
            num = False
            if buttonSetting["priority"] and buttonSetting["icon"]:
                # DETERMINE OBSERVATIONAL PRIORITY
                for l, n, c in zip(priorityList, priorityNumberList, priorityColor):
                    if l == buttonSetting["priority"].lower():
                        # add text color
                        text = khufu.coloredText(
                            text=f'<i class="{buttonSetting["icon"]} style="vertical-align: -.2em;""></i>',
                            color=c,
                            size=False,  # 1-10
                            pull=False,  # "left" | "right",
                            addBackgroundColor=False
                        )
                        title =  f"""{text} &nbsp{title}"""
                        num = n
            elif buttonSetting["icon"]:
                title =  f"""<i class="{buttonSetting["icon"]}"  style="vertical-align: -.2em;"></i> &nbsp{title}"""

            # CREATE THE LINK
            href = request.route_path(
                'transients_element', elementId=discoveryDataDictionary["transientBucketId"])
            name = khufu.a(
                content=name,
                href=href
            )

            href = request.route_path('transients', _query={
                                      'mwl': buttonSetting["mwf"]})
            newListLink = khufu.a(
                content=buttonSetting["destination-sidebar-title"],
                href=href
            )
            # CREATE THE UNDO LINK FOR NOTIFICATION
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
                # [ "warning" | "error" | "success" | "info" ]
                alertLevel='info'
            )

            notification = urllib.parse.quote(notification, safe='')
            discoveryDataDictionary["notification"] = notification

            href = request.route_path('transients_element', elementId=discoveryDataDictionary[
                                      "transientBucketId"], _query={'mwl': buttonSetting["mwf"], 'observationPriority': num, "method": "put"})
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
        delay=20
    )

    thisDropdown = khufu.dropdown(
        buttonSize='large',
        buttonColor='success',  # [ default | sucess | error | warning | info ]
        menuTitle=dropdownTitle,
        splitButton=False,
        linkList=linkList,
        separatedLinkList=False,
        pull=False,
        direction=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        popover=popover
    )

    log.debug('completed the ``_get_move_to_dropdown`` function')
    return thisDropdown


def _get_alert_dropdown(
        log,
        request,
        discoveryDataDictionary,
):
    """ get alert dropdown for the ticket

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data


    **Return**

    - ``thisDropdown`` -- the move to other alert list dropdown

    """
    import datetime

    log.debug('starting the ``_get_alert_dropdown`` function')

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
            buttonSize='large',
            # [ default | sucess | error | warning | info ]
            buttonColor='success',
            menuTitle=dropdownTitle,
            splitButton=False,
            linkList=linkList,
            separatedLinkList=False,
            pull=False,
            direction=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

    log.debug('completed the ``_get_alert_dropdown`` function')
    return thisDropdown


def _get_change_pi_button(
        log,
        request,
        discoveryDataDictionary,
):
    """ get change pi for the ticket action block

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data


    **Return**

    - ``button`` -- the change PI button and hidden modal form

    """
    from marshall_webapp.templates.commonelements import forms

    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    log.debug('starting the ``_get_change_pi_button`` function')
    # TEST THE ARGUMENTS

    ## VARIABLES ##
    changePiForm, button = forms.change_pi_form.change_pi_form(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )
    button = "%(button)s %(changePiForm)s" % locals()

    log.debug('completed the ``_get_change_pi_button`` function')
    return button


def _generate_ob_button(
        log,
        request,
        discoveryDataDictionary,
        lightcurveData,
        objectAkas,
):
    """ get generate OB button for the ticket action block

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data
    - ``lightcurveData`` -- lightcurve data for the object
    - ``objectAkas`` -- the akas of the object


    **Return**

    - ``button`` - the generate OB button with hidden modal form

    """
    from marshall_webapp.templates.commonelements import forms
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    log.debug('starting the ``_get_classify_button`` function')
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

    log.debug('completed the ``_get_classify_button`` function')
    return button


def _get_priority_switcher_dropdown(
        request,
        discoveryDataDictionary,
        log):
    """ get priority switcher dropdown

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    """
    log.debug('starting the ``_get_priority_switcher_dropdown`` function')
    import datetime

    log.debug('starting the ``_get_move_to_dropdown`` function')

    dropdownTitle = """<span class="colortext red"><i class="icon-fire"></i></span>"""
    dropdownTitle = """<i class="icon-fire"></i>"""

    # Add the appropriate titles to the dropdown
    linkTitleList = []
    linkPriorityList = []
    linkHiddenList = []
    if discoveryDataDictionary["marshallWorkflowLocation"] == "following":
        priorityList = ["critical", "important", "useful", "none"]
        priorityNumberList = [1, 2, 3, 4]
    else:
        priorityList = ["high", "medium", "low"]
        priorityNumberList = [1, 2, 3]
    priority = discoveryDataDictionary["observationPriority"]
    for l, n in zip(priorityList, priorityNumberList):
        linkTitleList.append(l)
        linkPriorityList.append(n)
        if priority != n:
            linkHiddenList.append(False)
        else:
            linkHiddenList.append(True)

    linkList = []
    for title, num, hidden in zip(linkTitleList, linkPriorityList, linkHiddenList):

        prefix = request.registry.settings["apache prefix"]
        discoveryDataDictionary["prefix"] = prefix
        name = discoveryDataDictionary["masterName"]
        href = request.route_path(
            'transients_element', elementId=discoveryDataDictionary["transientBucketId"])
        name = khufu.a(
            content=name,
            href=href
        )

        # GENERATE THE UNDO LINK
        href = request.route_path('transients_element', elementId=discoveryDataDictionary[
                                  "transientBucketId"], _query={'observationPriority': num, "method": "put"})
        undoLink = khufu.a(
            content='undo.',
            href=href,
            htmlClass="changePriorityLinkUndo",
            htmlId="ticket%(transientBucketId)s" % discoveryDataDictionary,
            postInBackground=True,
        )

        notification = "the observational priorty for %(name)s was changed to %(title)s. %(undoLink)s" % locals(
        )
        notification = khufu.alert(
            alertText=notification,
            alertHeading='',
            extraPadding=False,
            alertLevel='info'  # [ "warning" | "error" | "success" | "info" ]
        )
        notification = urllib.parse.quote(notification, safe='')
        discoveryDataDictionary["notification"] = notification

        href = request.route_path('transients_element', elementId=discoveryDataDictionary[
                                  "transientBucketId"], _query={'observationPriority': num, "method": "put"})
        link = khufu.a(
            content=title,
            href=href,
            tableIndex=-1,
            triggerStyle=False,  # [ False | "dropdown" | "tab" ]
            htmlClass="changePriorityLink",
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
            pager=False,  # [ False | "previous" | "next" ]
            hidden=hidden
        )
        linkList.append(linkListItem)

    popover = khufu.popover(
        tooltip=True,
        placement="right",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="set the observational priority of this object",
        content=False,
        delay=20
    )

    thisDropdown = khufu.dropdown(
        buttonSize='large',
        buttonColor='success',  # [ default | sucess | error | warning | info ]
        menuTitle=dropdownTitle,
        splitButton=False,
        linkList=linkList,
        separatedLinkList=False,
        pull=False,
        direction=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        popover=popover
    )

    log.debug('completed the ``_get_priority_switcher_dropdown`` function')
    return thisDropdown


def _snooze_button(
        request,
        discoveryDataDictionary,
        log):
    """ snooze button

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data

    """
    log.debug('starting the ``_snooze_button`` function')

    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    log.debug('starting the ``_get_change_pi_button`` function')
    # TEST THE ARGUMENTS

    mwl = discoveryDataDictionary["marshallWorkflowLocation"]

    name = discoveryDataDictionary["masterName"]
    href = request.route_path(
        'transients_element', elementId=discoveryDataDictionary["transientBucketId"])
    name = khufu.a(
        content=name,
        href=href
    )
    href = request.route_path('transients', _query={'mwl': mwl})
    newListLink = khufu.a(
        content="archive",
        href=href
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

    notification = "%(name)s was snoozed. %(undoLink)s" % locals(
    )
    notification = khufu.alert(
        alertText=notification,
        alertHeading='',
        extraPadding=False,
        alertLevel='info'  # [ "warning" | "error" | "success" | "info" ]
    )
    notification = urllib.parse.quote(notification, safe='')
    discoveryDataDictionary["notification"] = notification

    href = request.route_path('transients_element', elementId=discoveryDataDictionary[
        "transientBucketId"], _query={'mwl': "archive", "method": "put", "snoozed": True})

    popover = khufu.popover(
        tooltip=True,
        placement="right",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="snooze - hide object until more photometry obtained",
        content=False,
        delay=20
    )

    ## VARIABLES ##
    button = khufu.button(
        buttonText='<i class="icon-alarm3"></i>',
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='success',
        buttonSize='large',  # [ large | default | small | mini ]
        htmlId="snooze",
        htmlClass="ticketMoveToLink",
        href=href,
        pull=False,  # right, left, center
        submit=False,
        block=False,
        disable=False,
        postInBackground=True,
        dataToggle=False,  # [ modal ]
        popover=popover,
        notification=notification
    )

    log.debug('completed the ``_snooze_button`` function')
    return button

# xt-def-with-logger
