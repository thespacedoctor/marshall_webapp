#!/usr/local/bin/python
# encoding: utf-8
"""
comments.py
===========
:Summary:
    The comments tab for the PESSTO Object tickets

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
from docopt import docopt
import khufu
from dryxPython import commonutils as dcu
import dryxPython.mysql as dms


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 7, 2014
# CREATED : January 7, 2014
# AUTHOR : DRYX


def comments_tab(
        log,
        request,
        discoveryDataDictionary,
        objectComments,
        objectAkas,
        atelData,
        lightcurveData):
    """comments tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectComments`` -- the comments for the object
        - ``objectAkas`` -- object akas
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage
        - ``thisUrl`` -- current url

    **Return:**
        - ``comments_tab`` -- for each transient ticket in the transient listings pages

    **Todo**
    """
    ################ > IMPORTS ################
    from .. import ticket_building_blocks
    from .. import tabs
    from ... import single_ticket
    from .....commonelements import forms

    log.info('starting the ``comments_tab`` function')

    comments_block = ticket_building_blocks.comments_block.comments_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectComments=objectComments
    )

    newCommentForm = forms.add_new_comment_to_object_form.add_new_comment_to_object_form(
        log=log,
        request=request,
        transientBucketId=discoveryDataDictionary["transientBucketId"]
    )

    # EXTRA OVERVIEW INFO
    ## VARIABLES ##
    identity_block = ticket_building_blocks.identity_block.identity_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas,
    )

    object_info_block = ticket_building_blocks.object_info_block.object_info_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )

    host_info_block = ticket_building_blocks.host_info_block.host_info_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )

    lightcurve_block = ticket_building_blocks.lightcurve_block.lightcurve_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        lightcurveData=lightcurveData,
        objectAkas=objectAkas
    )

    classification_block = ticket_building_blocks.classification_block.classification_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
    )

    if classification_block:
        theseBlocks = [identity_block, object_info_block, classification_block,
                       host_info_block, lightcurve_block]
    else:
        theseBlocks = [identity_block, object_info_block,
                       host_info_block, lightcurve_block]

    thisRow = ""
    blockCount = len(theseBlocks)
    span = int(round(12. / (len(theseBlocks)) - 0.5))
    remainingSpans = 12 - span * len(theseBlocks)
    count = 1
    for block in theseBlocks:
        thisSpan = span
        if count <= remainingSpans:
            thisSpan = span + 1
        count += 1
        block = khufu.grid_column(
            span=thisSpan,  # 1-12
            offset=0,  # 1-12
            content=block
        )
        thisRow = """%(thisRow)s %(block)s""" % locals()

    overviewWell = khufu.grid_row(
        responsive=True,
        columns=thisRow
    )

    overviewWell = khufu.well(
        wellText=overviewWell,
        wellSize='default',  # [ "default" | "large" | "small" ]
        htmlClass="overviewWell"
    )

    # convert bytes to unicode
    if isinstance(comments_block, str):
        comments_block = unicode(
            comments_block, encoding="utf-8", errors="replace")
    # convert bytes to unicode
    if isinstance(overviewWell, str):
        overviewWell = unicode(overviewWell, encoding="utf-8", errors="replace")

    comments_block = u"""%(newCommentForm)s %(overviewWell)s %(comments_block)s""" % locals(
    )

    comments_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=False,
        blockList=[comments_block],
        tabFooter=False,
        htmlId="commentstab"
    )

    # convert bytes to unicode
    if isinstance(comments_tab, str):
        comments_tab = unicode(comments_tab, encoding="utf-8", errors="replace")

    log.info('completed the ``comments_tab`` function')
    return "%(comments_tab)s" % locals()


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
