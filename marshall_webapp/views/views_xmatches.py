import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_xmatches
from marshall_webapp.models.xmatches.element import models_xmatches_element_delete, models_xmatches_element_put, models_xmatches_element_post

# RESOURCE CONTEXT


@view_defaults(route_name='xmatches', permission="view_users")
class xmatches_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'xmatches'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'xmatches' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'xmatches' resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'xmatches' resource")

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        xmatches = templates_xmatches(
            log=self.log,
            request=self.request
        )
        responseContent = xmatches.get()
        return Response(responseContent)

# RESOURCE ELEMENT


@view_defaults(route_name='xmatches_elements', permission="view_users")
class xmatches_element_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'xmatches' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        xmatches = models_xmatches_element_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = xmatches.delete()
        return Response(responseContent)

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        xmatches = models_xmatches_element_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = xmatches.put()
        return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        xmatches = models_xmatches_element_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        thisResponse = xmatches.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET', permission="view_users", renderer="json", )
    @view_config(request_param="method=get", permission="view_users", renderer="json", )
    def get(self):
        xmatches = templates_xmatches(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return xmatches.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        xmatches = templates_xmatches(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return xmatches.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        xmatches = templates_xmatches(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return xmatches.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        xmatches = templates_xmatches(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return xmatches.get()
