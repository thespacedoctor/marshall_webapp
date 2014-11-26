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
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import datetime
from docopt import docopt
import khufu
from dryxPython import commonutils as dcu

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 7, 2014
# CREATED : January 7, 2014
# AUTHOR : DRYX


def comments_block(
        log,
        request,
        discoveryDataDictionary,
        objectComments
):
    """comments_block

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the pyramid request
        - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
        - ``objectComments`` -- the comments for the object

    **Return:**
        - ``commentBlock`` -- the comments block for the transient ticket in the transient listings pages

    **Todo**
    """
    commentBlock = ""

    for row in objectComments:
        if row["pesstoObjectsId"] != discoveryDataDictionary["transientBucketId"]:
            continue
        # AUTHOR
        author = row["commentAuthor"].replace(".", " ").title()

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


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
