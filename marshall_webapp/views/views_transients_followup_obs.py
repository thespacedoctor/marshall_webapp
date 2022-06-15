from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from ..templates.responses import templates_transients_followup_obs
from ..models.transients_followup_obs.element import models_transients_element_followup_obs_delete, models_transients_element_followup_obs_put, models_transients_element_followup_obs_post

# RESOURCE CONTEXT


@view_defaults(route_name='transients_followup_obs', permission="view_users")
class transients_followup_obs_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'transients_followup_obs'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(404, body_template="The DELETE method is not enabled on the 'transients_followup_obs' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        return exc.exception_response(404, body_template="The PUT method is not enabled on the 'transients_followup_obs' resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(404, body_template="The POST method is not enabled on the 'transients_followup_obs' resource")

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients_followup_obs = templates_transients_followup_obs(
            log=self.log,
            request=self.request
        )
        responseContent = transients_followup_obs.get()
        return Response(responseContent)

# RESOURCE ELEMENT


@view_defaults(route_name='transients_element_followup_obs', permission="view_users")
class transients_element_followup_obs_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'transients_followup_obs' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        transients_followup_obs = models_transients_element_followup_obs_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_followup_obs.delete()
        return Response(responseContent)

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        transients_followup_obs = models_transients_element_followup_obs_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_followup_obs.put()
        return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        transients_followup_obs = models_transients_element_followup_obs_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        thisResponse = transients_followup_obs.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET', permission="view_users", renderer="json", )
    @view_config(request_param="method=get", permission="view_users", renderer="json", )
    def get(self):
        transients_followup_obs = templates_transients_followup_obs(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_followup_obs.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transients_followup_obs = templates_transients_followup_obs(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_followup_obs.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transients_followup_obs = templates_transients_followup_obs(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_followup_obs.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transients_followup_obs = templates_transients_followup_obs(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_followup_obs.get()
