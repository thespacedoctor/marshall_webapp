from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from marshall_webapp.templates.responses import templates_resources_transients
from marshall_webapp.models.transients.element import models_transients_element_put, models_transients_element_post
from dryxPyramid.views.views_base_element import base_element_view
from venusian import lift


@view_defaults(route_name='transients_element', permission="view_users")
@lift()
class views_resources_transients_element(base_element_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "transients"

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        transients = models_transients_element_put(
            log=self.log,
            request=self.request
        )
        responseContent = transients.put()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        transients = models_transients_element_post(
            log=self.log,
            request=self.request
        )
        responseContent = transients.post()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients = templates_resources_transients(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients.get()
        return Response(responseContent)
