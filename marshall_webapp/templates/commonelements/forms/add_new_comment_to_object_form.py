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
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
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
    """
    commentInput = khufu.textarea(
        rows=1,
        span=11,
        placeholder="add a new comment",
        htmlId="comment" % locals(),
        required=True
    )
    # authorInput = khufu.formInput(
    # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
    #     ttype='text',
    #     placeholder='author',
    #     span=2,
    #     htmlId="author" % locals(),
    #     required=True
    # )
    addButton = khufu.button(
        buttonText='add',
        # [ default | primary | info | success | warning | danger | inverse | link ]
        buttonStyle='info',
        buttonSize='default',  # [ large | default | small | mini ]
        submit=True
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
        inputList=[commentInput, transientBucketInput, addButton]
    )
    commentCG = khufu.horizontalFormControlGroup(
        content=commentInput,
        validationLevel=False
    )

    href = request.route_path(
        'transients_element_comments', elementId=transientBucketId, _query={'method': 'post'})
    newCommentForm = khufu.form(
        # list of control groups
        content="""%(commentCG)s""" % locals(),
        # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
        formType='inline',
        postToScript=href,
        redirectUrl=request.path_qs
    )

    return newCommentForm


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


if __name__ == '__main__':
    main()
