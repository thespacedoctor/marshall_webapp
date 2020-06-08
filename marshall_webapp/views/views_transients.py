from builtins import object
import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from marshall_webapp.templates.responses import templates_transients
from marshall_webapp.models.transients import models_transients_post, models_transients_put, models_transients_get
from marshall_webapp.models.transients.element import models_transients_element_delete, models_transients_element_put, models_transients_element_post


# @view_config(route_name='index', request_method='GET', permission="view_users")
# def index(request):
#     href = request.route_path('transients')
#     return HTTPFound(location=href)

# @review: clean up this view callable when complete


@view_defaults(route_name='index', permission="view_users")
class index_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'index_view'' view")

    @view_config(request_method='POST', permission="view_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        href = self.request.route_path('transients')
        # REDIRECTS TO /transients
        return HTTPFound(location=href)

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        href = self.request.route_path('transients')
        # REDIRECTS TO /transients
        return HTTPFound(location=href)


@view_defaults(route_name='transients', permission="view_users")
class transients_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'transients' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transients' resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        # PLACEHOLDER METHOD - ADD LOGIC WHEN NEEDED ..
        transients = models_transients_put(
            log=self.log,
            request=self.request
        )
        responseContent = transients.put()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        # ADD A NEW TRANSIENT TO THE MARSHALL - VIA CREATE NEW TICKET BUTTON
        transients = models_transients_post(
            log=self.log,
            request=self.request
        )
        responseContent, redirectURL = transients.post()
        if len(redirectURL):
            return HTTPFound(location=redirectURL)
        else:
            return Response(responseContent)

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request
        )
        return transientData.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request
        )
        return transientData.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request
        )
        return transientData.get()

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get_html(self):
        transientData = templates_transients(
            log=self.log,
            request=self.request
        )
        htmlContent = transientData.get()
        return Response(htmlContent)


@view_defaults(route_name='transients_element', permission="view_users")
class transients_element_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'single_transient'' view")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        transients = models_transients_element_put(
            log=self.log,
            request=self.request
        )
        responseContent = transients.put()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transients' element resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        transients = models_transients_element_post(
            log=self.log,
            request=self.request
        )
        responseContent = transients.post()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients = templates_transients(
            log=self.log,
            request=self.request,
            elementId=self.request.matchdict["elementId"]
        )
        responseContent = transients.get()
        return Response(responseContent)


@view_defaults(route_name='transients_search', permission="view_users")
class transientsSearchView(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'views_transients_search'' view")

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        transients = templates_transients(
            log=self.log,
            request=self.request,
            search=True
        )
        responseContent = transients.get()
        return Response(responseContent)

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request,
            search=True
        )
        return transientData.get()

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request,
            search=True
        )
        return transientData.get()

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        transientData = models_transients_get(
            log=self.log,
            request=self.request,
            search=True
        )
        return transientData.get()

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'transients' search resource")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on the 'transients' search resource")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on the 'transients' search resource")
