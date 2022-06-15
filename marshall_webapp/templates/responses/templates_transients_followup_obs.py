#!/usr/bin/env python
# encoding: utf-8
"""
*The HTML template module for the `templates_transients_followup_obs.py` resource*

:Author:
    David Young

:Date Created:
    June 15, 2022
"""
################# GLOBAL IMPORTS ####################
from builtins import object
import sys
import os
import khufu
from ...models.transients_followup_obs import models_transients_followup_obs_get
from ...models.transients_followup_obs.element import models_transients_element_followup_obs_get


class templates_transients_followup_obs(object):

    """
    *The worker class for the templates_transients_followup_obs module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the element id of the resource requested (or false)

    ```eval_rst
    .. todo::

        - add usage info
        - create a sublime snippet for usage
        - add a tutorial about ``templates_transients_followup_obs`` to documentation
        - create a blog post about what ``templates_transients_followup_obs`` does
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
        format=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        # xt-self-arg-tmpx

        log.debug(
            "instansiating a new 'templates_transients_followup_obs' object")

        # Initial Actions

        return None

    # Method Attributes
    def get(self):
        """
        *get the templates_transients_followup_obs object*

        **Return:**
            - ``responseContent`` -- the response

        """
        self.log.debug('starting the ``get`` method')

        from ..commonelements.pagetemplates import defaultpagetemplate

        transients_followup_obs = models_transients_followup_obs_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        followup_obs = transients_followup_obs.get()

        self.log.debug('completed the ``get`` method')
        return followup_obs
    # xt-class-method
