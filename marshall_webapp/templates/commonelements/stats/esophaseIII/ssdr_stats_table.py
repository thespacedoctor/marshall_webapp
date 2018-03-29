#!/usr/local/bin/python
# encoding: utf-8
"""
ssdr_stats_table.py
====================
:Summary:
    The stats table for ESO Phase III SSDR

:Author:
    David Young

:Date Created:
    October 6, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
import khufu

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : October 6, 2014
# CREATED : October 6, 2014
# AUTHOR : DRYX


def ssdr_stats_table(
        log,
        request,
        releaseVersion):
    """ssdr stats table

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``releaseVersion`` -- which release

    **Return:**
        - ``table`` -- the ssdr FITS file stats table

    **Todo**
    """
    log.debug('starting the ``ssdr_stats_table`` function')

    # get the table data
    thisTable = releaseVersion.lower()
    sqlQuery = """
        select * from stats_%(thisTable)s_overview
    """ % locals()
    rowsTmp = request.db.execute(sqlQuery).fetchall()
    rows = []
    rows[:] = [dict(zip(row.keys(), row)) for row in rowsTmp]

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
    for row in rows:
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

    sqlQuery = """
        select sum(numberOfFiles) as numberOfFiles, sum(dataVolumeBytes) as dataVolumeBytes from stats_%(thisTable)s_overview
    """ % locals()
    rowsTmp = request.db.execute(sqlQuery).fetchall()
    rows = []
    rows[:] = [dict(zip(row.keys(), row)) for row in rowsTmp]

    numberOfFiles = rows[0]["numberOfFiles"]
    dataVolume = float(rows[0]["dataVolumeBytes"]) / (1024. ** 3)
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

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
