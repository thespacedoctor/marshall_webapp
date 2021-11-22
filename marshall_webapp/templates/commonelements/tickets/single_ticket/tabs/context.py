#!/usr/local/bin/python
# encoding: utf-8
"""
*The context tab for the PESSTO Object tickets*

:Author:
    David Young
"""
import sys
import os
import datetime
import re
import khufu
from marshall_webapp.templates.commonelements.tickets.single_ticket import ticket_building_blocks
from marshall_webapp.templates.commonelements import commonutils as cu


def context_tab(
        log,
        request,
        discoveryDataDictionary,
        objectAkas,
        atelData,
        lightcurveData,
        transientCrossmatches):
    """context tab

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
    - ``objectAkas`` -- object akas
    - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
    - ``atelData`` -- the atel matches for the objects displayed on the webpage
    - ``transientCrossmatches`` -- catalogue crossmatches (from sherlock)


    **Return**

    - ``context_tab`` -- the lightcurve/context tab for a single ticket on the transient listings page

    """
    from marshall_webapp.templates.commonelements.tickets import single_ticket

    log.debug('starting the ``context_tab`` function')

    crossmatches = _crossmatch_info_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        transientCrossmatches=transientCrossmatches
    )

    crossmatches = khufu.grid_row(
        responsive=True,
        columns=crossmatches,
        htmlId=False,
        htmlClass=False
    )

    aladin = _aladin_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        transientCrossmatches=transientCrossmatches
    )

    aladin = khufu.grid_row(
        responsive=True,
        columns=aladin,
        htmlId=False,
        htmlClass=False
    )

    sherlockForm = _sherlock_development_form(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        transientCrossmatches=transientCrossmatches
    )

    context_block = """%(aladin)s %(crossmatches)s %(sherlockForm)s """ % locals(
    )
    # context_block = """%(host_stamp)s%(crossmatches)s""" % locals(
    # )

    footer = context_footer_bar(
        log,
        request=request
    )

    context_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=False,
        blockList=[context_block],
        tabFooter=footer,
        htmlId="contexttab"
    )

    log.debug('completed the ``context_tab`` function')
    return "%(context_tab)s" % locals()


def context_footer_bar(
        log,
        request):
    """get ticket footer bar

    **Key Arguments**

    - ``log`` -- logger
    - ``discoveryData`` -- the discoveryData for the object
    - ``lightcurveData`` -- the lightcurve data for the object


    **Return**

    - ``context_footer_bar`` -- the ticket footer bar for the pesssto object

    """
    lsqExists = False
    log.debug('starting the ``context_footer_bar`` function')
    ## VARIABLES ##

    footerColumn = khufu.grid_column(
        span=2,  # 1-12
        offset=0,  # 1-12
        content="<BR>" % locals(
        )
    )

    context_footer_bar = khufu.grid_row(
        responsive=True,
        columns=footerColumn,
        htmlId=False,
        htmlClass="ticketFooter"
    )

    return context_footer_bar


def _host_info_block(
        log,
        request,
        discoveryDataDictionary):
    """get ticket host info block

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.


    **Return**

    - ``host_info_block`` -- the ticket identity block for the pesssto object

    """
    log.debug('starting the ``host_info_block`` function')

    title = cu.block_title(
        log,
        title="host stamp"
    )

    masterName = discoveryDataDictionary["masterName"]
    sherlockClassification = discoveryDataDictionary["sherlockClassification"]

    nearestObjectUrl = ""
    exactLocationUrl = ""
    ogleStamp = ""
    ra = discoveryDataDictionary["raDeg"]
    dec = discoveryDataDictionary["decDeg"]
    transientBucketId = discoveryDataDictionary["transientBucketId"]
    if discoveryDataDictionary["sdss_coverage"] == 1:
        nearestObjectUrl = "http://skyserver.sdss3.org/public/en/tools/explore/obj.aspx?ra=%(ra)s&dec=%(dec)s" % locals(
        )
        exactLocationUrl = """http://skyserver.sdss3.org/public/en/tools/chart/image.aspx?ra=%(ra)s&dec=%(dec)s&scale=0.25&opt=GS&width=512&height=512""" % locals(
        )
        downloadContextStamp = "caches/transients/%s/sdss_stamp.jpeg" % (
            discoveryDataDictionary["transientBucketId"],)
        contextStamp = request.static_url(f'marshall_webapp:{downloadContextStamp}')
        stampName = "%(masterName)s_sdss_context_image" % locals()
    elif discoveryDataDictionary["ogle_color_context_stamp"] == 1:
        downloadContextStamp = "caches/transients/%(transientBucketId)s/ogle_color_context_stamp.png" % locals(
        )
        contextStamp = request.static_url(f'marshall_webapp:{downloadContextStamp}')
        ogleStamp = "OGLE context stamp"
        stampName = "%(masterName)s_ogle_context_image" % locals()
    elif discoveryDataDictionary["sdss_coverage"] == 0:
        contextStamp = 'holder.js/500x500/auto/industrial/text:not in sdss footprint'
        downloadContextStamp = contextStamp
        stampName = False
    else:
        contextStamp = 'holder.js/500x500/auto/industrial/text:sdss stamp not ready yet'
        downloadContextStamp = contextStamp
        stampName = False
    sdssUrl = """http://skyserver.sdss3.org/public/en/tools/chart/image.aspx?ra=%(ra)s&dec=%(dec)s&scale=0.25&opt=GSP&width=512&height=512&query=G""" % locals(
    )

    sdssLinkRow = ""
    if len(nearestObjectUrl):
        nearestObjectUrl = khufu.a(
            content='sdss nearest object',
            href=nearestObjectUrl,
            openInNewTab=True
        )
        nearestObjectUrl = khufu.coloredText(
            text=nearestObjectUrl,
            color="cyan",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )
        exactLocationUrl = khufu.a(
            content='exact sdss location',
            href=exactLocationUrl,
            openInNewTab=True
        )
        exactLocationUrl = khufu.coloredText(
            text=exactLocationUrl,
            color="blue",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )
        sdssLinkRow = khufu.grid_row(
            responsive=True,
            columns="&nbsp&nbsp&nbsp&nbsp%(ogleStamp)s%(exactLocationUrl)s<br>&nbsp&nbsp&nbsp&nbsp%(nearestObjectUrl)s" % locals(
            ),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

    if len(ogleStamp):
        ogleStamp = khufu.coloredText(
            text="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp%(ogleStamp)s" % locals(),
            color="blue"
        )

    sdssLink = khufu.a(
        content='sdss dr12 location',
        href=sdssUrl,
    )

    if stampName:
        href = request.route_path(
            'download', _query={'url': downloadContextStamp, "webapp": "marshall_webapp", "filename": stampName})
    else:
        href = False

    imageModal = khufu.imagingModal(
        log=log,
        imagePath=contextStamp,
        display="rounded",  # [ rounded | circle | polaroid | False ]
        modalHeaderContent="Context Stamp for %(masterName)s" % locals(),
        modalFooterContent=sdssLink,
        stampWidth=400,
        modalImageWidth=400,
        downloadLink=href)
    imageModal = imageModal.get()

    return "%(title)s %(imageModal)s %(sdssLinkRow)s" % locals()


def _crossmatch_info_block(
        log,
        request,
        discoveryDataDictionary,
        transientCrossmatches):
    """get ticket host info block

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.


    **Return**

    - ``_crossmatch_info_block`` -- the crossmatch info from sherlock for the pesssto object

    """
    log.debug('starting the ``_crossmatch_info_block`` function')

    title = cu.block_title(
        log,
        title="crossmatched sources"
    )

    # FIND THIS TRANSIENT'S CROSSMATCHES
    transientBucketId = discoveryDataDictionary["transientBucketId"]
    cms = []
    for row in transientCrossmatches:
        if row["transientBucketId"] == transientBucketId:
            cms.append(row)

    masterName = discoveryDataDictionary["masterName"]
    sherlockClassification = discoveryDataDictionary["sherlockClassification"]

    sourceIcons = {
        "galaxy": "spinner5",
        "agn": "target3",
        "qso": "target3",
        "star": "star3",
        "cv": "sun6",
        "cb": "sun6",
        "other": "help2",
        "unclear": "help2"
    }
    transColors = {
        "sn": "blue",
        "nt": "magenta",
        "cv": "green",
        "agn": "yellow",
        "variablestar": "orange",
        "vs": "orange",
        "bs": "brown",
        "?": "violet",
        "unclear": "violet",
        "kepler": "#dc322f"
    }

    table = ""
    if len(cms) > 0:

        hs = ["Rank", "Catalogue", "Catalogue ID", "Catalogue Type (& Subtype)", "Classification",
              "Angular Separation from Transient", "Physical Separation from Transient", "Transient Peak M", "Source Distance", "Source Redshift", "Source Mag"]
        tableHead = ""
        for h in hs:
            th = khufu.th(
                content=h,
                color=False
            )
            tableHead = """%(tableHead)s%(th)s""" % locals()
        # xkhufu-th
        tableHead = khufu.thead(
            trContent=tableHead
        )

        tableBody = []

        rs = ["rank", "catalogue_table_name", "catalogue_object_id",  "catalogue_object_type", "sherlockClassification",
              "separationArcsec", "physical_separation_kpc", "transientAbsMag", "distance", "z", "best_mag"]
        for c in cms:

            # generate object links
            if c["object_link"]:
                c["catalogue_object_id"] = khufu.a(
                    content=c["catalogue_object_id"],
                    href=c["object_link"],
                    openInNewTab=True
                )

            if c["catalogue_table_name"]:

                popover = khufu.popover(
                    tooltip=True,
                    placement="top",  # [ top | bottom | left | right ]
                    # [ False | click | hover | focus | manual ]
                    trigger="hover",
                    title=c["search_name"],
                    content=False,
                    delay=200
                )

                # add text color
                c["catalogue_table_name"] = khufu.a(
                    content=c["catalogue_table_name"],
                    href="#",
                    popover=popover
                )

            # SOURCE MAGNITUDE
            if c["best_mag"]:
                m = c["best_mag"]
                e = c["best_mag_error"]
                f = c["best_mag_filter"]
                if e:
                    e = " &plusmn; %(e)0.2f" % locals()
                else:
                    e = ""
                if isinstance(m, float):
                    c["best_mag"] = "%(f)s = %(m)0.2f%(e)s" % locals()
                else:
                    c["best_mag"] = m

            # CLASSIFICATION
            if c["classificationReliability"] == 1:
                cText = "transient is <em>synonymous</em> with this source"
                cLevel = "success"
            elif c["classificationReliability"] == 2:
                cText = "transient may be <em>associated</em> with this source"
                cLevel = "warning"
            else:
                cText = "<em>annotation</em> - not to be relied on for predicting transient classification"
                cLevel = "important"

            b = khufu.badge(
                text=c["classificationReliability"],
                level=cLevel
            )
            popover = khufu.popover(
                tooltip=False,
                placement="right",
                trigger="hover",
                title="<b>Classification Reliability</b>",
                content=cText,
                delay=200
            )
            b = khufu.a(
                content=b,
                href=False,
                popover=popover
            )

            # DISTANCE CURATION
            if c["z"]:
                c["distance_method"] = "spec-z distance"
                col = "success"
                zbadge = "s"
            elif c["photoZ"]:
                c["distance_method"] = "photo-z distance"
                col = "important"
                zbadge = "p"
            if c["direct_distance"]:
                col = "warning"
                c["distance"] = c["direct_distance"]
                c["distance_method"] = "redshift-independent distance"
                zbadge = "r"

            # REDSHIFT CURATION
            if not c["z"]:
                if c["photoZ"]:
                    pz = c["photoZ"]
                    if c["photoZErr"]:
                        pze = c["photoZErr"]
                        pz = "%(pz)0.3f &plusmn; %(pze)0.3f" % locals()
                    b = khufu.badge(
                        text='p',
                        level='important'
                    )
                    popover = khufu.popover(
                        tooltip=True,
                        placement="right",
                        trigger="hover",
                        title="photo-z",
                        content=False,
                        delay=200
                    )
                    b = khufu.a(
                        content=b,
                        href=False,
                        popover=popover
                    )
                    c["z"] = pz + b

            else:
                b = khufu.badge(
                    text='s',
                    level='success'
                )
                popover = khufu.popover(
                    tooltip=True,
                    placement="right",
                    trigger="hover",
                    title="spec-z",
                    content=False,
                    delay=200
                )
                b = khufu.a(
                    content=b,
                    href=False,
                    popover=popover
                )
                cz = c["z"]
                if isinstance(cz, float):
                    c["z"] = "%(cz)0.3f %(b)s" % locals()

            tableRow = []

            for r in rs:
                if c[r] == None:
                    c[r] = "-"
                if r == "catalogue_object_type":
                    try:
                        icon = sourceIcons[c[r]]
                    except:
                        icon = "help2"
                    if c["catalogue_object_type"].lower() == "other":
                        c["catalogue_object_type"] = c[
                            "catalogue_object_subtype"]
                    thisType = c[r]

                    if c["catalogue_object_subtype"]:
                        thisType += " (" + c["catalogue_object_subtype"] + ")"

                    # add text color
                    c[r] = """<i class="icon-%(icon)s" color="#268bd2"></i> %(thisType)s""" % locals()

                if isinstance(c[r], float):
                    this = c[r]
                    c[r] = """%(this)0.2f""" % locals()

                # ADD UNITS
                if c[r] != "-":
                    if r in ["original_search_radius_arcsec", "major_axis_arcsec"] and c[r] != "-":
                        c[r] = c[r] + '"'
                    if r in ["distance"]:

                        b = khufu.badge(
                            text=zbadge,
                            level=col
                        )
                        popover = khufu.popover(
                            tooltip=True,
                            # [ top | bottom | left | right ]
                            placement="right",
                            # [ False | click | hover | focus | manual ]
                            trigger="hover",
                            title=c["distance_method"],
                            content=False,
                            delay=200
                        )
                        b = khufu.a(
                            content=b,
                            href=False,
                            popover=popover
                        )

                        c[r] = c[r] + ' Mpc ' + b

                    if r in ["physical_separation_kpc"]:
                        c[r] = c[r] + ' Kpc'
                    if r in ["separationArcsec"]:
                        n = c["northSeparationArcsec"]
                        e = c["eastSeparationArcsec"]
                        c[r] = c[r] + '" (%(n)0.2fN, %(e)0.2fE)' % locals()

                content = khufu.coloredText(
                    text=c[r],
                    color=transColors[c["association_type"].lower()],
                    size=False,  # 1-10
                    pull=False,  # "left" | "right",
                    addBackgroundColor=False
                )
                td = khufu.td(
                    content=content,
                    color=False
                )
                tableRow.append(td)
            # xkhufu-table-cell
            tr = khufu.tr(
                cellContent=tableRow,
                color=transColors[c["association_type"].lower()]
            )
            tableBody.append(tr)

        tableBody = khufu.tbody(
            trContent=tableBody
        )
        table = khufu.table(
            caption=False,
            thead=tableHead,
            tbody=tableBody,
            striped=False,
            bordered=False,
            hover=True,
            condensed=True
        )

    return "%(table)s" % locals()


def _aladin_block(
        log,
        request,
        discoveryDataDictionary,
        transientCrossmatches):
    """get aladin lite instance for transient

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.


    **Return**

    - ``_aladin_block`` -- the crossmatch info from sherlock for the pesssto object

    """
    log.debug('starting the ``_aladin_block`` function')

    title = cu.block_title(
        log,
        title="crossmatch map"
    )

    # ADD TEXT COLOR
    masterName = discoveryDataDictionary["masterName"]
    text = khufu.coloredText(
        text="Contextual classification for <em>%(masterName)s</em>" % locals(
        ),
        color="grey",
        size=3,  # 1-10
        pull="right",  # "left" | "right",
        addBackgroundColor=False
    )

    masterClassification = discoveryDataDictionary["classification"]

    # ADD TEXT COLOR
    masterClassification = khufu.coloredText(
        text=masterClassification,
        color="violet",
        size=6,  # 1-10
        pull="right",  # "left" | "right",
        addBackgroundColor=False
    )
    masterClassification = masterClassification + "</br>" + text + "</br>"

    text = khufu.p(
        content='',
        lead=False,
        textAlign=False,  # [ left | center | right ]
        color=False,  # [ muted | warning | info | error | success ]
        navBar=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    coords = "%s %s" % (
        discoveryDataDictionary["raDeg"], discoveryDataDictionary["decDeg"],)

    name = discoveryDataDictionary["masterName"]

    # FIND THIS TRANSIENT'S CROSSMATCHES
    transientBucketId = discoveryDataDictionary["transientBucketId"]
    cms = []
    for row in transientCrossmatches:
        if row["transient_object_id"] == transientBucketId:
            cms.append(row)

    masterName = discoveryDataDictionary["masterName"]
    sherlockClassification = discoveryDataDictionary["sherlockClassification"]
    if discoveryDataDictionary["ps1_map"] == 1:
        survey = "P/PanSTARRS/DR1/color/z/zg/g"
    elif discoveryDataDictionary["sdss_coverage"] == 1:
        survey = "P/SDSS9/color"
    else:
        survey = "P/DSS2/color"

    aladin = '<div class="aladin-hide" coords="%(coords)s" survey="%(survey)s" data="/marshall/transients/%(transientBucketId)s/context" transient="%(name)s" style="font-family:dryx_icon_font"></div>' % locals(
    )

    return "%(masterClassification)s %(aladin)s" % locals()


def _sherlock_development_form(
        log,
        request,
        discoveryDataDictionary,
        transientCrossmatches):
    """*a form for adding comments and confirming/reporting incorrect matches from sherlock trasient classifier*

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.):

    """

    transientBucketId = discoveryDataDictionary["transientBucketId"]

    if discoveryDataDictionary["mismatchComment"]:
        # add text color
        commentDate = discoveryDataDictionary["commentDate"]
        if commentDate:
            commentDate = commentDate.strftime("%Y-%m-%d")
        else:
            commentDate = "no comment date"
        if not discoveryDataDictionary["user"]:
            discoveryDataDictionary["user"] = "anon"
        text = khufu.coloredText(
            text="Mismatch reported by " + discoveryDataDictionary["user"].replace(".", " ").title(
            ) + ", " + commentDate + ": ",
            color="red",
            size=4,  # 1-10
            pull=False,  # "left" | "right",
            addBackgroundColor=False
        )

        currentComment = khufu.coloredText(
            text=text + discoveryDataDictionary["mismatchComment"],
            color="grey",
            size=3,  # 1-10
            pull=False,  # "left" | "right",
            addBackgroundColor=False
        )
    else:
        currentComment = ""

    if len(currentComment) == 0:

        button = khufu.button(
            buttonText='mismatch',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='success',
            buttonSize='default',  # [ large | default | small | mini ]
            htmlId=False,
            href=False,
            pull=False,  # right, left, center
            submit=True,
            block=False,
            disable=False,
            postInBackground=False,
            dataToggle=False,  # [ modal ]
            popover=False
        )

        correctMatchInput = khufu.formInput(
            # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
            ttype='text',
            placeholder='comment ...',
            span=10,
            htmlId="sherlockMatchComment",
            searchBar=False,
            pull=False,
            prepend=False,
            append=False,
            prependDropdown=False,
            appendDropdown=False,
            inlineHelpText=False,
            blockHelpText=False,
            focusedInputText=False,
            required=True,
            disabled=False
        )
        correctMatchInput = khufu.controlRow(
            inputList=[correctMatchInput, button]
        )
        correctMatchLabel = khufu.horizontalFormControlLabel(
            labelText='If you think the first ranked transient-host match is obviously incorrect please report the mismatch to help improve the contextual classifier',
            forId="sherlockMatchComment"
        )

        correctMatchCG = khufu.horizontalFormControlGroup(
            content=correctMatchLabel + correctMatchInput,
            validationLevel=False
        )
        # xkhufu-tmpx-form-control-groue

        sherlockForm = khufu.form(
            content=correctMatchCG,  # list of control groups
            # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            formType='inline',
            navBarPull=False,  # [ false | right | left ],
            postToScript="/marshall/transients/%(transientBucketId)s/context" % locals(),
            htmlId="sherlockDevelopment",
            postInBackground=False,
            htmlClass=False,
            redirectUrl="/marshall/transients/%(transientBucketId)s" % locals(),
            span=10,
            offset=1
        )

        currentComment = khufu.grid_column(
            span=6,  # 1-12
            offset=1,  # 1-12
            content=currentComment,
            pull=False,  # ["right", "left", "center"]
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
    else:
        sherlockForm = ""

        currentComment = khufu.grid_column(
            span=6,  # 1-12
            offset=0,  # 1-12
            content=currentComment,
            pull=False,  # ["right", "left", "center"]
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

    return currentComment + sherlockForm

    # xt-class-method
