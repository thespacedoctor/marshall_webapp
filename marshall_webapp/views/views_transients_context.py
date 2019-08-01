import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_transients_context
from marshall_webapp.models.transients_context.element import models_transients_element_context_delete, models_transients_element_context_put, models_transients_element_context_post

# RESOURCE CONTEXT


@view_defaults(route_name='transients_context', permission="view_users")
class transients_context_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transients_context'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transients_context' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'transients_context' resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'transients_context' resource")

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients_context = templates_transients_context(
            log=self.log,
            request=self.request
        )
        responseContent = transients_context.get()
        return Response(responseContent)

# RESOURCE ELEMENT


@view_defaults(route_name='transients_element_context', permission="view_users")
class transients_element_context_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transients_context' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        transients_context = models_transients_element_context_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_context.delete()
        return Response(responseContent)

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        transients_context = models_transients_element_context_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_context.put()
        return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        transients_context = models_transients_element_context_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        thisResponse = transients_context.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET', permission="view_users", renderer="json", )
    @view_config(request_param="method=get", permission="view_users", renderer="json", )
    def get(self):
        transients_context = templates_transients_context(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_context.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transients_context = templates_transients_context(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_context.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transients_context = templates_transients_context(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_context.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transients_context = templates_transients_context(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return transients_context.get()
