import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from ..templates.responses import templates_xmatches_catalogues
from ..models.xmatches_catalogues.element import models_xmatches_element_catalogues_get, models_xmatches_element_catalogues_delete, models_xmatches_element_catalogues_put, models_xmatches_element_catalogues_post

# RESOURCE CONTEXT


@view_defaults(route_name='xmatches_catalogues', permission="view_users")
class xmatches_catalogues_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'xmatches_catalogues'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'xmatches_catalogues' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'xmatches_catalogues' resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'xmatches_catalogues' resource")

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):

        xmatches_catalogues = templates_xmatches_catalogues(
            log=self.log,
            request=self.request
        )
        responseContent = xmatches_catalogues.get()
        return Response(responseContent)

# RESOURCE ELEMENT


@view_defaults(route_name='xmatches_element_catalogues', permission="view_users")
class xmatches_element_catalogues_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'xmatches_catalogues' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        xmatches_catalogues = models_xmatches_element_catalogues_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = xmatches_catalogues.delete()
        return Response(responseContent)

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        xmatches_catalogues = models_xmatches_element_catalogues_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = xmatches_catalogues.put()
        return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        xmatches_catalogues = models_xmatches_element_catalogues_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        thisResponse = xmatches_catalogues.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        xmatches_catalogues = templates_xmatches_catalogues(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return xmatches_catalogues.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        xmatches_catalogues = models_xmatches_element_catalogues_get(
            log=self.log,
            request=self.request,
            tcsCatalogueId=self.request.matchdict["elementId"]
        )
        return xmatches_catalogues.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        xmatches_catalogues = models_xmatches_element_catalogues_get(
            log=self.log,
            request=self.request,
            tcsCatalogueId=self.request.matchdict["elementId"]
        )
        return xmatches_catalogues.get()

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        xmatches_catalogues = templates_xmatches_catalogues(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return Response(unicode(xmatches_catalogues.get()))
