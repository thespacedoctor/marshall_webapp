from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from marshall_webapp.templates.responses import templates_transients_comments
from marshall_webapp.models.transients_comments import models_transients_comments_get
from marshall_webapp.models.transients_comments.element import models_transients_element_comments_delete, models_transients_element_comments_put, models_transients_element_comments_post
from dryxPyramid.views.views_base import base_view
from venusian import lift

# RESOURCE CONTEXT


@view_defaults(route_name='transients_comments',  permission="view_users")
@lift()
class views_transients_comments(base_view):

    def __init__(self, request):
        super().__init__(request)
        self.resourceName = "transients_comments"

    @view_config(request_method='GET', renderer="json", permission="view_users")
    @view_config(request_param="method=get", renderer="json",  permission="view_users")
    def get(self):
        transients_comments = models_transients_comments_get(
            log=self.log,
            request=self.request
        )
        return transients_comments.get()

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transients_comments = models_transients_comments_get(
            log=self.log,
            request=self.request
        )
        return transients_comments.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transients_comments = models_transients_comments_get(
            log=self.log,
            request=self.request
        )
        return transients_comments.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transients_comments = models_transients_comments_get(
            log=self.log,
            request=self.request
        )
        return transients_comments.get()

# RESOURCE ELEMENT


@view_defaults(route_name='transients_element_comments', permission="view_users")
class transients_element_comments_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transients_comments'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        transients_comments = models_transients_element_comments_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_comments.delete()
        return Response(responseContent)

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        transients_comments = models_transients_element_comments_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_comments.put()
        return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        transients_comments = models_transients_element_comments_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        thisResponse = transients_comments.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients_comments = templates_transients_comments(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients_comments.get()
        return Response(responseContent)
