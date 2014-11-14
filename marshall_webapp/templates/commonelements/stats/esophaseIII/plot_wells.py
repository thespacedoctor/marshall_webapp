#!/usr/bin/env python
# encoding: utf-8
"""
plot_wells.py

===============
:Summary:
    Plots and stats for ESO PhaseIII Data Products

:Author:
    David Young

:Date Created:
    April 29, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
from docopt import docopt
from dryxPython import commonutils as dcu
import khufu

###################################################################
# CLASSES                                                         #
###################################################################
# class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : April 29, 2014
# CREATED : April 29, 2014
# AUTHOR : DRYX
def plot_wells(
        log,
        request
):
    """The sofi/efosc imaging/spectra plot well for the stats page of the marshall

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the pyramid request

    **Return:**
        - ``plotWells`` -- the sofi/efosc imaging/spectra plot well
    """

    plotWells = ""

    instruments = ["sofi", "efosc"]
    dataTypes = ["spectra", "imaging"]

    for instrument in instruments:
        for dataType in dataTypes:
            well = _generate_plot_well(
                log=log,
                request=request,
                instrument=instrument,
                dataType=dataType
            )
            plotWells = """%(plotWells)s%(well)s""" % locals()

    return plotWells

# LAST MODIFIED : April 30, 2014
# CREATED : April 30, 2014
# AUTHOR : DRYX


def _generate_plot_well(
        log,
        request,
        instrument,
        dataType):
    """ generate plot well

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the pyramid request
        - ``instrument``
        - ``dataType``

    **Return:**
        - ``plotWell`` -- the well of plots
    """
    log.info('starting the ``_generate_plot_well`` function')

    # format attributes for titles
    instrument = instrument.upper()
    dataType = dataType[0].upper() + dataType[1:].lower()
    title = "%(instrument)s %(dataType)s" % locals()

    # generate the empty well
    imageWell = khufu.imageWell(
        log=log,
        title=title,
        description="Metrics from the SSDR1 %(title)s" % locals(
        )
    )

    # reformat attributes for detecting filenames
    instrument = instrument.lower()
    dataType = dataType.lower()

    # setup the phaseIII stats cache directory
    statsCache = request.registry.settings["stats cache directory"]
    esoPhaseIII = """%(statsCache)s/phaseIII""" % locals()

    # find each sofi/efosc imaging/spectra png in the phaseIII stats cache and append it to
    # the imaging well
    basePath = esoPhaseIII
    count = 0
    for d in os.listdir(basePath):
        filepath = os.path.join(basePath, d)
        if os.path.isfile(filepath) and "png" in d and instrument in d and dataType in d:
            count += 1
            log.debug(
                'instrument, instrument, d: %(instrument)s %(dataType)s %(d)s' %
                locals())
            fulltitle = d.replace(".png", "").replace(
                "_", " ")
            title = fulltitle.replace(
                "ssdr1 %(instrument)s %(dataType)s " % locals(), "")
            filepath = """/marshall/images/stats_cache/phaseIII/%(d)s""" % locals(
            )
            link = khufu.a(
                content='view in new tab',
                href=filepath,
                openInNewTab=True,
            )

            popover = khufu.popover(
                tooltip=True,
                placement="bottom",  # [ top | bottom | left | right ]
                trigger="hover",  # [ False | click | hover | focus | manual ]
                title="view plot in new tab",
                content=False,
                delay=200
            )

            imageButton = khufu.button(
                buttonText="""<i class="icon-file-pdf"></i>""",
                # [ default | primary | info | success | warning | danger | inverse | link ]
                buttonStyle='success',
                buttonSize='small',  # [ large | default | small | mini ]
                htmlId=False,
                href=filepath,
                pull=False,  # right, left, center
                submit=False,
                block=False,
                disable=False,
                dataToggle=False,  # [ modal ]
                popover=popover
            )

            matchObject = re.search(
                r'.*?(imaging|spectra)_(.*)_vs_(.*)\.png',
                d,
                flags=0  # re.S
            )

            if matchObject:
                dataType = matchObject.group(1)
                xKey = matchObject.group(2)
                yKey = matchObject.group(3)

            import urllib
            sqlQuery = urllib.quote("""select currentFilename, %(xKey)s ,%(yKey)s from %(instrument)s_%(dataType)s where data_rel = "SSDR1" and currentFilename not like "%%weight%%" order by %(yKey)s;""" % locals(
            ))
            csvType = urllib.quote("human")  # human or machine
            csvTitle = urllib.quote("ESO Phase III %(instrument)s %(dataType)s for SSDR1" % locals(
            ))
            csvFilename = urllib.quote("%(xKey)s_vs_%(yKey)s.csv" % locals())
            returnFormat = urllib.quote("webpageView")

            popover = khufu.popover(
                tooltip=True,
                placement="bottom",  # [ top | bottom | left | right ]
                trigger="hover",  # [ False | click | hover | focus | manual ]
                title="view csv file in browser",
                content=False,
                delay=200
            )

            viewCsvButton = khufu.button(
                buttonText="""<i class="icon-pilcrow"></i>""",
                # [ default | primary | info | success | warning | danger | inverse | link ]
                buttonStyle='success',
                buttonSize='small',  # [ large | default | small | mini ]
                htmlId=False,
                href="/marshall/scripts/python/sqlquery_to_csv.py?sqlQuery=%(sqlQuery)s&csvType=%(csvType)s&csvFilename=%(csvFilename)s&returnFormat=%(returnFormat)s&csvTitle=%(csvTitle)s" % locals(
                ),
                pull=False,  # right, left, center
                submit=False,
                block=False,
                disable=False,
                dataToggle=False,  # [ modal ]
                popover=popover
            )

            buttonGroup = khufu.buttonGroup(
                buttonList=[imageButton, viewCsvButton],
                format='default'  # [ default | toolbar | vertical ]
            )

            returnFormat = urllib.quote("webpageDownload")
            popover = khufu.popover(
                tooltip=True,
                placement="bottom",  # [ top | bottom | left | right ]
                trigger="hover",  # [ False | click | hover | focus | manual ]
                title="download csv file of plot data",
                content=False,
                delay=200
            )
            downloadCsv = khufu.button(
                buttonText="""<i class="icon-pilcrow"></i>""",
                # [ default | primary | info | success | warning | danger | inverse | link ]
                buttonStyle='primary',
                buttonSize='small',  # [ large | default | small | mini ]
                htmlId=False,
                href="/marshall/scripts/python/sqlquery_to_csv.py?sqlQuery=%(sqlQuery)s&csvType=%(csvType)s&csvFilename=%(csvFilename)s&returnFormat=%(returnFormat)s&csvTitle=%(csvTitle)s" % locals(
                ),
                pull=False,  # right, left, center
                submit=False,
                block=False,
                disable=False,
                dataToggle=False,  # [ modal ]
                popover=popover
            )

            imageWell.appendImage(
                imagePath=filepath,
                imageTitle=title,
                modalHeaderContent=fulltitle,
                modalFooterContent="""view in browser:&nbsp%(buttonGroup)s &nbsp&nbsp downloads: """ % locals(
                ),
                modalFooterButtons=[downloadCsv])
        else:
            log.debug('NOTHING FOUND TO PLOT')

    log.info('completed the ``_generate_plot_well`` function')
    if count:
        thisImageWell = imageWell.get()
    else:
        thisImageWell = ""

    return thisImageWell

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
