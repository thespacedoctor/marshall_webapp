#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_xmatches_views.py` resource*

:Author:
    David Young

:Date Created:
    October 13, 2015
"""
import sys
import os
import khufu
import re
from marshall_webapp.models.xmatches_views import models_xmatches_views_get
from marshall_webapp.models.xmatches_views.element import models_xmatches_element_views_get


class templates_xmatches_views():
    """
    The worker class for the templates_xmatches_views module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the element id of the resource requested (or false)
    """

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
            "instansiating a new 'templates_xmatches_views' object")

        return None

    def get(self):
        """get the templates_xmatches_views object

        **Return:**
            - ``webpage`` -- the webpage        
        """
        self.log.debug('starting the ``get`` method')

        from marshall_webapp.templates.commonelements.pagetemplates import defaultpagetemplate

        if self.elementId == False:
            xmatches_views = models_xmatches_views_get(
                log=self.log,
                request=self.request
            )
            self.catalogues = xmatches_views.get()

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

        **Return:**
            - ``table``        
        """
        self.log.debug('starting the ``create_table`` method')

        columnsNames = ["Catalogue", "Sources", "Number Rows",
                        "Associated Transients", "Top Rank Associated Transients"]
        columnsNamesDB = ["table_name", "object_types", "number_of_rows",
                          "all_transient_associations", "top_ranked_transient_associations"]

        for row in self.catalogues:
            row["table_name"] = row["table_name"].replace("tcs_cat_", "")
            matchObject = re.finditer(
                r'.*_(v\d.*)',
                row["table_name"],
                flags=0  # re.S
            )
            for match in matchObject:
                replaceMe = match.group(1).replace("_", ".")
                row["table_name"] = row["table_name"].replace(
                    match.group(1), replaceMe)

            row["table_name"] = row["table_name"].replace(
                "_", " ").replace(" final", "")

            for k, v in dict(row).iteritems():
                if isinstance(v, float):
                    row[k] = "{:,.0f}".format(v)

            href = self.request.route_path(
                'xmatches_element_views', elementId=row["table_id"])
            row["all_transient_associations"] = khufu.a(
                content=row["all_transient_associations"],
                href=href
            )

            href = self.request.route_path(
                'xmatches_element_views', elementId=row["table_id"], )
            row["all_transient_associations"] = khufu.a(
                content=row["all_transient_associations"],
                href=href
            )

            href = self.request.route_path('xmatches_element_views', elementId=row[
                "table_id"], _query={'tcsRank': 1})
            row["top_ranked_transient_associations"] = khufu.a(
                content=row["top_ranked_transient_associations"],
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

        # REPLACE COLUMN NAMES WITH DISPLAY NAMES (E.G. FOR WHEN MYSQL COLUMN
        # NAMES ARE USED)
        nd = table.modifyDisplayNameDict
        for o, n in zip(columnsNamesDB, columnsNames):
            nd[o] = n

        table = table.get()

        self.log.debug('completed the ``create_table`` method')
        return table

    # xt-class-method
