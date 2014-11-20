import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from ..templates.responses import templates_transients_obs
from ..models.transients_obs.element import models_transients_element_obs_get

# RESOURCE ELEMENT


@view_defaults(route_name='transients_element_obs')
class transients_element_obs_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transients_obs'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on 'transients_obs' elements")

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on 'transients_obs' elements")

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on 'transients_obs' elements")

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
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

        print filename

        return response
