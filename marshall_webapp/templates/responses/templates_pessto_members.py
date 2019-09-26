#!/usr/local/bin/python
# encoding: utf-8
"""
*Template for the pessto_members view*

:Author:
    David Young

:Date Created:
    January 21, 2016
"""
import sys
import os
from marshall_webapp.models.pessto_members import models_pessto_members_get
from pyramid.path import AssetResolver
import khufu


class templates_pessto_members():
    """
    The worker class for the templates_pessto_members module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid/WebObs request object
        - ``elementId`` -- the specific element requested (or False)
        - ``search`` -- is this a search? (boolean)
    """

    def __init__(
        self,
        log,
        request,
        elementId=False,
        search=False
    ):
        self.log = log
        self.request = request
        log.debug("instansiating a new 'templates_pessto_members' object")
        self.elementId = elementId
        self.search = search
        # xt-self-arg-tmpx

        members = models_pessto_members_get(
            log=self.log,
            request=self.request,
        )
        self.pesstoMembers = members.get(
        )

        return None

    def get(self):
        """get the templates_pessto_members object

        **Return:**
            - ``webpage`` -- the webapge HTML
        """
        self.log.debug('starting the ``get`` method')

        maincontent = self._get_members_table()
        from marshall_webapp.templates.commonelements.pagetemplates import defaultpagetemplate

        webpage = defaultpagetemplate(
            log=self.log,
            request=self.request,
            bodyId=False,
            pageTitle="PESSTO Marshall",
            topNavBar=False,
            sideBar=False,
            mainContent="<BR><BR>" + maincontent,
            relativePathFromDocRoot=False,
            thisPageName="PESSTO Members"
        )

        self.log.debug('completed the ``get`` method')
        return webpage

    def _get_members_table(self):
        """get members table
        """
        self.log.debug('starting the ``_get_members_table`` method')

        for row in self.pesstoMembers:
            for k, v in row.iteritems():
                row[k] = v.title()

        total = len(self.pesstoMembers)

        # ASSOICATE THE CORRECT COLUMN NAME TO MYSQL DATABASE COLUMN NAME
        tableColumnNames = {
            "firstname": "First Name",
            "secondname": "Second Name"
        }

        # A LIST OF NAMES FOR TABLE AND CSV VIEWS
        tableColumns = [
            "firstname",
            "secondname",
        ]

        # CREATE THE SORTABLE TABLES OF OBJECTS
        table = khufu.tables.sortable_table.sortable_table(
            currentPageUrl=self.request.path_qs,
            columnsToDisplay=tableColumns,
            tableRowsDictionary=self.pesstoMembers,
            log=self.log,
            defaultSort="secondname"
        )
        nd = table.modifyDisplayNameDict
        nd["firstname"] = "First Name"
        nd["secondname"] = "Second Name"

        # table.searchKeyAndColumn = ("search", "plainName")

        table = table.get()

        # ADD TEXT COLOR
        text = khufu.coloredText(
            text="There are currently %(total)s PESSTO Members signed up to use the Marshall<BR><BR>" % locals(
            ),
            color="#657b83",
            size=5,  # 1-10
            pull="right",  # "left" | "right",
            addBackgroundColor=False
        )

        object_table = khufu.grid_column(
            span=6,  # 1-12
            offset=0,  # 1-12
            content=text + table,
            htmlId="object_table",
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        self.log.debug('completed the ``_get_members_table`` method')
        return object_table

    # xt-class-method
