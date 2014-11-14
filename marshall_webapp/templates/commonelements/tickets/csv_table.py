#!/usr/local/bin/python
# encoding: utf-8
"""
csv_table.py
============
:Summary:
    Create CSV versions of the marshall tables being displayed

:Author:
    David Young

:Date Created:
    March 4, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import io
import csv
from docopt import docopt
from dryxPython import commonutils as dcu
from dryxPython import astrotools as dat
import datetime

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : March 4, 2014
# CREATED : March 4, 2014
# AUTHOR : DRYX


def csv_table(
        log,
        objectData,
        tableColumnNames=False,
        tableColumns=False,
        csvType="human"
):
    """csv_table

    **Key Arguments:**
        - ``log`` -- the logger
        - ``objectData`` -- a list of object dictionaries
        - ``tableColumnNames`` -- the table columns to be displayed - name / mysql name dictionary
        - ``tableColumns`` -- the table columns to be displayed
        - ``csvType`` -- the type of csv to generate

    **Return:**
        - None

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    # create an object to write to
    output = io.BytesIO()

    # setup csv styles
    if csvType == "machine":
        delimiter = ","
    elif csvType == "human":
        delimiter = "|"
    writer = csv.writer(output, dialect='excel', delimiter=delimiter,
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dividerWriter = csv.writer(output, dialect='excel', delimiter="+",
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # add column names to csv
    header = []
    divider = []
    allRows = []
    # table border for human readable
    if csvType == "human":
        header.append("")
        divider.append("")

    for name in tableColumns:
        if csvType == "machine":
            header.append(tableColumnNames[name])
            if "decdeg" in name.lower():
                header.append("ra_sex")
                header.append("dec_sex")
        elif csvType == "human":
            if "name" in name.lower():
                header.append(tableColumnNames[name].ljust(30).rjust(31))
                divider.append('-' * 31)
            elif "date" in name.lower() or "detection" in name.lower():
                header.append(tableColumnNames[name].ljust(26).rjust(27))
                divider.append('-' * 27)
            else:
                header.append(tableColumnNames[name].ljust(13).rjust(14))
                divider.append('-' * 14)

            if "decdeg" in name.lower():
                header.append("ra (sex)".ljust(13).rjust(14))
                header.append("dec (sex)".ljust(13).rjust(14))
                divider.append('-' * 14)
                divider.append('-' * 14)

    # table border for human readable
    if csvType == "human":
        header.append("")
        divider.append("")

    if csvType == "machine":
        writer.writerow(header)
    elif csvType == "human":
        dividerWriter.writerow(divider)
        writer.writerow(header)
        dividerWriter.writerow(divider)

    # clean up data
    for obj in objectData:
        # ADD SEXEGEMAL
        if "decDeg" in obj:
            raSex = dat.ra_to_sex(
                ra=float(obj["raDeg"]),
                delimiter=':'
            )
            decSex = dat.dec_to_sex(
                dec=float(obj["decDeg"]),
                delimiter=':'
            )

        thisRow = []
        # table border for human readable
        if csvType == "human":
            thisRow.append("")

        for c in tableColumns:
            if c.lower() in ["radeg", "decdeg"]:
                obj[c] = "%6.3f" % obj[c]
            elif c == "absolutePeakMagnitude" and obj[c]:
                obj[c] = "%6.2f" % obj[c]
            elif isinstance(obj[c], float) or isinstance(obj[c], long):
                obj[c] = "%6.2f" % obj[c]
            elif not obj[c] or (isinstance(obj[c], str) and ("unkn" in obj[c].lower())):
                obj[c] = ""
            elif isinstance(obj[c], datetime.datetime):
                # obj[c] = "boom"
                relativeDate = dcu.pretty_date(
                    date=obj[c]
                )
                thisDate = str(obj[c])[:10]
                obj[c] = "%(relativeDate)s %(thisDate)s" % locals()

            if csvType == "human":
                if "name" in c.lower():
                    obj[c] = str(obj[c].ljust(30).rjust(31))
                elif "date" in c.lower() or "detection" in c.lower():
                    obj[c] = str(obj[c].ljust(26).rjust(27))
                else:
                    obj[c] = str(obj[c].ljust(13).rjust(14))

            thisRow.append(obj[c])
            if c.lower() == "decdeg":
                thisRow.append(raSex.ljust(13).rjust(14))
                thisRow.append(decSex.ljust(13).rjust(14))
        # table border for human readable
        if csvType == "human":
            thisRow.append("")

        allRows.append(thisRow)

    # write out the data
    writer.writerows(allRows)
    # table border for human readable
    if csvType == "human":
        dividerWriter.writerow(divider)

    return output.getvalue()

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
