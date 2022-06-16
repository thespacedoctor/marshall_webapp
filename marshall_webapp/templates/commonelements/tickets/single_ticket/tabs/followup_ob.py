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

def followup_ob(
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
    
    log.debug('completed the ``comments_tab`` function')
    return "Hello World"
