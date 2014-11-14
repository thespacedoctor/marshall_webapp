#!/usr/local/bin/python
# encoding: utf-8
"""
comments_block.py
=================
:Summary:
    The comments block for the comments tab of the PESSTO Marshall object ticket

:Author:
    David Young

:Date Created:
    January 7, 2014

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
# LAST MODIFIED : January 7, 2014
# CREATED : January 7, 2014
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def comments_block(
        log,
        request,
        discoveryDataDictionary,
        objectComments
):
    """comments_block

    **Key Arguments:**
        # copy usage method(s) here and select the following snippet from the command palette:
        - ``log`` -- the logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
        - ``objectComments`` -- the comments for the object

    **Return:**
        - None

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    import datetime
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import khufu
    import dryxPython.commonutils as dcu

    commentBlock = ""

    for row in objectComments:
        if row["pesstoObjectsId"] != discoveryDataDictionary["transientBucketId"]:
            continue
        # AUTHOR
        author = row["commentAuthor"]
        author = khufu.coloredText(
            text="""%(author)s: """ % locals(),
            color="red",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        # COMMENT
        comment = row["comment"].replace("&lt;a", "<a").replace(
            "&gt;ATEL", ">ATEL").replace("&lt;/a&gt;", "</a>").replace("&quot;", '"')
        comment = khufu.coloredText(
            text=comment,
            color="grey",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        # DATE
        relativeDate = dcu.pretty_date(
            date=row["dateCreated"]
        )
        if relativeDate[-1:] == "d":
            relativeDate = relativeDate[2:-1]
            relativeDate = """%(relativeDate)s days ago""" % locals()
        relativeDate = khufu.coloredText(
            text="""(%(relativeDate)s) """ % locals(),
            color="green",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        commentRow = khufu.grid_row(
            responsive=True,
            columns="""%(author)s %(comment)s %(relativeDate)s """ % locals(),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        commentBlock = """%(commentBlock)s %(commentRow)s""" % locals()

    return commentBlock

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
