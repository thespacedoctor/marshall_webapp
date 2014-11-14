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
    @review: when complete review and cleanup this templates_stats.py module
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
        - @review: when complete, clean templates_stats class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        request
    ):
        self.log = log
        log.debug("instansiating a new 'templates_stats' object")
        self.request = request
        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the templates_stats object

        **Return:**
            - ``templates_stats``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        placeHolder = khufu.image(
            # [ industrial | gray | social ]
            src='holder.js/500x500/industrial/text:hello world',
        )

        from ..commonelements.stats.esophaseIII import plot_wells, ssdr1_stats_table

        sofiImagingPlots = plot_wells(
            log=self.log,
            request=request
        )

        ssdr1Table = ssdr1_stats_table(
            log=self.log,
            request=self.request,
        )

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

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
