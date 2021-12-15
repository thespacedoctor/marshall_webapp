#!/usr/local/bin/python
# encoding: utf-8
"""
*The comments tab for the PESSTO Object tickets*

:Author:
    David Young
"""
import sys
import os
import datetime
import khufu

def comments_tab(
        log,
        request,
        discoveryDataDictionary,
        objectComments,
        objectAkas,
        atelData,
        lightcurveData,
        transientCrossmatches):
    """comments tab

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
    - ``objectComments`` -- the comments for the object
    - ``objectAkas`` -- object akas
    - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
    - ``atelData`` -- the atel matches for the objects displayed on the webpage
    - ``transientCrossmatches`` -- info from the transient crossmatcher
    

    **Return**

    - ``comments_tab`` -- for each transient ticket in the transient listings pages
    
    """
    from marshall_webapp.templates.commonelements.tickets.single_ticket import ticket_building_blocks, tabs
    from marshall_webapp.templates.commonelements.tickets import single_ticket
    from marshall_webapp.templates.commonelements import forms

    log.debug('starting the ``comments_tab`` function')

    commentCount, comments_block = ticket_building_blocks.comments_block.comments_block(
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
        transientCrossmatches=transientCrossmatches
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

    log.debug('completed the ``comments_tab`` function')
    return commentCount, "%(comments_tab)s" % locals()
