from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.models.transients_akas import models_transients_akas_get
from dryxPyramid.views.views_base import base_view
from venusian import lift


@view_defaults(route_name='transients_akas',  permission="view_users")
@lift()
class views_resources_transients_akas(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "transients_akas"

    # xpyr-view-resource-get-html
     # API RENDERINGS
    @view_config(request_method='GET', renderer="json", permission="view_users")
    @view_config(request_param=["method=get"], renderer="json", permission="view_users")
    def get(self):
        transients_akas = models_transients_akas_get(
            log=self.log,
            request=self.request
        )
        return transients_akas.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transients_akas = models_transients_akas_get(
            log=self.log,
            request=self.request
        )
        return transients_akas.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transients_akas = models_transients_akas_get(
            log=self.log,
            request=self.request
        )
        return transients_akas.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transients_akas = models_transients_akas_get(
            log=self.log,
            request=self.request
        )
        return transients_akas.get()
