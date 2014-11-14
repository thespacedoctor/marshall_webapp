#!/usr/local/bin/python
# encoding: utf-8
"""
ssdr1_stats_table.py
====================
:Summary:
    The stats table for ESO Phase III SSDR1

:Author:
    David Young

:Date Created:
    October 6, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
import khufu
# from ..__init__ import *

###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx
# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : October 6, 2014
# CREATED : October 6, 2014
# AUTHOR : DRYX
def ssdr1_stats_table(
        log,
        request):
    """ssdr1 stats table

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean ssdr1_stats_table function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``ssdr1_stats_table`` function')

    # get the table data
    sqlQuery = """
        select * from stats_ssdr1_overview
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
        select sum(numberOfFiles) as numberOfFiles, sum(dataVolumeBytes) as dataVolumeBytes from stats_ssdr1_overview
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
        striped=True,
        bordered=False,
        hover=True,
        condensed=False
    )

    log.info('completed the ``ssdr1_stats_table`` function')
    return table

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
