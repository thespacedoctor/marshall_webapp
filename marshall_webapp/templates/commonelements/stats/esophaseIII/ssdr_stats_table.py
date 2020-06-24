#!/usr/local/bin/python
# encoding: utf-8
"""
*The stats table for ESO Phase III SSDR*

:Author:
    David Young
"""
import sys
import os
import khufu
from marshall_webapp.models.stats import models_stats_get

def ssdr_stats_table(
        log,
        request,
        releaseVersion):
    """ssdr stats table

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``releaseVersion`` -- which release
    

    **Return**

    - ``table`` -- the ssdr FITS file stats table
    
    """
    log.debug('starting the ``ssdr_stats_table`` function')

    # get the table data
    thisTable = releaseVersion.lower()

    stats = models_stats_get(
        log=log,
        request=request,
        elementId=releaseVersion
    )
    result = stats.get()

    fileTypes = result["fileTypes"]
    fileTotals = result["fileTotals"]

    headerList = ["File Type", "Number of Files", "Data Volume"]

    tableHead = ""
    for h in headerList:
        th = khufu.th(
            content=h,
            color=False
        )
        tableHead = "%(tableHead)s%(th)s" % locals()
    tableHead = khufu.thead(
        trContent=tableHead
    )

    tableBody = ""
    for row in fileTypes:
        tableRow = ""
        fileType = row["filetype"].replace("_", " ").replace(
            "efosc", "EFOSC").replace("sofi", "SOFI")
        numberOfFiles = row["numberOfFiles"]
        # convert to GB
        dataVolume = float(row["dataVolumeBytes"]) / (1024. ** 3)
        if dataVolume < 1.:
            dataVolume = float(row["dataVolumeBytes"]) / (1024. ** 2)
            dataVolume = "%(dataVolume)0.2f MB" % locals()
        else:
            dataVolume = "%(dataVolume)0.2f GB" % locals()

        td = khufu.td(
            content=fileType,
            color=False
        )
        tableRow = "%(tableRow)s%(td)s" % locals()
        td = khufu.td(
            content=numberOfFiles,
            color=False
        )
        tableRow = "%(tableRow)s%(td)s" % locals()
        td = khufu.td(
            content=dataVolume,
            color=False
        )
        tableRow = "%(tableRow)s%(td)s" % locals()
        tr = khufu.tr(
            cellContent=tableRow,
            color=False
        )
        tableRow = ""
        tableBody = "%(tableBody)s%(tr)s" % locals()

    numberOfFiles = fileTotals[0]["numberOfFiles"]
    dataVolume = float(fileTotals[0]["dataVolumeBytes"]) / (1024. ** 3)
    if dataVolume < 1.:
        dataVolume = float(row["dataVolumeBytes"]) / (1024. ** 2)
        dataVolume = "%(dataVolume)0.2f MB" % locals()
    else:
        dataVolume = "%(dataVolume)0.2f GB" % locals()

    tableRow = ""
    td = khufu.td(
        content="<strong>Total</strong>",
        color=False
    )
    tableRow = "%(tableRow)s%(td)s" % locals()
    td = khufu.td(
        content=numberOfFiles,
        color=False
    )
    tableRow = "%(tableRow)s%(td)s" % locals()
    td = khufu.td(
        content=dataVolume,
        color=False
    )
    tableRow = "%(tableRow)s%(td)s" % locals()
    tr = khufu.tr(
        cellContent=tableRow,
        color=False
    )
    tableBody = "%(tableBody)s%(tr)s" % locals()

    tableBody = khufu.tbody(
        trContent=tableBody
    )
    table = khufu.table(
        caption='',
        thead=tableHead,
        tbody=tableBody,
        striped=True
    )

    log.debug('completed the ``ssdr_stats_table`` function')
    return table
