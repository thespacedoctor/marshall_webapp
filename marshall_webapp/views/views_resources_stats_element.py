from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_resource_stats
from marshall_webapp.models.stats import models_stats_get
# from marshall_webapp.models.stats import models_stats_put
# from marshall_webapp.models.stats import models_stats_delete
# from marshall_webapp.models.stats import models_stats_push

from dryxPyramid.views.views_base_element import base_element_view
from venusian import lift

@view_defaults(route_name='stats_element', permission="view_users")
@lift()
class views_resources_stats_element(base_element_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "stats"

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        stats = templates_resource_stats(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = stats.get()
        return Response(responseContent)

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        stats = models_stats_get(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return stats.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        stats = models_stats_get(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return stats.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        stats = models_stats_get(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return stats.get()
