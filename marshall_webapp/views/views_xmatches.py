from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_xmatches
from marshall_webapp.models.xmatches.element import models_xmatches_element_delete, models_xmatches_element_put, models_xmatches_element_post
from dryxPyramid.views.views_base import base_view, base_element_view
from venusian import lift


@view_defaults(route_name='xmatches',  permission="view_users")
@lift()
class views_xmatches(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "xmatches"

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        xmatches = templates_xmatches(
            log=self.log,
            request=self.request
        )
        responseContent = xmatches.get()
        return Response(responseContent)
