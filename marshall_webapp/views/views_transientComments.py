import logging
import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from ..templates.responses import templates_transientComments
from ..models.transientComments import models_transientComments_post, models_transientComments_put
from ..models.transientComments.element import models_transientComments_element_delete, models_transientComments_element_put

# RESOURCE CONTEXT


@view_defaults(route_name='transientComments')
class transientComments_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transientComments'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transientComments' resource")

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        transientComments = models_transientComments_put(
            log=self.log,
            request=self.request
        )
        responseContent = transientComments.put()
        return Response(responseContent)

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        transientComments = models_transientComments_post(
            log=self.log,
            request=self.request
        )
        thisResponse = transientComments.post()

        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(thisResponse)

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def get(self):
        transientComments = templates_transientComments(
            log=self.log,
            request=self.request
        )
        responseContent = transientComments.get()
        return Response(responseContent)

# RESOURCE ELEMENT


@view_defaults(route_name='transientComments_element')
class transientComments_element_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transientComments'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        transientComments = models_transientComments_element_delete(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transientComments.delete()
        return Response(responseContent)

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        transientComments = models_transientComments_element_put(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transientComments.put()
        return Response(responseContent)

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on 'transientComments' elements")

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def get(self):
        transientComments = templates_transientComments(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transientComments.get()
        return Response(responseContent)
