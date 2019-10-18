#!/usr/local/bin/python
# encoding: utf-8
"""
*The identity block for the object ticket*

:Author:
    David Young

:Date Created:
    November 20, 2013
"""

import re
import datetime
import sys
import os
import numpy as np
import string
import khufu

from marshall_webapp.templates.commonelements import commonutils as cu


def identity_block(
        log,
        request,
        discoveryDataDictionary,
        objectAkas):
    """
    *get ticket identity block*

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
        - ``objectAkas`` -- the object akas

    **Return:**
        - ``identity_block`` -- the ticket identity block for the pesssto object
    """
    log.debug('starting the ``identity_block`` function')

    annotations = []

    pesstoCredentialsPopover = khufu.popover(
        tooltip=True,
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="""username: 'pessto'<br>password: '!explosions'""",
        content=False,
        delay=20
    )

    title = cu.block_title(
        log,
        title="identity"
    )

    q = discoveryDataDictionary['marshallWorkflowLocation'].lower()

    if discoveryDataDictionary['snoozed'] == 1:
        q = "snoozed"

    icon = ""
    if q == "inbox":
        icon = """<i class="icon-inbox"></i> inbox"""
    elif q == "review for followup":
        icon = """<i class="icon-eye"></i> review for followup"""
    elif q == "following":
        icon = """<i class="icon-pin"></i> following"""
    elif q == "archive":
        icon = """<i class="icon-archive"></i> archive"""
    elif q == "pending observation":
        icon = """<i class="icon-target2"></i> classification targets"""
    elif q == "followup complete":
        icon = """<i class="icon-checkmark-circle"></i> followup complete"""
    elif q == "snoozed":
        icon = """<i class="icon-alarm3"></i> snoozed""" % locals()

    if discoveryDataDictionary['snoozed'] == 2:
        unsnoozedIcon = """    <i class="icon-alarm3"></i> unsnoozed""" % locals()
        unsnoozedIcon = khufu.coloredText(
            text=unsnoozedIcon,
            color="red",
            size=3,  # 1-10
            pull=False,  # "left" | "right"
        )
    else:
        unsnoozedIcon = ""

    icon = khufu.coloredText(
        text=icon + unsnoozedIcon,
        color="cyan",
        size=3,  # 1-10
        pull=False,  # "left" | "right"
    )

    surveyObjectUrl = discoveryDataDictionary["surveyObjectUrl"]
    if surveyObjectUrl and "portal.nersc.gov/" in surveyObjectUrl:
        user = request.registry.settings["credentials"]["lsq"]["username"]
        pwd = request.registry.settings["credentials"]["lsq"]["password"]
        surveyObjectUrl = surveyObjectUrl.replace(
            "portal.", "%(user)s:%(pwd)s@portal." % locals())
    if surveyObjectUrl and "ps1gw" in surveyObjectUrl:
        annotations.append("within sky map of gravitational wave source")

    # if surveyObjectUrl and ("ps13pi" in surveyObjectUrl):
    #     user = request.registry.settings["credentials"]["ps1-3pi"]["username"]
    #     pwd = request.registry.settings["credentials"]["ps1-3pi"]["password"]
    #     surveyObjectUrl = surveyObjectUrl.replace(
    #         "star.", "%(user)s:%(pwd)s@star." % locals())

    # if surveyObjectUrl and ("ps1fgss" in surveyObjectUrl):
    #     user = request.registry.settings["credentials"]["ps1-fgss"]["username"]
    #     pwd = request.registry.settings["credentials"]["ps1-fgss"]["password"]
    #     surveyObjectUrl = surveyObjectUrl.replace(
    #         "star.", "%(user)s:%(pwd)s@star." % locals())

    # if surveyObjectUrl and ("ps1gw" in surveyObjectUrl):
    #     user = request.registry.settings["credentials"]["ps1-gw"]["username"]
    #     pwd = request.registry.settings["credentials"]["ps1-gw"]["password"]
    #     surveyObjectUrl = surveyObjectUrl.replace(
    #         "star.", "%(user)s:%(pwd)s@star." % locals())

    # MASTER NAME
    masterName = discoveryDataDictionary["masterName"]
    name = masterName
    if discoveryDataDictionary["survey"]:
        survey = discoveryDataDictionary["survey"].upper()
    else:
        survey = ""

    if surveyObjectUrl:
        if "skymapper" in surveyObjectUrl or "ps1gw" in surveyObjectUrl or "ps1fgss" in surveyObjectUrl or "ps13pi" in surveyObjectUrl:
            popover = pesstoCredentialsPopover
        else:
            popover = False

        masterNameLink = khufu.a(
            content=discoveryDataDictionary["masterName"],
            href=surveyObjectUrl,
            openInNewTab=True,
            popover=popover
        )
    else:
        masterNameLink = discoveryDataDictionary["masterName"]

    # AKA NAMES
    akaRows = []
    for item in objectAkas:

        surveyObjectUrl = item["url"]
        if item["transientBucketId"] == discoveryDataDictionary["transientBucketId"] and item["name"] != discoveryDataDictionary["masterName"]:
            if "@" not in surveyObjectUrl:
                if surveyObjectUrl and "portal.nersc.gov/" in surveyObjectUrl:
                    user = request.registry.settings[
                        "credentials"]["lsq"]["username"]
                    pwd = request.registry.settings[
                        "credentials"]["lsq"]["password"]
                    surveyObjectUrl = surveyObjectUrl.replace(
                        "portal.", "%(user)s:%(pwd)s@portal." % locals())

                # elif surveyObjectUrl and ("ps13pi" in surveyObjectUrl):
                #     user = request.registry.settings[
                #         "credentials"]["ps1-3pi"]["username"]
                #     pwd = request.registry.settings[
                #         "credentials"]["ps1-3pi"]["password"]
                #     surveyObjectUrl = surveyObjectUrl.replace(
                #         "star.", "%(user)s:%(pwd)s@star." % locals())

                # elif surveyObjectUrl and ("ps1fgss" in surveyObjectUrl):
                #     user = request.registry.settings[
                #         "credentials"]["ps1-fgss"]["username"]
                #     pwd = request.registry.settings[
                #         "credentials"]["ps1-fgss"]["password"]
                #     surveyObjectUrl = surveyObjectUrl.replace(
                #         "star.", "%(user)s:%(pwd)s@star." % locals())

                # elif surveyObjectUrl and ("ps1gw" in surveyObjectUrl):
                #     user = request.registry.settings[
                #         "credentials"]["ps1-gw"]["username"]
                #     pwd = request.registry.settings[
                #         "credentials"]["ps1-gw"]["password"]
                #     surveyObjectUrl = surveyObjectUrl.replace(
                #         "star.", "%(user)s:%(pwd)s@star." % locals())
            if surveyObjectUrl and "ps1gw" in surveyObjectUrl and "within sky map of gravitational wave source" not in annotations:
                annotations.append(
                    "within sky map of gravitational wave source")

            item["url"] = surveyObjectUrl
            akaRows.append(item)

    numerator = 70.
    if discoveryDataDictionary["classifiedFlag"]:
        numerator = 60.

    size = int(numerator / len(discoveryDataDictionary["masterName"]))
    if size > 6:
        size = 6

    masterName = khufu.coloredText(
        text="""%(masterNameLink)s""" % locals(),
        color="green",
        size=size,  # 1-10
        pull=False,  # "left" | "right"
    )

    masterName = """%(masterName)s""" % locals()

    masterName = khufu.grid_row(
        responsive=True,
        columns=masterName,
        htmlId=False,
        htmlClass="name",
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    # IMAGE STAMP
    transient_cache = request.static_path(
        "marshall_webapp:static/caches/transients/")
    download_prefix = "/marshall/static/caches/transients/"

    sourceImages = []
    dsourceImages = []
    objectNames = []

    stampFlags = {
        "user_added_stamp": "useradded_target_stamp.jpeg",
        "ps1_target_stamp": "ps1_target_stamp.jpeg",
        "gaia_stamp": "gaia_stamp.jpeg",
        "ogle_target_stamp": "ogle_target_stamp.jpeg",
        "atlas_target_stamp": "atlas_target_stamp.jpeg",
        "css_stamp": "css_stamp.jpeg",
        "des_target_stamp": "des_target_stamp.gif",
        "mls_stamp": "mls_stamp.jpeg",
        "sss_stamp": "sss_stamp.jpeg",
        "lsq_stamp": "lsq_stamp.jpeg",
        "master_stamp": "master_stamp.jpeg",
        "ztf_stamp": "ztf_triplet_stamp.jpeg"
    }

    hasStamp = False
    href = False
    for k, v in stampFlags.iteritems():
        if discoveryDataDictionary[k] == 1:
            hasStamp = True
            src = "%s%s/%s" % (transient_cache,
                               discoveryDataDictionary["transientBucketId"], v)
            dsrc = "%s%s/%s" % (download_prefix,
                                discoveryDataDictionary["transientBucketId"], v)
            sourceImages.append(src)
            dsourceImages.append(dsrc)
            objectName = ""
            for item in objectAkas:
                if k.split("_")[0] in item["name"].lower():
                    objectName = item["name"]
                    objectName = khufu.a(
                        content=objectName,
                        href=item["url"],
                        tableIndex=False,
                        # [ False | "dropdown" | "tab" | "modal" ],
                        triggerStyle=False,
                        htmlClass=False,
                        postInBackground=False,
                        openInNewTab=True,
                        popover=False
                    )
            objectNames.append(objectName)

    if discoveryDataDictionary["bsl_stamp"] and discoveryDataDictionary["tripletImageUrl"]:
        hasStamp = True
        remoteUrl = discoveryDataDictionary["tripletImageUrl"]
        theseLines = string.split(remoteUrl, '.')
        extension = theseLines[-1]
        stampName = "bsl_stamp.%(extension)s" % locals()
        src = "%s%s/bsl_stamp.%s" % (transient_cache,
                                     discoveryDataDictionary["transientBucketId"], extension)
        sourceImages.append(src)
        dsourceImages.append(src)
        objectNames.append("Bright SN List Stamp")

    if discoveryDataDictionary["targetImageUrl"] and hasStamp == False:
        src = discoveryDataDictionary["targetImageUrl"]
        dsrc = discoveryDataDictionary["targetImageUrl"]
        href = discoveryDataDictionary["targetImageUrl"]
        objectNames.append("User Added Stamp")
        sourceImages.append(src)
        dsourceImages.append(dsrc)

    if len(sourceImages) == 0:
        src = 'holder.js/400x400/auto/industrial/text:no stamp'
        dsrc = src
        sourceImages.append(src)
        dsourceImages.append(dsrc)

    src = sourceImages[0]
    dsrc = dsourceImages[0]

    objectName = discoveryDataDictionary["masterName"]
    if not href:
        href = request.route_path(
            'download', _query={'url': dsrc, "webapp": "marshall_webapp", "filename": "%(objectName)s_image_stamp" % locals()})

    imageSource = khufu.a(
        content='image source',
        href=surveyObjectUrl,
    )

    allImage = ""

    count = 0
    for s, d, n in zip(sourceImages, dsourceImages, objectNames):
        count += 1
        reminderImages = len(sourceImages) % 3
        if reminderImages == 0:
            span = 4
            offset = 0
        elif count < len(sourceImages[:-reminderImages]):
            span = 4
            offset = 0
        elif reminderImages == 2:
            span = 6
            offset = 0
        else:
            span = 6
            offset = 3

        if "marshall_webapp:" in s:
            href = request.static_path('%(s)s' % locals())
        else:
            href = s
        thisImage = khufu.image(
            src=s,  # [ industrial | gray | social ]
            href=href,
            display="rounded",  # [ rounded | circle | polaroid | False ]
            pull=False,  # [ "left" | "right" | "center" | False ]
            htmlClass=False,
            width="90%"
        )
        thisImage = khufu.grid_row(
            responsive=True,
            columns=thisImage,
        )
        # add text color
        name = khufu.coloredText(
            text=n,
            color="blue",
            size=7,  # 1-10
            pull=False,  # "left" | "right",
            addBackgroundColor=False
        )

        name = khufu.grid_row(
            responsive=True,
            columns=name,
        )
        column = khufu.grid_column(
            span=span,  # 1-12
            offset=offset,  # 1-12
            content=thisImage + name,
            pull=False,  # ["right", "left", "center"]
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        allImage += column

    grid_row = khufu.grid_row(
        responsive=True,
        columns=allImage,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    randNum = int(np.random.rand() * 10000)
    modal = khufu.modal(
        modalHeaderContent="Image Stamps for %(masterNameLink)s" % locals(
        ),
        modalBodyContent=grid_row,
        modalFooterContent="",
        htmlId="hookId%(randNum)s" % locals(),
        centerContent=True
    )
    objectStamp = khufu.image(
        src=sourceImages[0],  # [ industrial | gray | social ]
        href="#hookId%(randNum)s" % locals(),
        display="rounded",  # [ rounded | circle | polaroid | False ]
        pull=False,  # [ "left" | "right" | "center" | False ]
        htmlClass=False,
        width="100%",
        modal=True
    )
    objectStamp = objectStamp + modal

    surveyURLRanking = {
        "rochester": 0,
        "wis-tns": 1
    }

    akaList = ""
    if len(akaRows) == 0:
        akaTitle = ""
    elif len(akaRows) == 1:
        akaTitle = "aka: "
        row = akaRows[0]
        aka = row["name"]
        size = 3
        if len(aka) > 19:
            size = 2

        if "skymapper" in row["url"] or "ps1gw" in row["url"] or "ps1fgss" in row["url"] or "ps13pi" in row["url"] or "atlas" in row["url"]:
            popover = pesstoCredentialsPopover
        else:
            popover = False

        aka = khufu.a(
            content=aka,
            href=row["url"],
            openInNewTab=True,
            popover=pesstoCredentialsPopover
        )

        aka = khufu.coloredText(
            text=aka,
            color="orange",
            size=size,  # 1-10
            pull=False,  # "left" | "right"
        )
        akaList = aka
    else:
        akaTitle = "akas: "
        for row in akaRows:
            row["urlRank"] = 10
            for k, v in surveyURLRanking.iteritems():
                if k in row["url"]:
                    row["urlRank"] = v
        from operator import itemgetter
        akaRows = list(akaRows)
        akaRows = sorted(akaRows, key=itemgetter('urlRank'), reverse=True)

        for row in akaRows:
            log.debug('aka: %s' % (row,))
            aka = row["name"]
            if aka in akaList:
                continue

            if "skymapper" in row["url"] or "ps1gw" in row["url"] or "ps1fgss" in row["url"] or "ps13pi" in row["url"] or "atlas" in row["url"]:
                popover = pesstoCredentialsPopover
            else:
                popover = False

            aka = khufu.a(
                content=aka,
                href=row["url"],
                openInNewTab=True,
                popover=pesstoCredentialsPopover
            )
            aka = """&nbsp&nbsp&nbsp%(aka)s """ % locals()

            aka = khufu.coloredText(
                text=aka,
                color="orange",
                size=3,  # 1-10
                pull=False,  # "left" | "right"
            )

            aka = khufu.grid_row(
                responsive=True,
                columns=aka,
                htmlId=False,
                htmlClass="aka",
                onPhone=True,
                onTablet=True,
                onDesktop=True
            )
            akaList = "%(akaList)s %(aka)s" % locals()

    if len(akaList) != 0:
        akaTitle = cu.little_label(
            text=akaTitle,
            lineBreak=False
        )
        akaList = "%(akaTitle)s %(akaList)s" % locals()
        akaList = khufu.grid_row(
            responsive=True,
            columns=akaList,
            htmlId=False,
            htmlClass="akaList",
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

    pi = ""
    if discoveryDataDictionary["classifiedFlag"] == 1:

        pi = cu.little_label(
            text="PI: ",
            lineBreak=False
        )

        if discoveryDataDictionary["pi_name"]:
            pi_name = discoveryDataDictionary["pi_name"]
            firstName = pi_name.split(' ', 1)[0]
            thisName = discoveryDataDictionary["masterName"]
            pi_email = discoveryDataDictionary["pi_email"]
            pi_name = khufu.a(
                content="""%(pi_name)s&nbsp<i class="icon-mail7"></i>""" % locals(),
                href="mailto:%(pi_email)s?subject=%(thisName)s&body=Hi %(firstName)s," % locals(
                ),
                tableIndex=False,
                triggerStyle=False,  # [ False | "dropdown" | "tab" ],
                htmlClass=False,
                postInBackground=False
            )
        else:
            pi_name = "no pi set"

        pi_name = khufu.coloredText(
            text=pi_name,
            color="cyan",
            size=3,
        )

        pi = khufu.grid_row(
            responsive=True,
            columns="%(pi)s %(pi_name)s" % locals(),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        # convert bytes to unicode
        if isinstance(pi, str):
            pi = unicode(pi, encoding="utf-8", errors="replace")

    transientId = cu.little_label(
        text="pessto id: ",
        lineBreak=False
    )
    thisTransientBucketId = khufu.coloredText(
        text=discoveryDataDictionary["transientBucketId"],
        color="magenta",
        size=3,
    )

    observationalPriority = ""
    if discoveryDataDictionary["marshallWorkflowLocation"] in ["following", "pending observation"]:
        observationalPriority = cu.little_label(
            text="priority: ",
            lineBreak=False
        )
        if discoveryDataDictionary["marshallWorkflowLocation"] == "following":
            pList = ["CRITICAL", "IMPORTANT", "USEFUL", "NONE"]
            for n, w, c in zip([1, 2, 3, 4], pList, ["green", "yellow", "red", "blue"]):
                if discoveryDataDictionary["observationPriority"] == n:
                    thisObservationalPriority = w
                    thisColor = c
        else:
            pList = ["HIGH", "MEDIUM", "LOW"]
            for n, w, c in zip([1, 2, 3], pList, ["green", "yellow", "red"]):
                if discoveryDataDictionary["observationPriority"] == n:
                    thisObservationalPriority = w
                    thisColor = c

        thisObservationalPriority = "<strong>%(thisObservationalPriority)s</strong>" % locals(
        )
        thisObservationalPriority = khufu.coloredText(
            text=thisObservationalPriority,
            color=thisColor,
            size=3,
            htmlClass="priorityLabel"
        )
        observationalPriority = khufu.grid_row(
            responsive=True,
            columns="%(observationalPriority)s %(thisObservationalPriority)s" % locals(
            ),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

    transientId = khufu.grid_row(
        responsive=True,
        columns="%(transientId)s %(thisTransientBucketId)s" % locals(
        ),
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    listLocation = cu.little_label(
        text="list: ",
        lineBreak=False
    )

    listLocation = khufu.grid_row(
        responsive=True,
        columns="%(listLocation)s %(icon)s" % locals(
        ),
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    if len(annotations):
        icon = """<i class="icon-tag"></i>"""
        annotations = ("<BR>").join(annotations)
        # add text color
        annotations = khufu.coloredText(
            text="&nbsp&nbsp%(icon)s&nbsp<em>%(annotations)s</em>" % locals(),
            color="red",
            size=3,  # 1-10
            pull=False,  # "left" | "right",
            addBackgroundColor=False
        )

        annotations = khufu.grid_row(
            responsive=True,
            columns="%(annotations)s" % locals(
            ),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
    else:
        annotations = ""

    content = u"%(title)s %(masterName)s %(annotations)s %(objectStamp)s %(observationalPriority)s %(pi)s %(akaList)s %(listLocation)s %(transientId)s " % locals(
    )
    if isinstance(content, str):
        content = unicode(content, encoding="utf-8", errors="replace")

    return content
