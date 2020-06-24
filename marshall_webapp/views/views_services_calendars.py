from builtins import str
from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from marshall_webapp.templates.responses import templates_services_calendars
from dryxPyramid.views.views_base import base_view
from venusian import lift

@view_defaults(route_name='calendars',  permission="view_users")
@lift()
class views_services_calendars(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "calendars"

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        calendar = templates_services_calendars(
            log=self.log,
            request=self.request
        )
        htmlContent = calendar.get()
        return Response(str(htmlContent))
