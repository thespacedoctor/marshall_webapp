#!/usr/local/bin/python
# encoding: utf-8
"""
templates_stats.py
==================
:Summary:
    The HTML template module for the `templates_stats.py` resource

:Author:
    David Young

:Date Created:
    October 6, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from ..commonelements.pagetemplates import defaultpagetemplate


class templates_stats():

    """
    The worker class for the templates_stats module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- request

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        request
    ):
        self.log = log
        log.debug("instansiating a new 'templates_stats' object")
        self.request = request
        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the templates_stats object

        **Return:**
            - ``webpage`` -- the webpage HTML

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        from ..commonelements.stats.esophaseIII import plot_wells, ssdr1_stats_table

        # get the image wells for the plots
        sofiImagingPlots = plot_wells(
            log=self.log,
            request=self.request
        )

        # get the ssdr1 stats table
        ssdr1Table = ssdr1_stats_table(
            log=self.log,
            request=self.request,
        )

        # d3 practice
        d3plot = self.generate_d3_plot()

        # craft the content of the page
        mainContent = khufu.grid_column(
            span=12,  # 1-12
            offset=0,  # 1-12
            content="""%(d3plot)s %(sofiImagingPlots)s %(ssdr1Table)s""" % locals(
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
            pageTitle="PESSTO Marshall",
            topNavBar=False,
            sideBar="stats",
            mainContent=mainContent,
            relativePathFromDocRoot=False,
            thisPageName="PESSTO Stats"
        )

        self.log.info('completed the ``get`` method')
        return webpage

    def generate_d3_plot(
            self):
        """generate d3 plot

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean generate_d3_plot method
            - @review: when complete add logging
        """
        self.log.info('starting the ``generate_d3_plot`` method')

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

            htmlContent += khufu.plots.svgchart.svgchart(
                htmlClass=htmlClass,
                csvUrl=False,
                disable=False,
                htmlId=False,
                chartType=""
            )
            htmlContent += "<hr>"

        self.log.info('completed the ``generate_d3_plot`` method')
        return htmlContent.decode('utf-8')

    # use the tab-trigger below for new method
    # xt-class-method
