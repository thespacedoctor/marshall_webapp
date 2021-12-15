#!/usr/bin/env python
# encoding: utf-8
"""
*The data model module for the `transients_comments_element_post` resource*

:Author:
    David Young
"""
from builtins import object
import sys
import os
import khufu

class models_transients_comments_element_post(object):
    """
    *The worker class for the models_transients_comments_element_post module*

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element id requests (or False)
    - ``search`` -- is this a search request (boolean)
    

    **Usage**

    

    ```eval_rst
    .. todo::

        - add usage info
        - create a sublime snippet for usage
        - add a tutorial about ``models_transients_comments_element_post`` to documentation
        - create a blog post about what ``models_transients_comments_element_post`` doess
    ```

    ```python
    usage code 
    ```
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        elementId=False,
        search=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        self.search = search
        self.qs = dict(request.params)  # the query string
        # the query string defaults
        self.defaultQs = {}
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'models_transients_comments_element_post' object")

        # Variable Data Atrributes

        # Initial Actions
        self._set_default_parameters()

        return None

    # Method Attributes
    def post(self):
        """
        *execute the post method on the models_transients_comments_element_post object*

        **Return**

        - ``responseContent`` -- the reponse to send to the browser
        
        """
        self.log.debug('starting the ``post`` method')

        elementId = self.elementId

        responseContent = "Response from <code>" + __name__ + "</code><BR><BR>"
        if elementId:
            responseContent = "%(responseContent)sThe element selected was </code>%(elementId)s</code>" % locals(
            )
        else:
            responseContent = "%(responseContent)sResource Context selected (no element)" % locals(
            )

        self.log.debug('completed the ``post`` method')
        return responseContent

    def _set_default_parameters(
            self):
        """
        *set default parameters*

        **Key Arguments**

        - 
        

        **Return**

        - None
        
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        for k, v in list(self.defaultQs.items()):
            if k not in self.qs:
                self.qs[k] = v

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
