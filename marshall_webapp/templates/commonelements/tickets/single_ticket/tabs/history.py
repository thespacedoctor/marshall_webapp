#!/usr/local/bin/python
# encoding: utf-8
"""
history.py
===========
:Summary:
    The history tab for the PESSTO Object tickets

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


def history_tab(
        log,
        request,
        discoveryDataDictionary,
        objectComments,
        objectAkas,
        atelData,
        lightcurveData):
    """history tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectComments`` -- the history for the object
        - ``objectAkas`` -- object akas
        - ``lightcurveData`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage
        - ``thisUrl`` -- current url

    **Return:**
        - ``history_tab`` -- for each transient ticket in the transient listings pages

    **Todo**
    """
    ################ > IMPORTS ################
    from .. import ticket_building_blocks
    from .. import tabs
    from ... import single_ticket
    from .....commonelements import forms

    log.info('starting the ``history_tab`` function')

    history_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=False,
        blockList=["nice"],
        tabFooter=False,
        htmlId="historytab"
    )

    # convert bytes to unicode
    if isinstance(history_tab, str):
        history_tab = unicode(history_tab, encoding="utf-8", errors="replace")

    log.info('completed the ``history_tab`` function')
    return history_tab


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
