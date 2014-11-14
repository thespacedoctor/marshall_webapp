import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from ..templates.responses import templates_transient_comments
from ..models.transient_comments import models_transient_comments_post, models_transient_comments_put
from ..models.transient_comments.element import models_transients_element_comments_delete, models_transients_element_comments_put, models_transients_element_comments_post

# RESOURCE CONTEXT


@view_defaults(route_name='transient_comments')
class transient_comments_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transient_comments'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transient_comments' resource")

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'transient_comments' resource")

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'transient_comments' resource")

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def get(self):
        transient_comments = templates_transient_comments(
            log=self.log,
            request=self.request
        )
        responseContent = transient_comments.get()
        return Response(responseContent)

# RESOURCE ELEMENT


@view_defaults(route_name='transients_element_comments')
class transients_element_comments_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transient_comments'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        transient_comments = models_transients_element_comments_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transient_comments.delete()
        return Response(responseContent)

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        transient_comments = models_transients_element_comments_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transient_comments.put()
        return Response(responseContent)

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        transient_comments = models_transients_element_comments_post(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        thisResponse = transient_comments.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def get(self):
        transient_comments = templates_transient_comments(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transient_comments.get()
        return Response(responseContent)
