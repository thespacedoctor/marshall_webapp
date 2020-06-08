from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from marshall_webapp.templates.responses import templates_transients_lightcurves
from marshall_webapp.models.transients_lightcurves import models_transients_lightcurves_post, models_transients_lightcurves_put

# RESOURCE CONTEXT


@view_defaults(route_name='transients_lightcurves', permission="view_users")
class transients_lightcurves_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'transients_lightcurves'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transients_lightcurves' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'transients_lightcurves' resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'transients_lightcurves' resource")

    @view_config(request_method='GET', renderer="json", permission="view_users")
    @view_config(request_param="method=get", renderer="json", permission="view_users")
    def get(self):
        return exc.exception_response(405, body_template="The GET method is not allowed on the 'transients_lightcurves' resource")


@view_defaults(route_name='transients_element_lightcurves', permission="view_users")
class transients_elements_lightcurve_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'transients_element_lightcurves'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transients_element_lightcurves' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'transients_element_lightcurves' resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'transients_element_lightcurves' resource")

    @view_config(request_method='GET', renderer="json", permission="view_users")
    @view_config(request_param="method=get", renderer="json", permission="view_users")
    def get(self):
        transients_lightcurves = templates_transients_lightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_lightcurves.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transients_lightcurves = templates_transients_lightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_lightcurves.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transients_lightcurves = templates_transients_lightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_lightcurves.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transients_lightcurves = templates_transients_lightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_lightcurves.get()

    @view_config(request_method='GET', request_param="format=d3", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=d3"], renderer="json", permission="view_users")
    def get_d3(self):
        transients_lightcurves = templates_transients_lightcurves(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"],
            format="d3"
        )
        return transients_lightcurves.get()
