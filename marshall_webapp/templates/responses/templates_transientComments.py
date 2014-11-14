#!/usr/local/bin/python
# encoding: utf-8
"""
templates_transientComments.py
==============================
:Summary:
    The HTML template module for the `templates_transientComments.py` resource

:Author:
    David Young

:Date Created:
    October 9, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete review and cleanup this `templates_transientComments.py` module
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from ...models.transientComments import models_transientComments_get
from ...models.transientComments.element import models_transientComments_element_get


class templates_transientComments():

    """
    The worker class for the templates_transientComments module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request

    **Todo**
        - @review: when complete, clean templates_transientComments class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        request,
        elementId=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'templates_transientComments' object")

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the templates_transientComments object

        **Return:**
            - ``responseContent`` -- the response

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        templates_transientComments = None

        transientComments = models_transientComments_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        responseContent = transientComments.get()

        self.log.info('completed the ``get`` method')
        return responseContent
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
