#!/usr/local/bin/python
# encoding: utf-8
"""
templates_xmatches_catalogues.py
========================================================
:Summary:
    The HTML template module for the `templates_xmatches_catalogues.py` resource

:Author:
    David Young

:Date Created:
    October 13, 2015

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
import re
from marshall_webapp.models.xmatches_catalogues import models_xmatches_catalogues_get
from marshall_webapp.models.xmatches_catalogues.element import models_xmatches_element_catalogues_get


class templates_xmatches_catalogues():

    """
    The worker class for the templates_xmatches_catalogues module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the element id of the resource requested (or false)
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        elementId=False,
        format=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'templates_xmatches_catalogues' object")

        # Initial Actions

        return None

    # Method Attributes
    def get(self):
        """get the templates_xmatches_catalogues object

        **Return:**
            - ``responseContent`` -- the response

        **Todo**
        """
        self.log.debug('starting the ``get`` method')

        from marshall_webapp.templates.commonelements.pagetemplates import defaultpagetemplate

        if self.elementId == False:
            xmatches_catalogues = models_xmatches_catalogues_get(
                log=self.log,
                request=self.request
            )
            self.catalogues = xmatches_catalogues.get()

            from marshall_webapp.templates.commonelements.pagetemplates import defaultpagetemplate

            # add text color
            text = khufu.coloredText(
                text="<BR>Click on the <em>associated transient</em> links to reveal matched transient tickets<br><br>",
                color="grey",
                size=4,  # 1-10
                pull="right",  # "left" | "right",
                addBackgroundColor=False
            )

            maincontent = text + self.create_table()

            webpage = defaultpagetemplate(
                log=self.log,
                request=self.request,
                bodyId=False,
                pageTitle="PESSTO Marshall",
                topNavBar=False,
                sideBar="xmatches",
                mainContent=maincontent,
                relativePathFromDocRoot=False,
                thisPageName="xmatches"
            )
        else:
            from templates_transients import templates_transients
            webpage = templates_transients(
                log=self.log,
                request=self.request,
                tcsCatalogueId=self.elementId
            ).get()

        self.log.debug('completed the ``get`` method')
        return webpage

    def create_table(
            self):
        """create table

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean create_table method
            - @review: when complete add logging
        """
        self.log.debug('starting the ``create_table`` method')

        columnsNames = ["Catalogue",
                        "Associated Transients", "Top Rank Associated Transients"]
        columnsNamesDB = ["catalogue_table_name",
                          "all_count", "top_rank_count"]

        for row in self.catalogues:
            print row
            matchObject = re.finditer(
                r'.*_(v\d.*)',
                row["catalogue_table_name"],
                flags=0  # re.S
            )

            for k, v in dict(row).iteritems():
                if isinstance(v, float):
                    row[k] = "{:,.0f}".format(v)

            href = self.request.route_path(
                'xmatches_element_catalogues', elementId=row["catalogue_table_id"])
            row["all_count"] = khufu.a(
                content=row["all_count"],
                href=href
            )

            href = self.request.route_path(
                'xmatches_element_catalogues', elementId=row["catalogue_table_id"], )
            row["all_count"] = khufu.a(
                content=row["all_count"],
                href=href
            )

            href = self.request.route_path('xmatches_element_catalogues', elementId=row[
                "catalogue_table_id"], _query={'tcsRank': 1})
            row["top_rank_count"] = khufu.a(
                content=row["top_rank_count"],
                href=href
            )

        import khufu.tables.sortable_table as sortable_table
        # build a sortable table
        table = sortable_table.sortable_table(
            currentPageUrl=self.request.path_qs,
            columnsToDisplay=columnsNamesDB,
            tableRowsDictionary=self.catalogues,
            log=self.log,
            defaultSort=False
        )

        # replace column names with display names (e.g. for when MySQL column
        # names are used)
        nd = table.modifyDisplayNameDict
        for o, n in zip(columnsNamesDB, columnsNames):
            nd[o] = n

        # replace column names with sortBy names (e.g. for when MySQL column names are used)
        # sd = table.modifySortByDict
        # xt-sortby-dictionary

        # change relative column sizes
        # table.modifyColumnWidths = ["3", "28", ... ]

        # search trigger when clicking on a row
        # table.searchKeyAndColumn = ("searchString", "plainName")
        # table.columnsToHide = ["plainName"]

        table = table.get()

        self.log.debug('completed the ``create_table`` method')
        return table

    # use the tab-trigger below for new method
    # xt-class-method
