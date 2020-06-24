#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_services_calendars.py` resource*

:Author:
    David Young
"""
from builtins import object
import sys
import os
import khufu
from marshall_webapp.templates.commonelements.pagetemplates import defaultpagetemplate

class templates_services_calendars(object):
    """
    The worker class for the templates_services_calendars module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    
    """

    def __init__(
        self,
        log,
        request
    ):
        self.log = log
        log.debug("instansiating a new 'templates_services_calendars' object")
        self.request = request
        # xt-self-arg-tmpx

        return None

    def get(self):
        """get the templates_services_calendars object

        **Return**

        - ``webpage`` -- the webpage for the calendar
        
        """
        self.log.debug('starting the ``get`` method')

        # the google calendar embed code
        maincontent = """
            <iframe src="https://www.google.com/calendar/embed?title=PESSTO%20NTT%20and%20Supplementary%20Telescope%20Time&amp;height=600&amp;wkst=1&amp;bgcolor=%23cccccc&amp;src=pessto.org_2ifj20jf8dln05cfpls2tjds4k%40group.calendar.google.com&amp;color=%232F6309&amp;src=pessto.org_b855vuk2444lqcot2d2tiakst8%40group.calendar.google.com&amp;color=%23711616&amp;ctz=Europe%2FLondon" style=" border:solid 1px #777 " width="800" height="600" frameborder="0" scrolling="no"></iframe>
        """

        src = self.request.static_path(
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
            pageTitle="ePESSTO+ Marshall",
            topNavBar=False,
            sideBar=False,
            mainContent=maincontent,
            relativePathFromDocRoot=False,
            thisPageName="PESSTO Observing Calendar"
        )

        self.log.debug('completed the ``get`` method')
        return webpage

    # xt-class-method
