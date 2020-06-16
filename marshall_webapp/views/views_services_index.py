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


@view_defaults(route_name='index', permission="view_users")
class views_services_index(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'index_view'' view")

    @view_config(request_method='POST', permission="view_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        href = self.request.route_path('transients')
        # REDIRECTS TO /transients
        return HTTPFound(location=href)

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        href = self.request.route_path('transients')
        # REDIRECTS TO /transients
        return HTTPFound(location=href)
