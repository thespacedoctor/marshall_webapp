import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from ..templates.responses import templates_transientLightcurves
from ..models.transientLightcurves import models_transientLightcurves_post, models_transientLightcurves_put

# RESOURCE CONTEXT


@view_defaults(route_name='transientLightcurves')
class transientLightcurves_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transientLightcurves'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transientLightcurves' resource")

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'transientLightcurves' resource")

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'transientLightcurves' resource")

    @view_config(request_method='GET', renderer="json")
    @view_config(request_param="method=get", renderer="json")
    def get(self):
        transientLightcurves = templates_transientLightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transientLightcurves.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json")
    @view_config(request_param=["method=get", "format=json"], renderer="json")
    def get_json(self):
        transientLightcurves = templates_transientLightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transientLightcurves.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv")
    def get_csv(self):
        transientLightcurves = templates_transientLightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        # return {u"nice": u"nice"}
        return transientLightcurves.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table")
    def get_plain_table(self):
        transientLightcurves = templates_transientLightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        # return {u"nice": u"nice"}
        return transientLightcurves.get()
