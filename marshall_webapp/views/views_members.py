from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_members
from marshall_webapp.models.members.element import models_members_element_delete, models_members_element_put, models_members_element_post
from dryxPyramid.views.views_base import base_view, base_element_view
from venusian import lift

# RESOURCE CONTEXT


@view_defaults(route_name='members',  permission="view_users")
@lift()
class views_members(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "members"

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        members = templates_members(
            log=self.log,
            request=self.request
        )
        responseContent = members.get()
        return Response(responseContent)
