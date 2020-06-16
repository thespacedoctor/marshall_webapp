#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_resource_stats.py` resource*

:Author:
    David Young

:Date Created:
    October 6, 2014
"""
from builtins import range
from builtins import object
import sys
import os
import khufu
from marshall_webapp.templates.commonelements.pagetemplates import defaultpagetemplate


class templates_resource_stats(object):
    """
    The worker class for the templates_resource_stats module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- request
        - ``elementId`` -- elementId
    """

    def __init__(
        self,
        log,
        request,
        elementId="SSDR1"
    ):
        self.log = log
        log.debug("instansiating a new 'templates_resource_stats' object")
        self.request = request
        self.elementId = elementId
        # xt-self-arg-tmpx

        return None

    def get(self):
        """get the templates_resource_stats object

        **Return:**
            - ``webpage`` -- the webpage HTML
        """
        self.log.debug('starting the ``get`` method')

        from marshall_webapp.templates.commonelements.stats.esophaseIII import plot_wells, ssdr_stats_table

        # GET THE IMAGE WELLS FOR THE PLOTS
        sofiImagingPlots = plot_wells(
            log=self.log,
            request=self.request,
            releaseVersion=self.elementId
        )

        # GET THE SSDR1 STATS TABLE
        ssdr1Table = ssdr_stats_table(
            log=self.log,
            request=self.request,
            releaseVersion=self.elementId
        )

        # # d3 practice
        # d3plot = self.generate_d3_plot()
        # d3plot = ""

        # CRAFT THE CONTENT OF THE PAGE
        mainContent = khufu.grid_column(
            span=12,  # 1-12
            offset=0,  # 1-12
            content="""%(sofiImagingPlots)s %(ssdr1Table)s""" % locals(
            ),
            pull=False,  # ["right", "left", "center"]
            htmlId=False,
            htmlClass="statspagecontent",
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        webpage = defaultpagetemplate(
            log=self.log,
            request=self.request,
            bodyId=False,
            pageTitle="ePESSTO+ Marshall",
            topNavBar=False,
            sideBar="stats",
            mainContent=mainContent,
            relativePathFromDocRoot=False,
            thisPageName="PESSTO Stats"
        )

        self.log.debug('completed the ``get`` method')
        return webpage

    def generate_d3_plot(
            self):
        """generate d3 plot
        """
        self.log.debug('starting the ``generate_d3_plot`` method')

        htmlContent = ""
        for i in range(1, 26):
            htmlClass = "example%(i)02d" % locals()
            htmlContent += khufu.pageHeader(
                headline=htmlClass,
                tagline=''
            )

            if i == 4:
                htmlContent += """
    <p>
      <label for="nHeight"
             style="display: inline-block; width: 240px; text-align: right">
             height = <span id="nHeight-value">…</span>
      </label>
      <input type="range" min="1" max="280" id="nHeight">
    </p>

    <p>
      <label for="nWidth"
             style="display: inline-block; width: 240px; text-align: right">
             width = <span id="nWidth-value">…</span>
      </label>
      <input type="range" min="1" max="400" id="nWidth">
    </p>"""

            if i == 5:
                htmlContent += """
    <p>
      <label for="nValue"
             style="display: inline-block; width: 240px; text-align: right">
             angle = <span id="nValue-value"></span>
      </label>
      <input type="number" min="0" max="360" step="5" value="0" id="nValue">
    </p>"""

            if i == 6:
                htmlContent += """
    <p>
      <label for="nRadius"
             style="display: inline-block; width: 240px; text-align: right">
             radius = <span id="nRadius-value">…</span>
      </label>
      <input type="range" min="1" max="150" id="nRadius">
    </p>
    """

            if i == 7:
                htmlContent += """
    <p>
      <label for="nAngle"
             style="display: inline-block; width: 240px; text-align: right">
             angle = <span id="nAngle-value">…</span>
      </label>
      <input type="range" min="0" max="360" id="nAngle">
    </p>
    """

            if i == 8:
                htmlContent += """
    <p>
      <label for="nAngle02"
         style="display: inline-block; width: 240px; text-align: right">
         angle = <span id="nAngle02-value">…</span>
      </label>
      <input type="range" min="0" max="360" id="nAngle02">
    </p>
    """

            if i == 9:
                htmlContent += """

    """

            if i == 10:
                htmlContent += """
    <div id="map" style="width: 600px; height: 400px"></div>
    """

            if i == 11:
                htmlContent += """
    <div id="map02" style="width: 600px; height: 400px"></div>
    """

            if i == 12:
                htmlContent += """

    """

            if i == 13:
                htmlContent += """

    """

            if i == 14:
                htmlContent += """

    """

            if i == 24:
                htmlContent += """
    <div id="new_input">
        &nbsp &nbsp
        Stock: <input type="text" name="stock" id="stock" value="GOOG"
        style="width: 70px;">
        &nbsp &nbsp
        Start: <input type="text" name="start" id="start" value="2013-08-10"
        style="width: 80px;">
        &nbsp &nbsp
        End: <input type="text" name="end" id="end" value="2014-03-10"
        style="width: 80px;">
        &nbsp &nbsp
        <input name="updateButton"
        type="button"
        value="Update"
        onclick="updateData()" />
    </div>
    """

            htmlContent += khufu.plots.svg.svg(
                htmlClass=htmlClass,
                csvUrl=False,
                disable=False,
                htmlId=False,
                chartType=""
            )
            htmlContent += "<hr>"

        self.log.debug('completed the ``generate_d3_plot`` method')
        return htmlContent.decode('utf-8')

    # xt-class-method
