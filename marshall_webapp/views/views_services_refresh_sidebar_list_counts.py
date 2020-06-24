from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from marshall_webapp.services import services_refresh_sidebar_list_counts
from dryxPyramid.views.views_base import base_view
from venusian import lift

# RESOURCE CONTEXT

@view_defaults(route_name='refresh_sidebar_list_counts',  permission="view_users")
@lift()
class views_services_refresh_sidebar_list_counts(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "refresh_sidebar_list_counts"

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        refresh_sidebar_list_counts = services_refresh_sidebar_list_counts(
            log=self.log,
            request=self.request
        )
        responseContent = refresh_sidebar_list_counts.put()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)
