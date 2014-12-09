#!/usr/local/bin/python
# encoding: utf-8
"""
templates_calendars.py
======================
:Summary:
    The HTML template module for the `templates_calendars.py` resource

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


class templates_calendars():

    """
    The worker class for the templates_calendars module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        request
    ):
        self.log = log
        log.debug("instansiating a new 'templates_calendars' object")
        self.request = request
        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the templates_calendars object

        **Return:**
            - ``webpage`` -- the webpage for the calendar

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        # the google calendar embed code
        maincontent = """
            <iframe src="https://www.google.com/calendar/embed?title=PESSTO%20NTT%20and%20Supplementary%20Telescope%20Time&amp;height=600&amp;wkst=1&amp;bgcolor=%23cccccc&amp;src=pessto.org_2ifj20jf8dln05cfpls2tjds4k%40group.calendar.google.com&amp;color=%232F6309&amp;src=pessto.org_b855vuk2444lqcot2d2tiakst8%40group.calendar.google.com&amp;color=%23711616&amp;ctz=Europe%2FLondon" style=" border:solid 1px #777 " width="800" height="600" frameborder="0" scrolling="no"></iframe>
        """

        src = request.static_url(
            'marshall_webapp:static/docs/pessto_calendar_tutorial.pdf')
        info = khufu.p(
            content='For instructions on adding supplementary telescope time to this calendar <a href="%(src)s">see here</a>' % locals(
            ),
            htmlId="calendarInfo",
            lead=True,
            textAlign="left",  # [ left | center | right ]
            color=False,  # [ muted | warning | info | error | success ]
        )
        maincontent = """%(maincontent)s %(info)s """ % locals()

        webpage = defaultpagetemplate(
            log=self.log,
            request=self.request,
            bodyId=False,
            pageTitle="PESSTO Marshall",
            topNavBar=False,
            sideBar=False,
            mainContent=maincontent,
            relativePathFromDocRoot=False,
            thisPageName="PESSTO Observing Calendar"
        )

        self.log.info('completed the ``get`` method')
        return webpage

    # xt-class-method
