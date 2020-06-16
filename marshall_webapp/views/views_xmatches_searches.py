from builtins import str
from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_xmatches_searches
from marshall_webapp.models.xmatches_searches.element import models_xmatches_element_searches_get, models_xmatches_element_searches_delete, models_xmatches_element_searches_put, models_xmatches_element_searches_post
from dryxPyramid.views.views_base import base_view
from venusian import lift

# RESOURCE CONTEXT


@view_defaults(route_name='xmatches_searches',  permission="view_users")
@lift()
class views_xmatches_searches(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "xmatches_searches"

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):

        xmatches_searches = templates_xmatches_searches(
            log=self.log,
            request=self.request
        )
        responseContent = xmatches_searches.get()
        return Response(responseContent)

# RESOURCE ELEMENT


@view_defaults(route_name='xmatches_element_searches', permission="view_users")
class xmatches_element_searches_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug(
            "instantiating a new 'xmatches_searches' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        xmatches_searches = models_xmatches_element_searches_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = xmatches_searches.delete()
        return Response(responseContent)

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        xmatches_searches = models_xmatches_element_searches_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = xmatches_searches.put()
        return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        xmatches_searches = models_xmatches_element_searches_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        thisResponse = xmatches_searches.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        xmatches_searches = templates_xmatches_searches(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return xmatches_searches.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        xmatches_searches = models_xmatches_element_searches_get(
            log=self.log,
            request=self.request,
            tcsCatalogueId=self.request.matchdict["elementId"]
        )
        return xmatches_searches.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        xmatches_searches = templates_xmatches_searches(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return xmatches_searches.get()

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        xmatches_searches = templates_xmatches_searches(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        return Response(str(xmatches_searches.get()))
