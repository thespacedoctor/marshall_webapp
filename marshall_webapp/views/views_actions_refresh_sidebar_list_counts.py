import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from ..models.actions import models_refresh_sidebar_list_counts

# RESOURCE CONTEXT


@view_defaults(route_name='refresh_sidebar_list_counts')
class refresh_sidebar_list_counts_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'refresh_sidebar_list_counts'' view")

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        refresh_sidebar_list_counts = models_refresh_sidebar_list_counts(
            log=self.log,
            request=self.request
        )
        responseContent = refresh_sidebar_list_counts.put()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def put(self):
        return exc.exception_response(405, body_template="The GET method is not allowed on the 'refresh_sidebar_list_counts' action")

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def put(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'refresh_sidebar_list_counts' action")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def put(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'refresh_sidebar_list_counts' action")
