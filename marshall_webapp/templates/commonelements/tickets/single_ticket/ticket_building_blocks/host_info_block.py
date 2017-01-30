#!/usr/local/bin/python
# encoding: utf-8
"""
host_info_block.py
=================
:Summary:
    The host info block for the object ticket

:Author:
    David Young

:Date Created:
    November 20, 2013

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import datetime
from docopt import docopt
import numpy as np
import khufu
import collections
from dryxPython import commonutils as dcu
from .....commonelements import commonutils as cu


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : November 20, 2013
# CREATED : November 20, 2013
# AUTHOR : DRYX


def host_info_block(
        log,
        request,
        discoveryDataDictionary,
        transientCrossmatches):
    """get ticket host info block

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
        - ``transientCrossmatches`` -- info from the transient crossmatcher

    **Return:**
        - ``host_info_block`` -- the ticket identity block for the pesssto object

    """
    log.info('starting the ``host_info_block`` function')

    title = cu.block_title(
        log,
        title="host info"
    )

    transientBucketId = discoveryDataDictionary["transientBucketId"]
    masterName = discoveryDataDictionary["masterName"]
    sherlockClassification = discoveryDataDictionary["sherlockClassification"]

    cm = ""
    for row in transientCrossmatches:
        if row["transient_object_id"] == transientBucketId and row["rank"] == 1:
            cm = row
            cmName = row["catalogue_object_id"]
            cmType = row["catalogue_object_type"]
            cmZ = row["z"]
            cmCat = row["catalogue_table_name"]
            cmSep = row["separation"]
            cmPhySep = row["physical_separation_kpc"]

    if len(cm):
        littleTitle = cu.little_label(
            text="most likely crossmatch:"
        )

        object_link = None
        if "ned" in cmCat:
            object_link = "https://ned.ipac.caltech.edu/cgi-bin/objsearch?objname=%(cmName)s&extend=no&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=RA+or+Longitude&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES" % locals()
        elif "sdss" in cmCat:
            object_link = "http://skyserver.sdss.org/dr12/en/tools/explore/Summary.aspx?id=%(cmName)s" % locals(
            )
        elif "milliquas" in cmCat:
            object_link = "https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3query.pl?bparam_name=%(cmName)s&navtrail=%%3Ca+class%%3D%%27navpast%%27+href%%3D%%27https%%3A%%2F%%2Fheasarc.gsfc.nasa.gov%%2FW3Browse%%2Fall%%2Fmilliquas.html%%27%%3E+Choose+Tables%%3C%%2Fa%%3E+%%3E+%%3Ca+class%%3D%%27navpast%%27+href%%3D%%27%%2Fcgi-bin%%2FW3Browse%%2Fw3table.pl%%3FREAL_REMOTE_HOST%%3D143.117.37.81%%26tablehead%%3Dname%%253Dmilliquas%%26Action%%3DMore%%2BOptions%%26REAL_REMOTE_HOST%%3D143%%252E117%%252E37%%252E81%%26Equinox%%3D2000%%26Action%%3DMore%%2BOptions%%26sortby%%3Dpriority%%26ResultMax%%3D1000%%26maxpriority%%3D99%%26Coordinates%%3DEquatorial%%26tablehead%%3Dname%%253Dmilliquas%%26Action%%3DParameter%%2BSearch%%27%%3EParameter+Search%%3C%%2Fa%%3E&popupFrom=Query+Results&tablehead=name%%3Dheasarc_milliquas%%26description%%3DMillion+Quasars+Catalog+%%28MILLIQUAS%%29%%2C+Version+4.5+%%2810+May+2015%%29%%26url%%3Dhttp%%3A%%2F%%2Fheasarc.gsfc.nasa.gov%%2FW3Browse%%2Fgalaxy-catalog%%2Fmilliquas.html%%26archive%%3DN%%26radius%%3D1%%26mission%%3DGALAXY+CATALOG%%26priority%%3D5%%26tabletype%%3DObject&dummy=Examples+of+query+constraints%%3A&varon=name&bparam_name%%3A%%3Aunit=+&bparam_name%%3A%%3Aformat=char25&varon=ra&bparam_ra=&bparam_ra%%3A%%3Aunit=degree&bparam_ra%%3A%%3Aformat=float8%%3A.5f&varon=dec&bparam_dec=&bparam_dec%%3A%%3Aunit=degree&bparam_dec%%3A%%3Aformat=float8%%3A.5f&varon=bmag&bparam_bmag=&bparam_bmag%%3A%%3Aunit=mag&bparam_bmag%%3A%%3Aformat=float8%%3A4.1f&varon=rmag&bparam_rmag=&bparam_rmag%%3A%%3Aunit=mag&bparam_rmag%%3A%%3Aformat=float8%%3A4.1f&varon=redshift&bparam_redshift=&bparam_redshift%%3A%%3Aunit=+&bparam_redshift%%3A%%3Aformat=float8%%3A6.3f&varon=radio_name&bparam_radio_name=&bparam_radio_name%%3A%%3Aunit=+&bparam_radio_name%%3A%%3Aformat=char22&varon=xray_name&bparam_xray_name=&bparam_xray_name%%3A%%3Aunit=+&bparam_xray_name%%3A%%3Aformat=char22&bparam_lii=&bparam_lii%%3A%%3Aunit=degree&bparam_lii%%3A%%3Aformat=float8%%3A.5f&bparam_bii=&bparam_bii%%3A%%3Aunit=degree&bparam_bii%%3A%%3Aformat=float8%%3A.5f&bparam_broad_type=&bparam_broad_type%%3A%%3Aunit=+&bparam_broad_type%%3A%%3Aformat=char4&bparam_optical_flag=&bparam_optical_flag%%3A%%3Aunit=+&bparam_optical_flag%%3A%%3Aformat=char3&bparam_red_psf_flag=&bparam_red_psf_flag%%3A%%3Aunit=+&bparam_red_psf_flag%%3A%%3Aformat=char1&bparam_blue_psf_flag=&bparam_blue_psf_flag%%3A%%3Aunit=+&bparam_blue_psf_flag%%3A%%3Aformat=char1&bparam_ref_name=&bparam_ref_name%%3A%%3Aunit=+&bparam_ref_name%%3A%%3Aformat=char6&bparam_ref_redshift=&bparam_ref_redshift%%3A%%3Aunit=+&bparam_ref_redshift%%3A%%3Aformat=char6&bparam_qso_prob=&bparam_qso_prob%%3A%%3Aunit=percent&bparam_qso_prob%%3A%%3Aformat=int2%%3A3d&bparam_alt_name_1=&bparam_alt_name_1%%3A%%3Aunit=+&bparam_alt_name_1%%3A%%3Aformat=char22&bparam_alt_name_2=&bparam_alt_name_2%%3A%%3Aunit=+&bparam_alt_name_2%%3A%%3Aformat=char22&Entry=&Coordinates=J2000&Radius=Default&Radius_unit=arcsec&NR=CheckCaches%%2FGRB%%2FSIMBAD%%2FNED&Time=&ResultMax=10&displaymode=Display&Action=Start+Search&table=heasarc_milliquas" % locals()
        elif ("ps1" not in cmCat) and ("ritter" not in cmCat) and ("down" not in cmCat) and ("guide_star" not in cmCat) and ("kepler" not in cmCat):
            object_link = "http://simbad.u-strasbg.fr/simbad/sim-id?Ident=%(cmName)s&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit+id" % locals(
            )

        if object_link:
            cmName = khufu.a(
                content=cmName,
                href=object_link,
                openInNewTab=True
            )

        # add text color
        cmName = khufu.coloredText(
            text=cmName,
            color="orange"
        )

        cmCat = cmCat.replace("tcs_cat_", " ").replace("_stream", " ")
        if cmCat[0] in ["a", "e", "i", "o", "u"]:
            cmCat = "an %(cmCat)s" % locals()
        else:
            cmCat = "a %(cmCat)s" % locals()

        if cmPhySep:
            try:
                cmPhySep = float(cmPhySep)
                cmPhySep = " (%(cmPhySep)0.2f Kpc) " % locals()
            except:
                cmPhySep = "" % locals()
        else:
            cmPhySep = "" % locals()

        if cmZ:
            try:
                cmZ = float(cmZ)
                cmZ = "at z = %(cmZ)0.3f " % locals()
            except:
                cmZ = ""
        else:
            cmZ = ""

        if cmSep:
            try:
                cmSep = float(cmSep)
                cmSep = "%(cmSep)0.2f" % locals()
            except:
                cmSep = ""
        else:
            cmSep = ""

        cmType = khufu.coloredText(
            text="%(cmCat)s %(cmType)s %(cmZ)sseparated %(cmSep)s\"%(cmPhySep)s from the transient" % locals(),
            color="yellow",
            size=2,
        )

        cm = khufu.grid_row(
            responsive=True,
            columns="%(littleTitle)s %(cmName)s" % locals(),
        )

        cm = khufu.grid_row(
            responsive=True,
            columns="%(cm)s &nbsp&nbsp&nbsp %(cmType)s" % locals(),
        )

    nearestObjectUrl = ""
    exactLocationUrl = ""
    ogleStamp = ""
    ra = discoveryDataDictionary["raDeg"]
    dec = discoveryDataDictionary["decDeg"]

    contextMaps = {}

    contextMaps = collections.OrderedDict(sorted(contextMaps.items()))

    if discoveryDataDictionary["sdss_coverage"] == 1:
        nearestObjectUrl = "http://skyserver.sdss3.org/public/en/tools/explore/obj.aspx?ra=%(ra)s&dec=%(dec)s" % locals(
        )
        exactLocationUrl = """http://skyserver.sdss3.org/public/en/tools/chart/image.aspx?ra=%(ra)s&dec=%(dec)s&scale=0.25&opt=GS&width=512&height=512""" % locals(
        )

    if discoveryDataDictionary["ps1_map"] == 1:
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%s/ps1_map_color.jpeg" % (
            discoveryDataDictionary["transientBucketId"],))
        contextStamp = downloadContextStamp
        contextMaps["PS1"] = contextStamp
        stampName = "%(masterName)s_ps1_context_image" % locals()
    if discoveryDataDictionary["sdss_coverage"] == 1:
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%s/sdss_stamp.jpeg" % (
            discoveryDataDictionary["transientBucketId"],))
        contextStamp = downloadContextStamp
        contextMaps["SDSS DR12"] = contextStamp
        stampName = "%(masterName)s_sdss_context_image" % locals()
    if discoveryDataDictionary["ogle_color_context_stamp"] == 1:
        downloadContextStamp = request.static_path("marshall_webapp:static/caches/transients/%(transientBucketId)s/ogle_color_context_stamp.png" % locals(
        ))
        contextStamp = downloadContextStamp
        contextMaps["OGLE"] = contextStamp
        ogleStamp = "OGLE context stamp"
        ogleStamp = khufu.coloredText(
            text="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp%(ogleStamp)s" % locals(),
            color="blue"
        )
        stampName = "%(masterName)s_ogle_context_image" % locals()

    if len(contextMaps) == 0:
        downloadContextStamp = 'holder.js/500x500/auto/industrial/text:no context stamp'
        contextStamp = downloadContextStamp
        contextMaps["PLACEHOLDER"] = contextStamp
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

    sdssLink = khufu.a(
        content='sdss dr12 location',
        href=sdssUrl,
    )

    if len(contextMaps) > 0:
        for k, v in contextMaps.iteritems():
            stampName = "%(masterName)s_%(k)s_context_image" % locals()
            stampName = stampName.lower()
            contextStamp = v
            break
        noModal = False

        href = request.route_path(
            'download', _query={'url': downloadContextStamp, "webapp": "marshall_webapp", "filename": stampName})
    else:
        href = False
        contextStamp = contextMaps["PLACEHOLDER"]
        noModal = True

    allImage = ""
    count = 0
    for k, v in contextMaps.iteritems():
        count += 1
        reminderImages = len(contextMaps) % 3
        if reminderImages == 0:
            span = 4
            offset = 0
        elif count < (len(contextMaps) - reminderImages):
            span = 4
            offset = 0
        elif reminderImages == 2:
            span = 6
            offset = 0
        else:
            span = 6
            offset = 3

        thisImage = khufu.image(
            src=v,  # [ industrial | gray | social ]
            href=False,
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
            text=k,
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
        modalHeaderContent="Context Maps for %(masterName)s" % locals(
        ),
        modalBodyContent=grid_row,
        modalFooterContent="",
        htmlId="hookId%(randNum)s" % locals(),
        centerContent=True
    )
    imageModal = khufu.image(
        src=contextStamp,  # [ industrial | gray | social ]
        href="#hookId%(randNum)s" % locals(),
        display="rounded",  # [ rounded | circle | polaroid | False ]
        pull=False,  # [ "left" | "right" | "center" | False ]
        htmlClass=False,
        width="100%",
        modal=True
    )
    if noModal == False:
        imageModal = imageModal + modal

    # imageModal = khufu.imagingModal(
    #     log=log,
    #     imagePath=contextStamp,
    #     display="rounded",  # [ rounded | circle | polaroid | False ]
    #     modalHeaderContent="Context Stamp for %(masterName)s" % locals(),
    #     modalFooterContent=sdssLink,
    #     stampWidth="100%",
    #     modalImageWidth=400,
    #     downloadLink=href)
    # imageModal = imageModal.get()

    if sherlockClassification:
        littleTitle = cu.little_label(
            text="contextual classification:"
        )

        sherlockClassification = khufu.coloredText(
            text=sherlockClassification,
            color="violet",
            size=6,  # 1-10
        )

        sherlockClassification = khufu.grid_row(
            responsive=True,
            columns="%(littleTitle)s %(sherlockClassification)s" % locals(),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
    else:
        sherlockClassification = ""

    return "%(title)s %(imageModal)s %(sdssLinkRow)s %(sherlockClassification)s %(cm)s" % locals()


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
