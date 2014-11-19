#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_element_put.py
==============================
:Summary:
    The HTML template module for the `models_transients_element_put.py` resource

:Author:
    David Youn
:Date Created:
    October 7, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from dryxPython import commonutils as dcu
from dryxPython import astrotools as dat


class models_transients_element_put():

    """
    The worker class for the models_transients_element_put module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        request
    ):
        self.log = log
        self.request = request
        self.transientBucketId = request.matchdict["elementId"]
        self.response = ""
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'models_transients_element_put' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def put(self):
        """get the models_transients_element_put object

        **Return:**
            - ``models_transients_element_put``

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        # move the objects to another list if requested
        if "mwl" in self.request.params or "awl" in self.request.params:
            self._move_transient_to_another_list()

        # change the pi is requested
        if set(("piName", "piEmail")) <= set(self.request.params):
            self._change_pi_for_object()

        # throw warning if nothing has changed
        if len(self.response) == 0:
            self.response = "nothing has changed"

        self.log.info('completed the ``get`` method')

        return self.response

    def _move_transient_to_another_list(
            self):
        """ create sqlquery for the put request

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
        """
        self.log.info('starting the ``_create_sqlquery`` method')
        transientBucketId = self.transientBucketId

        # change the marshall workflow location list if requested
        if "mwl" in self.request.params:
            mwl = self.request.params["mwl"]
            sqlQuery = """
                update pesstoObjects set marshallWorkflowLocation = "%(mwl)s" where transientBucketId = %(transientBucketId)s
            """ % locals()
            self.request.db.execute(sqlQuery)
            self.response = self.response + \
                " transientBucketId %(transientBucketId)s moved to the `%(mwl)s` marshallWorkflowLocation<BR>" % locals(
                )

        # change the alert workflow location list if requested
        if "awl" in self.request.params:
            mwl = self.request.params["awl"]
            sqlQuery = """
                update pesstoObjects set alertWorkflowLocation = "%(awl)s" where transientBucketId = %(transientBucketId)s
            """ % locals()
            self.request.db.execute(sqlQuery)
            self.response = self.response + \
                " transientBucketId %(transientBucketId)s moved to the `%(awl)s` alertWorkflowLocation<BR>" % locals(
                )

        self.log.info('completed the ``_create_sqlquery`` method')
        return None

    def _change_pi_for_object(
            self):
        """ change pi for object

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
        """
        self.log.info('starting the ``_change_pi_for_object`` method')

        piName = self.request.params["piName"]
        piEmail = self.request.params["piEmail"]
        transientBucketId = self.transientBucketId

        # change the pi in the database
        sqlQuery = """
            update pesstoObjects set pi_name = "%(piName)s", pi_email = "%(piEmail)s" where transientBucketId = %(transientBucketId)s   
        """ % locals()
        self.request.db.execute(sqlQuery)

        self.response = self.response + \
            "changed the PI of transient #%(transientBucketId)s to '%(piName)s' (%(piEmail)s)" % locals(
            )

        self.log.info('completed the ``_change_pi_for_object`` method')
        return None

    # xt-class-method
