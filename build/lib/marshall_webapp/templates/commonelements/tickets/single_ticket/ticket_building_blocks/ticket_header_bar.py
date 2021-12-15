#!/usr/local/bin/python
# encoding: utf-8
"""
*The ticket header bar for the object ticket*

:Author:
    David Young
"""
import sys
import os
import re
import datetime
from marshall_webapp.templates.commonelements import commonutils as cu
import khufu
from fundamentals import times


def ticket_header_bar(
        log,
        request,
        discoveryDataDictionary,
        objectComments,
        atelData,
        lightcurveData,
        objectHistories):
    """get ticket header bar

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``discoveryDataDictionary`` -- a dictionary of the discovery data for this transient.
    - ``objectComments`` -- the comments for the object
    - ``atelData`` -- the atel matches for the objects displayed on the webpage
    - ``lightcurveData`` -- the transient lightcurve data
    - ``objectHistories`` -- the object histories


    **Return**

    - ``ticket_header_bar`` -- the ticket identity bar for the pesssto object

    """
    log.debug('starting the ``ticket_header_bar`` function')

    ## VARIABLES ##
    now = datetime.datetime.now()
    currentMagEstimate = discoveryDataDictionary["currentMagnitudeEstimate"]
    if currentMagEstimate in [9999, -9999]:
        for dataPoint in lightcurveData:
            if dataPoint["transientBucketId"] == discoveryDataDictionary["transientBucketId"]:
                break
        if len(lightcurveData) and (now - dataPoint["observationDate"] < datetime.timedelta(days=7)):
            currentMagEstimate = dataPoint["magnitude"]
    magWarning = None
    if currentMagEstimate and currentMagEstimate > 21.0:
        magWarning = _get_magnitude_warning(
            log,
            currentMag=currentMagEstimate,
            transientBucketId=discoveryDataDictionary["transientBucketId"]
        )

    if magWarning:
        pass
    else:
        magWarning = ""

    # ATEL WARNING IF REQUIRED
    atelWarning = None
    if discoveryDataDictionary["classifiedFlag"] == 0:
        atelWarning = _get_atel_warning(
            log,
            atelData=atelData,
            transientBucketId=discoveryDataDictionary["transientBucketId"]
        )

    if atelWarning:
        pass
    else:
        atelWarning = ""

    # RESURRECTED OBJECT WARNING
    ressurectedWarning = _resurrected_object_warning(
        log,
        objectHistories,
        transientBucketId=discoveryDataDictionary["transientBucketId"]
    )

    theseObjectComments = []
    theseObjectComments[:] = [t for t in objectComments if t[
        "pesstoObjectsId"] == discoveryDataDictionary["transientBucketId"]]

    latestComment = ""
    if len(theseObjectComments):
        latestComment = theseObjectComments[0]["comment"].replace("<", "&lt;").replace("&lt;a", "<a").replace(
            "&gt;ATEL", ">ATEL").replace("&lt;/a&gt;", "</a>").replace("&lt;/a", "</a").replace("&quot;", '"').replace("&gt;", ">").replace('href=http',  'href="http')
        regex = re.compile(r'(href\=\"http[\w\d\.~/:?=]*?)\>', re.S)
        latestComment = regex.sub('\g<1>">', latestComment)
        # convert bytes to unicode
        log.debug("""latestComment: `%(latestComment)s`""" % locals())
        commentDate = theseObjectComments[0]["dateCreated"]
        commentAuthor = theseObjectComments[0][
            "commentAuthor"].lower().replace("_", " ").replace(".", " ").title()
        commentAuthor = khufu.coloredText(
            text="""- %(commentAuthor)s""" % locals(),
            color="green",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        # FROM DATETIME IMPORT DATETIME, DATE, TIME
        now = datetime.datetime.now()
        delta = now - commentDate
        delta = delta.days
        if (delta < 13):

            thisDate = times.datetime_relative_to_now(commentDate)
            if thisDate[-1:] == "d":
                thisDate = thisDate[2:-1]
                thisDate = """%(thisDate)s days ago""" % locals()
        else:
            thisDate = str(commentDate)[:10]
        thisDate = thisDate.strip()
        if thisDate[:2] == "1 ":
            thisDate = thisDate.replace("days", "day")

        prefix = khufu.coloredText(
            text="<strong>latest comment (%(thisDate)s):</strong>" % locals(
            ),
            color="blue",
            size=False,  # 1-10
            pull=False,  # "left" | "right"
        )

        # ADD TEXT COLOR
        latestComment = khufu.coloredText(
            text=latestComment,
            color="cream",
            size=False,  # 1-10
            pull=False,  # "left" | "right",
            addBackgroundColor=False
        )

        latestComment = khufu.well(
            wellText="""%(prefix)s  %(latestComment)s %(commentAuthor)s""" % locals(
            ),
            wellSize='small'
        )

    # LSQ FORCE PHOTOMETRY WARNING
    lsqFPAlert = _get_no_lsq_recalibrated_data_alert(
        log=log,
        lightcurveData=lightcurveData,
        discoveryDataDictionary=discoveryDataDictionary
    )

    comment = khufu.grid_row(
        responsive=True,
        columns="""%(latestComment)s""" % locals(),
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    topbar = khufu.grid_column(
        span=12,  # 1-12
        offset=0,  # 1-12
        content="""%(ressurectedWarning)s %(magWarning)s %(atelWarning)s %(lsqFPAlert)s %(comment)s """ % locals(
        ),
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    topbar = khufu.grid_row(
        responsive=True,
        columns=topbar,
        htmlId=False,
        htmlClass="ticketHeader",
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    return topbar


def _get_atel_warning(
        log,
        atelData,
        transientBucketId):
    """ get atel warning for ticket

    **Key Arguments**

    - ``log`` -- logger
    - ``atelData`` -- the atel matches for the objects displayed on the webpage
    - ``transientBucketId`` -the unquie id for the transient in the marshall database


    **Return**

    - ``warning`` or None -- the atel warning

    """
    log.debug('starting the ``_get_atel_warning`` function')
    ## VARIABLES ##
    rows = []
    for dataPoint in atelData:
        if dataPoint["transientBucketId"] == transientBucketId:
            row = dataPoint
            rows.append(row)

    atelLinks = []
    for row in rows:
        thisName = row["name"].replace("atel_", "")
        atelLink = khufu.a(
            content="""ATel %(thisName)s""" % locals(),
            href=row["surveyObjectUrl"],
            openInNewTab=True
        )
        atelLinks.append(atelLink)

    atels = ""
    if len(atelLinks):
        atels = """this object many have been classified already - see """
        count = 1
        for link in atelLinks:
            atels = "%(atels)s %(link)s" % locals()
            if count != len(atelLinks):
                atels = "%(atels)s, " % locals()
            count += 1
        log.debug('completed the ``_get_atel_warning`` function')

        atels = khufu.alert(
            alertText=atels,
            alertHeading='Warning',
            extraPadding=False,
            alertLevel='error'
        )

        return atels

    log.debug('completed the ``_get_atel_warning`` function')
    return None


def _get_magnitude_warning(
        log,
        currentMag,
        transientBucketId):
    """ get atel warning for ticket

    **Key Arguments**

    - ``log`` -- logger
    - ``currentMag`` -- the current magnitude estimate of the object
    - ``transientBucketId`` -the unquie id for the transient in the marshall database


    **Return**

    - ``warning`` or None -- the atel warning

    """
    log.debug('starting the ``_get_magnitude_warning`` function')

    if currentMag in [9999, -9999]:
        text = "not enough data to determine a current magnitude"
        alertLevel = 'info'
        alertHeading = "Alert"
    else:
        text = "this object is too faint to take a classification spectrum - please consider archiving it"
        alertLevel = "error"
        alertHeading = "Warning"

    alert = khufu.alert(
        alertText=text,
        alertHeading=alertHeading,
        extraPadding=False,
        alertLevel=alertLevel
    )
    return alert

    log.debug('completed the ``_get_magnitude_warning`` function')
    return None


def _get_no_lsq_recalibrated_data_alert(
        log,
        lightcurveData,
        discoveryDataDictionary):
    """ get no lsq recalibrated data alert

    **Key Arguments**

    - ``log`` -- logger
    - ``discoveryDataDictionary`` -- dictionary of the transient's discovery data
    - ``lightcurveData`` -- the transient lightcurve data


    **Return**

    - ``alert`` -- alert for when LSQ object has no recalibrated data yet

    """
    log.debug('starting the ``_get_no_lsq_recalibrated_data_alert`` function')

    alert = ""
    for row in lightcurveData:
        if row["transientBucketId"] == discoveryDataDictionary["transientBucketId"]:
            if row["survey"] and row["survey"].lower() == "lsq-discoveries":
                name = discoveryDataDictionary["masterName"]
                alert = khufu.alert(
                    alertText='lsq forced photometry not yet available for %(name)s' % locals(
                    ),
                    alertHeading='Note',
                    extraPadding=False,
                    # [ "warning" | "error" | "success" | "info" ]
                    alertLevel='info'
                )
                break

    log.debug('completed the ``_get_no_lsq_recalibrated_data_alert`` function')
    return alert


def _resurrected_object_warning(
        log,
        objectHistories,
        transientBucketId):
    """ get no lsq recalibrated data alert

    **Key Arguments**

    - ``log`` -- logger
    - ``transientBucketId`` -- the transientBucketId
    - ``objectHistories`` -- the transient lightcurve data


    **Return**

    - ``alert`` -- alert for when LSQ object has no recalibrated data yet

    """
    log.debug('starting the ``_resurrected_object_warning`` function')

    notification = False
    for row in objectHistories:
        if row["transientBucketId"] == transientBucketId:
            if "marshall's object resurrector" in row["log"]:
                notification = True
            else:
                notification = False

    if notification is True:
        notification = khufu.alert(
            alertText='Resurrected from archive - possibly on the rise again',
            alertHeading='Note',
            extraPadding=False,
            # [ "warning" | "error" | "success" | "info" ]
            alertLevel='success'
        )
    else:
        notification = ""

    log.debug('completed the ``_resurrected_object_warning`` function')
    return notification
