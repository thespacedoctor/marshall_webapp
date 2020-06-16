from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from marshall_webapp.templates.responses import templates_resources_transients
from marshall_webapp.models.transients import models_transients_post, models_transients_get
from marshall_webapp.models.transients.element import models_transients_element_put, models_transients_element_post
from dryxPyramid.views.views_base import base_view
from venusian import lift

# NOTE THIS VIEW IS A PROXY FOR THE TRANSIENT ROUTE - NO NEED FOR A
# SEPARATE UNIT TEST


@view_defaults(route_name='transients_search', permission="view_users")
@lift()
class views_services_search(object):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "transients_search"

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients = templates_resources_transients(
            log=self.log,
            request=self.request,
            search=True
        )
        responseContent = transients.get()
        return Response(responseContent)

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request,
            search=True
        )
        return transientData.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request,
            search=True
        )
        return transientData.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request,
            search=True
        )
        return transientData.get()
