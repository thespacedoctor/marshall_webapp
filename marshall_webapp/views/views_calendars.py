import logging
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from ..templates.responses import templates_calendars


@view_defaults(route_name='calendars')
class views_calendarsView(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'calendars'' view")

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def get_html(self):
        calendar = templates_calendars(
            log=self.log,
            request=self.request
        )
        htmlContent = calendar.get()
        return Response(str(htmlContent))

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        return Response("""{self.request.method} request for the `{__name__}` module</body>""".format(**dict(globals(), **locals())))

    @view_config(request_method='DELETE', permission="delete")
    @view_config(request_param="method=delete", permission="delete")
    def delete(self):
        return Response("""{self.request.method} request for the `{__name__}` module</body>""".format(**dict(globals(), **locals())))

    @view_config(request_method='PUT', permission="edit")
    @view_config(request_param="method=put", permission="edit")
    def delete(self):
        return Response("""{self.request.method} request for the `{__name__}` module</body>""".format(**dict(globals(), **locals())))
