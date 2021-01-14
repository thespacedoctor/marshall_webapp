#!/usr/local/bin/python
# encoding: utf-8
"""
*The comments block for the comments tab of the PESSTO Marshall object ticket*

:Author:
    David Young
"""
import sys
import os
import re
import datetime
import khufu
from fundamentals import times


def comments_block(
        log,
        request,
        discoveryDataDictionary,
        objectComments
):
    """comments_block

    **Key Arguments**

    - ``log`` -- the logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
    - ``objectComments`` -- the comments for the object


    **Return**

    - ``commentBlock`` -- the comments block for the transient ticket in the transient listings pages

    """
    commentBlock = ""
    count = 0

    for row in objectComments:
        if row["pesstoObjectsId"] != discoveryDataDictionary["transientBucketId"]:
            continue
        count += 1
        # AUTHOR
        author = row["commentAuthor"].replace(".", " ").replace(
            "_", " ").title().replace("Atel", "ATel")

        author = khufu.coloredText(
            text="""%(author)s: """ % locals(),
            color="red",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        # COMMENT
        comment = row["comment"].replace("<", "&lt;").replace("&lt;a", "<a").replace(
            "&gt;ATEL", ">ATEL").replace("&lt;/a&gt;", "</a>").replace("&lt;/a", "</a").replace("&quot;", '"').replace("&gt;", ">").replace('href=http',  'href="http')
        regex = re.compile(r'(href\=\"http[\w\d\.~/:?=]*?)\>', re.S)
        comment = regex.sub('\g<1>">', comment)

        # print comment
        comment = khufu.coloredText(
            text=comment,
            color="grey",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        # DATE
        from datetime import datetime, date, time
        now = datetime.now()
        delta = now - row["dateCreated"]
        delta = delta.days
        if (delta < 13):

            thisDate = times.datetime_relative_to_now(row["dateCreated"])
            if thisDate[-1:] == "d":
                thisDate = thisDate[2:-1]
                thisDate = """%(thisDate)s days ago""" % locals()
        else:
            thisDate = str(row["dateCreated"])[:10]
        thisDate = khufu.coloredText(
            text="""(%(thisDate)s) """ % locals(),
            color="green",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        commentRow = khufu.grid_row(
            responsive=True,
            columns="""%(author)s %(comment)s %(thisDate)s """ % locals(),
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        commentBlock = """%(commentBlock)s %(commentRow)s""" % locals()

    return count, commentBlock
