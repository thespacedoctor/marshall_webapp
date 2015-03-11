#!/usr/local/bin/python
# encoding: utf-8
"""
overview.py
===========
:Summary:
    The overview tab for the PESSTO Object tickets

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
from docopt import docopt
from dryxPython import commonutils as dcu

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 7, 2014
# CREATED : January 7, 2014
# AUTHOR : DRYX


def overview_tab(
        log,
        request,
        discoveryDataDictionary,
        objectComments,
        objectAkas,
        atelData,
        lightcurveData,
        objectHistories,
        headerAndFooter=True):
    """overview tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectComments`` -- the comments for the object
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage
        - ``objectHistories`` -- the object histories
        - ``headerAndFooter`` -- do you want to display the header and footer?

    **Return:**
        - ``overview_tab`` -- the transient overview info tab for the single ticket displayed on the transient listing pages

    **Todo**
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import datetime
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu
    import dryxPython.mysql as dms
    from .. import ticket_building_blocks
    from ... import single_ticket

    log.info('starting the ``overview_tab`` function')
    # TEST THE ARGUMENTS

    ## VARIABLES ##
    identity_block = ticket_building_blocks.identity_block.identity_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas
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

    actions_block = ticket_building_blocks.actions_block.actions_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        lightcurveData=lightcurveData,
        objectAkas=objectAkas
    )

    if headerAndFooter is False:
        overview_tab_header = False
        overview_tab_footer = False
    else:
        overview_tab_header = ticket_building_blocks.ticket_header_bar.ticket_header_bar(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
            objectComments=objectComments,
            atelData=atelData,
            lightcurveData=lightcurveData,
            objectHistories=objectHistories)
        overview_tab_footer = ticket_building_blocks.ticket_footer_bar.ticket_footer_bar(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
            atelData=atelData
        )

    overview_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=overview_tab_header,
        blockList=[identity_block, object_info_block,
                   classification_block, host_info_block, lightcurve_block, ],
        tabFooter=overview_tab_footer,
        actionsBlock=actions_block
    )

    log.info('completed the ``overview_tab`` function')
    return overview_tab

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
