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
            request=request
        )

        # get the ssdr1 stats table
        ssdr1Table = ssdr1_stats_table(
            log=self.log,
            request=self.request,
        )

        # craft the content of the page
        mainContent = khufu.grid_column(
            span=12,  # 1-12
            offset=0,  # 1-12
            content="""%(sofiImagingPlots)s %(ssdr1Table)s""" % locals(),
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

    # xt-class-method
