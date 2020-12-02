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


@view_defaults(route_name='transients',  permission="view_users")
@lift()
class views_resources_transients(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "transients"

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        # ADD A NEW TRANSIENT TO THE MARSHALL - VIA CREATE NEW TICKET BUTTON
        transients = models_transients_post(
            log=self.log,
            request=self.request
        )
        responseContent, redirectURL = transients.post()
        if len(redirectURL):
            return HTTPFound(location=redirectURL)
        else:
            return Response(responseContent)

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request
        )
        return transientData.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request
        )
        return transientData.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request
        )
        return transientData.get()

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transientData = templates_resources_transients(
            log=self.log,
            request=self.request
        )
        htmlContent = transientData.get()
        return Response(htmlContent)
