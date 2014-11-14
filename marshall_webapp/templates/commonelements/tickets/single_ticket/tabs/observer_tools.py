#!/usr/local/bin/python
# encoding: utf-8
"""
observer tools.py
===========
:Summary:
    The observer tools tab for the PESSTO Object tickets

:Author:
    David Young

:Date Created:
    March 7, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import commonutils as dcu

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : March 7, 2014
# CREATED : March 7, 2014
# AUTHOR : DRYX


def observer_tools_tab_header(
        log,
        request,
        discoveryDataDictionary,
        objectComments,
        objectAkas,
        atelData,
        lightcurveData,
        headerAndFooter=True):
    """observer tools tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectComments`` -- the comments for the object
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage
        - ``headerAndFooter`` -- do you want to display the header and footer?

    **Return:**
        - ``observer_tools_tab``

    **Todo**
        - @review: when complete, clean observer_tools_tab function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
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

    log.info('starting the ``observer_tools_tab`` function')
    # TEST THE ARGUMENTS

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

    actions_block = ticket_building_blocks.actions_block.actions_block(
        log=log,
        request=request,
        discoveryDataDictionary=discoveryDataDictionary,
        objectAkas=objectAkas
    )

    if headerAndFooter is False:
        observer_tools_tab_header = False
        observer_tools_tab_footer = False
    else:
        observer_tools_tab_header = ticket_building_blocks.ticket_header_bar.ticket_header_bar(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
            objectComments=objectComments,
            lightcurveData=lightcurveData,
            atelData=atelData)
        observer_tools_tab_footer = ticket_building_blocks.ticket_footer_bar.ticket_footer_bar(
            log=log,
            request=request,
            discoveryDataDictionary=discoveryDataDictionary,
            atelData=atelData,
        )

    observer_tools_tab = single_ticket._ticket_tab_template(
        log=log,
        request=request,
        tabHeader=observer_tools_tab_header,
        blockList=[identity_block, object_info_block,
                   classification_block, host_info_block, lightcurve_block, ],
        tabFooter=observer_tools_tab_footer,
        actionsBlock=actions_block,
    )

    log.info('completed the ``observer_tools_tab`` function')
    return observer_tools_tab

# use the tab-trigger below for new function
# x-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

############################################
# CODE TO BE DEPECIATED                    #
############################################

if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
