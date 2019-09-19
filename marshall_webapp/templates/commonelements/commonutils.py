#!/usr/local/bin/python
# encoding: utf-8
"""
*Common Utilities for the PESSTO Webapp(s)*

:Author:
    David Young

:Date Created:
    November 21, 2013
"""
import sys
import os
import khufu


def block_title(
        log,
        title,
        align="left"
):
    """block title

    **Key Arguments:**
        - ``title`` -- the title for the block
        - ``log`` -- the logger
        - ``align`` -- False | left | right | center

    **Return:**
        - ``title`` -- the title for the ticket block
    """
    log.debug('starting the ``block_title`` function')

    thisTitle = khufu.p(
        content=title,
        textAlign=align,  # [ left | center | right ]
        color="muted",  # [ muted | warning | info | error | success ]
    )

    thisTitle = khufu.grid_row(
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
        - ``text`` -- little label 
    """
    if lineBreak is not False:
        lineBreak = "<br>&nbsp&nbsp&nbsp"
    else:
        lineBreak = ""

    text = khufu.coloredText(
        text="%(text)s %(lineBreak)s" % locals(),
        color="grey",  # [ muted | warning | info | error | success ]
        htmlClass="littlelabel",
        pull=pull
    )

    return text

if __name__ == '__main__':
    main()
