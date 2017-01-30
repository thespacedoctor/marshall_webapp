#!/usr/local/bin/python
# encoding: utf-8
"""
context.py
=============
:Summary:
    The context tab for the PESSTO Object tickets

:Author:
    David Young

:Date Created:
    January 7, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import datetime
import re
from docopt import docopt
from dryxPython import commonutils as dcu
import khufu
import dryxPython.astrotools as dat
from .. import ticket_building_blocks
from .....commonelements import commonutils as cu

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 7, 2014
# CREATED : January 7, 2014
# AUTHOR : DRYX


def context_tab(
        log,
        request,
        discoveryDataDictionary,
        objectAkas,
        atelData,
        lightcurveData,
        transientCrossmatches):
    """context tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectAkas`` -- object akas
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage
        - ``transientCrossmatches`` -- catalogue crossmatches (from sherlock)

    **Return:**
        - ``context_tab`` -- the lightcurve/context tab for a single ticket on the transient listings page

    **Todo**
    """
    from ... import single_ticket

    log.info('starting the ``context_tab`` function')

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

    context_block = """%(aladin)s %(crossmatches)s""" % locals(
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

    log.info('completed the ``context_tab`` function')
    return "%(context_tab)s" % locals()


# LAST MODIFIED : November 20, 2013
# CREATED : November 20, 2013
# AUTHOR : DRYX

def context_footer_bar(
        log,
        request):
    """get ticket footer bar

    **Key Arguments:**
        - ``log`` -- logger
        - ``discoveryData`` -- the discoveryData for the object
        - ``lightcurveData`` -- the lightcurve data for the object

    **Return:**
        - ``context_footer_bar`` -- the ticket footer bar for the pesssto object

    **Todo**
    """
    lsqExists = False
    log.info('starting the ``context_footer_bar`` function')
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

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.

    **Return:**
        - ``host_info_block`` -- the ticket identity block for the pesssto object

    """
    log.info('starting the ``host_info_block`` function')

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
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%s/sdss_stamp.jpeg" % (
            discoveryDataDictionary["transientBucketId"],))
        contextStamp = request.static_path(
            "marshall_webapp:static/caches/transients/%s/sdss_stamp.jpeg" % (
                discoveryDataDictionary["transientBucketId"],))
        stampName = "%(masterName)s_sdss_context_image" % locals()
    elif discoveryDataDictionary["ogle_color_context_stamp"] == 1:
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%(transientBucketId)s/ogle_color_context_stamp.png" % locals(
        ))
        contextStamp = request.static_path(
            "marshall_webapp:static/caches/transients/%(transientBucketId)s/ogle_color_context_stamp.png" % locals(
            ))
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

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.

    **Return:**
        - ``_crossmatch_info_block`` -- the crossmatch info from sherlock for the pesssto object

    """
    log.info('starting the ``_crossmatch_info_block`` function')

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
        "other": "help2"
    }
    transColors = {
        "sn": "blue",
        "nt": "magenta",
        "cv": "green",
        "agn": "yellow",
        "variablestar": "orange",
        "?": "violet",
        "kepler": "#dc322f"
    }

    table = ""
    if len(cms) > 0:

        hs = ["Rank", "Classifcation", "Association", "Type", "Catalogue",
              "Angular Separation", "Physical Separation", "Radius (if Galaxy)", "Distance", "Redshift", "Original Search Radius"]
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

        rs = ["rank", "association_type", "catalogue_object_id", "catalogue_object_type", "catalogue_table_name",
              "separationArcsec", "physical_separation_kpc", "major_axis_arcsec", "distance", "z", "original_search_radius_arcsec"]
        for c in cms:

            # generate object links
            if c["object_link"]:
                c["catalogue_object_id"] = khufu.a(
                    content=c["catalogue_object_id"],
                    href=c["object_link"],
                    openInNewTab=True
                )

            if c["catalogue_table_name"]:
                c["catalogue_table_name"] = c[
                    "catalogue_table_name"].replace("tcs_cat_", "").replace("_", " ")
                regex = re.compile(r'(v\d{1,3}) (\d{1,3})( (\d{1,3}))?')
                c["catalogue_table_name"] = regex.sub(
                    "\g<1>.\g<2>", c["catalogue_table_name"])

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

            if c["direct_distance"]:
                c["distance"] = c["direct_distance"]
            tableRow = []

            for r in rs:
                if c[r] == None:
                    c[r] = "-"
                if r == "catalogue_object_type":
                    icon = sourceIcons[c[r]]
                    if c["catalogue_object_type"].lower() == "other":
                        c["catalogue_object_type"] = c[
                            "catalogue_object_subtype"]
                    thisType = c[r]
                    # add text color
                    c[
                        r] = """<i class="icon-%(icon)s" color="#268bd2"></i> %(thisType)s""" % locals()

                if isinstance(c[r], float):
                    this = c[r]
                    c[r] = """%(this)0.2f""" % locals()

                # ADD UNITS
                if c[r] != "-":
                    if r in ["separationArcsec", "original_search_radius_arcsec", "major_axis_arcsec"] and c[r] != "-":
                        c[r] = c[r] + '"'
                    if r in ["distance"]:
                        c[r] = c[r] + ' Mpc'
                    if r in ["physical_separation_kpc"]:
                        c[r] = c[r] + ' Kpc'

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

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.

    **Return:**
        - ``_aladin_block`` -- the crossmatch info from sherlock for the pesssto object

    """
    log.info('starting the ``_aladin_block`` function')

    title = cu.block_title(
        log,
        title="crossmatch map"
    )

    # add text color
    masterName = discoveryDataDictionary["masterName"]
    text = khufu.coloredText(
        text="Contextual classification for <em>%(masterName)s</em>" % locals(
        ),
        color="grey",
        size=3,  # 1-10
        pull="right",  # "left" | "right",
        addBackgroundColor=False
    )

    masterClassification = discoveryDataDictionary["sherlockClassification"]

    # add text color
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
    if discoveryDataDictionary["sdss_coverage"] == 1:
        survey = "P/SDSS9/color"
    else:
        survey = "P/DSS2/color"

    aladin = '<div class="aladin-hide" coords="%(coords)s" survey="%(survey)s" data="/marshall/transients/%(transientBucketId)s/context" transient="%(name)s" style="font-family:dryx_icon_font"></div>' % locals(
    )

    return "%(masterClassification)s %(aladin)s" % locals()

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
