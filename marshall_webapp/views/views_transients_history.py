# @review: tidy this module when complete

from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from marshall_webapp.templates.responses import templates_transients_history
from marshall_webapp.models.transients_history.element import models_transients_element_history_delete, models_transients_element_history_put, models_transients_element_history_post
from dryxPyramid.views.views_base import base_view
from venusian import lift

# RESOURCE ELEMENT


@view_defaults(route_name='transients_history',  permission="view_users")
@lift()
class views_transients_history(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "transients_history"

    @view_config(request_method='DELETE', permission="superuser")
    @view_config(request_param="method=delete", permission="superuser")
    def delete(self):
        transients_history = models_transients_element_history_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_history.delete()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='PUT', permission="superuser")
    @view_config(request_param="method=put", permission="superuser")
    def put(self):
        transients_history = models_transients_element_history_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_history.put()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        transients_history = models_transients_element_history_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_history.post()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients_history = templates_transients_history(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_history.get()
        return Response(responseContent)
