#!/usr/local/bin/python
# encoding: utf-8
"""
commonutils.py
==============
:Summary:
    Common Utilities for the PESSTO Webapp(s)

:Author:
    David Young

:Date Created:
    November 21, 2013

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu


###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : November 21, 2013
# CREATED : November 21, 2013
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def block_title(
        log,
        title,
        align="left"
):
    """block title

    **Key Arguments:**
        - ``title`` -- the title for the block
        - ``log`` -- the logger

    **Return:**
        - ``title`` -- the title for the ticket block

    **Todo**
        - @review: when complete, clean block_title function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import dryxPython.htmlframework as dhf

    log.debug('starting the ``block_title`` function')
    # TEST THE ARGUMENTS

    ## VARIABLES ##

    thisTitle = dhf.p(
        content=title,
        textAlign=align,  # [ left | center | right ]
        color="muted",  # [ muted | warning | info | error | success ]
    )

    thisTitle = dhf.grid_row(
        responsive=True,
        columns=thisTitle,
        htmlId=False,
        htmlClass="ticketBlockTitle",
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    title = thisTitle

    log.debug('completed the ``block_title`` function')
    return title

# LAST MODIFIED : YYMD
# CREATED : YYMD
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def little_label(
        text="",
        pull=False,
        lineBreak=True
):
    """little labels for the pessto marshall tickets

    **Key Arguments:**
        - ``text`` -- the label text
        - ``lineBreak`` -- add a line break

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean little_labels function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import dryxPython.htmlframework as dhf

    ## VARIABLES ##

    if lineBreak is not False:
        lineBreak = "<br>&nbsp&nbsp&nbsp"
    else:
        lineBreak = ""

    text = dhf.coloredText(
        text="%(text)s %(lineBreak)s" % locals(),
        color="grey",  # [ muted | warning | info | error | success ]
        htmlClass="littlelabel",
        pull=pull
    )

    return text

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
