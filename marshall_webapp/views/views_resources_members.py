from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_resource_members
from marshall_webapp.models.members import models_members_get
from dryxPyramid.views.views_base import base_view
from venusian import lift


@view_defaults(route_name='members',  permission="view_users")
@lift()
class views_resources_members(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "members"

    # HTML WEBPAGES
    @view_config(request_method='GET', request_param="format=html", permission="view_users")
    @view_config(request_param=["method=get", "format=html"], permission="view_users")
    def get_html(self):
        members = templates_resource_members(
            log=self.log,
            request=self.request
        )
        responseContent = members.get()
        return Response(responseContent)

    # API RENDERINGS
    @view_config(request_method='GET', renderer="json", permission="view_users")
    @view_config(request_param=["method=get"], renderer="json", permission="view_users")
    def get(self):
        members = models_members_get(
            log=self.log,
            request=self.request
        )
        return members.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        members = models_members_get(
            log=self.log,
            request=self.request
        )
        return members.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        members = models_members_get(
            log=self.log,
            request=self.request
        )
        return members.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        members = models_members_get(
            log=self.log,
            request=self.request
        )
        return members.get()
