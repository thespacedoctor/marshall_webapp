from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_resource_stats
from marshall_webapp.models.stats import models_stats_get
from dryxPyramid.views.views_base import base_view
from venusian import lift


@view_defaults(route_name='stats',  permission="view_users")
@lift()
class views_resources_stats(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "stats"

    # HTML WEBPAGES
    @view_config(request_method='GET', request_param="format=html", permission="view_users")
    @view_config(request_param=["method=get", "format=html"], permission="view_users")
    def get_html(self):
        stats = templates_resource_stats(
            log=self.log,
            request=self.request
        )
        responseContent = stats.get()
        return Response(responseContent)

    # xpyr-pyramid-resource-view-extra-api-renderings
