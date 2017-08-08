import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from ..templates.responses import templates_calendars


@view_defaults(route_name='calendars',  permission="view_users")
class views_calendarsView(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'calendars'' view")

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get_html(self):
        calendar = templates_calendars(
            log=self.log,
            request=self.request
        )
        htmlContent = calendar.get()
        return Response(str(htmlContent))

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'calendars' resource")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'calendars' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'calendars' resource")
