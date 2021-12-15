from builtins import str
from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from marshall_webapp.templates.responses import templates_transients_obs
from marshall_webapp.models.transients_obs.element import models_transients_element_obs_get
from dryxPyramid.views.views_base import base_view
from venusian import lift

# RESOURCE ELEMENT

@view_defaults(route_name='transients_element_obs',  permission="view_users")
@lift()
class views_transients_obs(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "transients_element_obs"

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients_obs = templates_transients_obs(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        filename, transients_obs_text = transients_obs.get()
        response = Response(str(transients_obs_text))
        response.content_type = 'text/obx'
        response.content_disposition = "attachment; filename=%(filename)s" % locals(
        )

        return response
