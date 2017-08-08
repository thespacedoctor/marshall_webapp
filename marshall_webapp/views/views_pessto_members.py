import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from ..templates.responses import templates_pessto_members
from ..models.pessto_members.element import models_pessto_members_element_delete, models_pessto_members_element_put, models_pessto_members_element_post

# RESOURCE CONTEXT


@view_defaults(route_name='pessto_members', permission="view_users")
class pessto_members_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'pessto_members'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'pessto_members' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'pessto_members' resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'pessto_members' resource")

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        pessto_members = templates_pessto_members(
            log=self.log,
            request=self.request
        )
        responseContent = pessto_members.get()
        return Response(responseContent)

# RESOURCE ELEMENT


@view_defaults(route_name='pessto_members_elements', permission="view_users")
class pessto_members_element_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'pessto_members' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        pessto_members = models_pessto_members_element_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = pessto_members.delete()
        return Response(responseContent)

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        pessto_members = models_pessto_members_element_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = pessto_members.put()
        return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        pessto_members = models_pessto_members_element_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        thisResponse = pessto_members.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET', permission="view_users", renderer="json", )
    @view_config(request_param="method=get", permission="view_users", renderer="json", )
    def get(self):
        pessto_members = templates_pessto_members(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return pessto_members.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        pessto_members = templates_pessto_members(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return pessto_members.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        pessto_members = templates_pessto_members(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return pessto_members.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        pessto_members = templates_pessto_members(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return pessto_members.get()
