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
import re
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
        objectAkas,
        atelData,
        objectHistories):
    """history tab

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- the unique discoveryData dictionary of the object in the pessto marshall database (from view_object_contextual_data)
        - ``objectAkas`` -- object akas
        - ``objectHistories`` -- the lightcurve data for the objects displayed on the webpage
        - ``atelData`` -- the atel matches for the objects displayed on the webpage

    **Return:**
        - ``history_tab`` -- for each transient ticket in the transient listings pages

    **Todo**
    """
    ################ > IMPORTS ################
    from time import strftime
    from .. import ticket_building_blocks
    from .. import tabs
    from ... import single_ticket
    from .....commonelements import forms

    log.info('starting the ``history_tab`` function')

    theseHistories = []
    theseHistories[:] = [t for t in objectHistories]

    transientBucketId = discoveryDataDictionary["transientBucketId"]
    content = ""

    # determine date added to the marshall
    dateAddedToMarshall = discoveryDataDictionary["dateAdded"]
    objectAddedToMarshallBy = discoveryDataDictionary["objectAddedToMarshallBy"]
    if not objectAddedToMarshallBy or objectAddedToMarshallBy.lower() == "none":
        thisLog = "object added to the 'inbox' via the marshall's automatic import scripts"
        if discoveryDataDictionary["decDeg"] > 30.:
            thisLog = "object added directly to the 'archive' via the marshall's automatic import scripts (> +30 dec)"
    else:
        thisLog = "object added to the 'inbox' by %(objectAddedToMarshallBy)s" % locals(
        )
    if discoveryDataDictionary["lsq_lightcurve"]:
        newEntry = {
            "transientBucketId": transientBucketId,
            "dateCreated": dateAddedToMarshall,
            "log": "LSQ's recalibrated data added to marshall" % locals(
            )
        }
    else:
        newEntry = {
            "transientBucketId": transientBucketId,
            "dateCreated": dateAddedToMarshall,
            "log": "%(thisLog)s" % locals(
            )
        }
    theseHistories.append(newEntry)

    # determine date classified
    classificationDate = discoveryDataDictionary["classificationDate"]
    classificationSurvey = discoveryDataDictionary["classificationSurvey"]
    classificationAddedBy = discoveryDataDictionary["classificationAddedBy"]
    objectAddedToMarshallBy = discoveryDataDictionary["objectAddedToMarshallBy"]
    if classificationDate:
        newEntry = {
            "transientBucketId": transientBucketId,
            "dateCreated": classificationDate,
            "log": "object classified by %(classificationSurvey)s (classification added by %(classificationAddedBy)s)" % locals(
            )
        }
        theseHistories.append(newEntry)

    from operator import itemgetter
    theseHistories = sorted(
        theseHistories, key=itemgetter('dateCreated'), reverse=False)

    for hLog in theseHistories:

        if hLog["transientBucketId"] == transientBucketId:
            content += _generate_log_string_for_ticket(
                log=log,
                logDate=hLog["dateCreated"],
                logString=hLog["log"])

    regex = re.compile(r'by (\w*)\.(\w*)')
    content = regex.sub(lambda match: "by " + match.group(1)[0].upper(
    ) + match.group(1)[1:] + " " + match.group(2)[0].upper() + match.group(2)[1:], content)

    history_tab = single_ticket._ticket_tab_template(
        log,
        request=request,
        tabHeader=False,
        blockList=[content + "<br>"],
        tabFooter=False,
        htmlId="historytab"
    )

    # convert bytes to unicode
    if isinstance(history_tab, str):
        history_tab = unicode(history_tab, encoding="utf-8", errors="replace")

    log.info('completed the ``history_tab`` function')
    return history_tab


# LAST MODIFIED : March 6, 2015
# CREATED : March 6, 2015
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method
def _generate_log_string_for_ticket(
        log,
        logDate,
        logString):
    """ generate log string for ticket

    **Key Arguments:**
        - ``log`` -- logger
        # copy usage method(s) here and select the following snippet from the command palette:
        # x-setup-docstring-keys-from-selected-usage-options

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean _generate_log_string_for_ticket function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``_generate_log_string_for_ticket`` function')

    relativeDate = dcu.pretty_date(
        date=logDate
    )
    logDate = logDate.strftime('%Y-%m-%d %H:%M:%S')
    # add text color
    logDate = khufu.coloredText(
        text=logDate,
        color="green",
        size=3,  # 1-10
        pull=False,  # "left" | "right",
        addBackgroundColor=False
    )
    # add text color
    relativeDate = khufu.coloredText(
        text="(" + relativeDate.strip() + ")",
        color="violet",
        size=3,  # 1-10
        pull=False,  # "left" | "right",
        addBackgroundColor=False
    )

    # add text color
    logString = khufu.coloredText(
        text=logString,
        color="cream",
        size=3,  # 1-10
        pull=False,  # "left" | "right",
        addBackgroundColor=False
    )
    logString = """<strong>%(logDate)s</strong>&nbsp&nbsp&nbsp%(relativeDate)s&nbsp&nbsp&nbsp%(logString)s""" % locals(
    )
    column = khufu.grid_column(
        span=10,  # 1-12
        offset=1,  # 1-12
        content=logString,
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )
    grid_row = khufu.grid_row(
        responsive=True,
        columns=column,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    log.info('completed the ``_generate_log_string_for_ticket`` function')
    return grid_row

# use the tab-trigger below for new function
# xt-def-with-logger


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
