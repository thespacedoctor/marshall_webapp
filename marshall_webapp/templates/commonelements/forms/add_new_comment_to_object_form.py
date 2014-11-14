#!/usr/local/bin/python
# encoding: utf-8
"""
add_new_comment_to_object_form.py
=================================
:Summary:
    A form to add a new comment to an object ticket in the PESSTO Marshall

:Author:
    David Young

:Date Created:
    January 7, 2014

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
import khufu
from dryxPython import commonutils as dcu


def add_new_comment_to_object_form(
        log,
        request,
        transientBucketId
):
    """add_new_comment_to_object_form

    **Key Arguments:**
        - ``log`` -- the logger
        - ``request`` -- the pyramid request
        - ``transientBucketId`` -- the transientBucketId of the object

    **Return:**
        - ``newCommentForm`` -- the new comment form

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """

    # x-tmpx-form-control-group
    # x-horizontal-form-item
    commentInput = khufu.textarea(
        rows=1,
        span=9,
        placeholder="add a new comment",
        htmlId="comment" % locals(),
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=True,
        disabled=False
    )
    authorInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        ttype='text',
        placeholder='author',
        span=2,
        htmlId="author" % locals(),
        pull=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=True,
        disabled=False
    )
    addButton = khufu.button(
        buttonText='add',
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='info',
        buttonSize='default',  # [ large | default | small | mini ]
        htmlId=False,
        href=False,
        pull=False,  # right, left, center
        submit=True,
        block=False,
        disable=False,
        dataToggle=False
    )
    transientBucketInput = khufu.formInput(
        # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
        ttype='number',
        placeholder='',
        span=2,
        htmlId='transientBucketId',
        hidden=True,
        defaultValue=transientBucketId
    )

    commentInput = khufu.controlRow(
        inputList=[authorInput, commentInput, transientBucketInput, addButton]
    )
    commentCG = khufu.horizontalFormControlGroup(
        content=commentInput,
        validationLevel=False
    )

    prefix = request.registry.settings["apache prefix"]

    href = request.route_path(
        'transients_element_comments', elementId=transientBucketId, _query={'method': 'post'})
    newCommentForm = khufu.form(
        # list of control groups
        content="""%(commentCG)s""" % locals(),
        # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
        formType='inline',
        postToScript=href,
        redirectUrl=request.url
    )

    return newCommentForm

# use the tab-trigger below for new function
# x-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

############################################
# CODE TO BE DEPECIATED                    #
############################################

if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
