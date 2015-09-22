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
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

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
import dryxPython.mysql as dms
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

    host = _host_info_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary
    )

    host_stamp = khufu.grid_column(
        span=4,  # 1-12
        offset=0,  # 1-12
        content=host,
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    crossmatches = _crossmatch_info_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        transientCrossmatches=transientCrossmatches
    )

    crossmatches = khufu.grid_column(
        span=8,  # 1-12
        offset=0,  # 1-12
        content=crossmatches,
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    context_block = """%(host_stamp)s%(crossmatches)s""" % locals(
    )

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
        display="polaroid",  # [ rounded | circle | polaroid | False ]
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
        if row["transient_object_id"] == transientBucketId:
            cms.append(row)

    masterName = discoveryDataDictionary["masterName"]
    sherlockClassification = discoveryDataDictionary["sherlockClassification"]

    table = ""
    if len(cms) > 0:

        hs = ["Rank", "Classifcation", "Association", "Type", "Catalogue",
              "Angular Separation", "Physical Separation", "Radius (if Galaxy)", "Distance", "Redshift"]
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
              "separation", "physical_separation_kpc", "major_axis_arcsec", "distance", "z"]
        for c in cms:

            if c["direct_distance"]:
                c["distance"] = c["direct_distance"]
            tableRow = []

            for r in rs:
                if c[r] == None:
                    c[r] = "-"
                if isinstance(c[r], float):
                    this = c[r]
                    c[r] = """%(this)0.3f""" % locals()
                td = khufu.td(
                    content=c[r],
                    color=False
                )
                tableRow.append(td)
            # xkhufu-table-cell
            tr = khufu.tr(
                cellContent=tableRow,
                color=False
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

    return "%(title)s %(table)s" % locals()

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
