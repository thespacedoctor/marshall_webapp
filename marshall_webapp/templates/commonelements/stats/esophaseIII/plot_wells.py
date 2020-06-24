#!/usr/bin/env python
# encoding: utf-8
"""
*Plots and stats for ESO PhaseIII Data Products*

:Author:
    David Young
"""
import sys
import os
import re
import khufu

def plot_wells(
        log,
        request,
        releaseVersion
):
    """The sofi/efosc imaging/spectra plot well for the stats page of the marshall

    **Key Arguments**

    - ``log`` -- the logger
    - ``request`` -- the pyramid request
    

    **Return**

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
                dataType=dataType,
                releaseVersion=releaseVersion
            )
            plotWells = """%(plotWells)s%(well)s""" % locals()

    return plotWells

def _generate_plot_well(
        log,
        request,
        instrument,
        dataType,
        releaseVersion):
    """ generate plot well

    **Key Arguments**

    - ``log`` -- the logger
    - ``request`` -- the pyramid request
    - ``instrument``
    - ``dataType``
    - ``releaseVersion`` - the release versions to seperate
    

    **Return**

    - ``plotWell`` -- the well of plots
    
    """
    log.debug('starting the ``_generate_plot_well`` function')

    # format attributes for titles
    instrument = instrument.upper()
    dataType = dataType[0].upper() + dataType[1:].lower()
    title = "%(instrument)s %(dataType)s" % locals()

    # GENERATE THE EMPTY WELL
    imageWell = khufu.imageWell(
        log=log,
        title=title,
        description="Metrics from the %(releaseVersion)s %(title)s" % locals(
        )
    )

    # REFORMAT ATTRIBUTES FOR DETECTING FILENAMES
    instrument = instrument.lower()
    dataType = dataType.lower()

    # SETUP THE PHASEIII STATS CACHE DIRECTORY
    statsCache = request.registry.settings["stats cache directory"]
    esoPhaseIII = """%(statsCache)s/phaseIII""" % locals()

    # FIND EACH SOFI/EFOSC IMAGING/SPECTRA PNG IN THE PHASEIII STATS CACHE AND APPEND IT TO
    # THE IMAGING WELL
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
                "%(releaseVersion)s %(instrument)s %(dataType)s " % locals(), "").lower()
            filepath = request.static_path(
                'marshall_webapp:static/caches/stats/phaseIII/%(d)s' % locals())
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
                delay=20
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
            sqlQuery = urllib.quote("""select currentFilename, %(xKey)s ,%(yKey)s from %(instrument)s_%(dataType)s where data_rel = "%(releaseVersion)s" and currentFilename not like "%%weight%%" order by %(yKey)s;""" % locals(
            ))
            csvType = urllib.quote("human")  # human or machine
            csvTitle = urllib.quote("ESO Phase III %(instrument)s %(dataType)s for %(releaseVersion)s" % locals(
            ))
            csvFilename = urllib.quote("%(xKey)s_vs_%(yKey)s.csv" % locals())
            returnFormat = urllib.quote("webpageView")

            popover = khufu.popover(
                tooltip=True,
                placement="bottom",  # [ top | bottom | left | right ]
                trigger="hover",  # [ False | click | hover | focus | manual ]
                title="view csv file in browser",
                content=False,
                delay=20
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
                delay=20
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

    log.debug('completed the ``_generate_plot_well`` function')
    if count:
        thisImageWell = imageWell.get()
    else:
        thisImageWell = ""

    return thisImageWell

# use the tab-trigger below for new function
