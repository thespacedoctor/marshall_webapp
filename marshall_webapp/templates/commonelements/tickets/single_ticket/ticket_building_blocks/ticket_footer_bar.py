#!/usr/local/bin/python
# encoding: utf-8
"""
*The ticket footer bar for the object ticket*

:Author:
    David Young

:Date Created:
    November 20, 2013
"""
import sys
import os
import re
from marshall_webapp.templates.commonelements import commonutils as cu
import khufu


def ticket_footer_bar(
        log,
        request,
        discoveryDataDictionary,
        atelData):
    """get ticket footer bar

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``discoveryData`` -- the discoveryData for the object
        - ``atelData`` -- the atel matches for the objects displayed on the webpage

    **Return:**
        - ``ticket_footer_bar`` -- the ticket footer bar for the pesssto object
    """
    log.debug('starting the ``ticket_footer_bar`` function')

    ## VARIABLES ##
    transientBucketId = discoveryDataDictionary["transientBucketId"]

    atels = _get_atel_list(
        log,
        transientBucketId,
        atelData
    )

    # LINK EXPLODER BUTTONS

    # NED
    ra = discoveryDataDictionary["raDeg"]
    ra = "%(ra)9.6f" % locals()
    dec = discoveryDataDictionary["decDeg"]
    dec = "%(dec)9.6f" % locals()
    if float(dec) > 0.:
        dec = str("""+%(dec)s""" % locals())
    nedLink = """http://ned.ipac.caltech.edu/cgi-bin/objsearch?in_csys=Equatorial&in_equinox=J2000.0&lon=%(ra)sd&lat=%(dec)sd&radius=0.5&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&search_type=Near+Position+Search&z_constraint=Unconstrained&z_value1=&z_value2=&z_unit=z&ot_include=ANY&nmp_op=ANY&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=Distance+to+search+center&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES""" % locals(
    )
    adsLink = """http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?db_key=AST&db_key=PRE&qform=AST&arxiv_sel=astro-ph&arxiv_sel=cond-mat&arxiv_sel=cs&arxiv_sel=gr-qc&arxiv_sel=hep-ex&arxiv_sel=hep-lat&arxiv_sel=hep-ph&arxiv_sel=hep-th&arxiv_sel=math&arxiv_sel=math-ph&arxiv_sel=nlin&arxiv_sel=nucl-ex&arxiv_sel=nucl-th&arxiv_sel=physics&arxiv_sel=quant-ph&arxiv_sel=q-bio&sim_query=YES&ned_query=YES&adsobj_query=YES&aut_logic=OR&obj_logic=OR&author=&object=%(ra)s+%(dec)s+%%3A+0+1&start_mon=&start_year=&end_mon=&end_year=&ttl_logic=OR&title=&txt_logic=OR&text=&nr_to_return=200&start_nr=1&jou_pick=ALL&ref_stems=&data_and=ALL&group_and=ALL&start_entry_day=&start_entry_mon=&start_entry_year=&end_entry_day=&end_entry_mon=&end_entry_year=&min_score=&sort=SCORE&data_type=SHORT&aut_syn=YES&ttl_syn=YES&txt_syn=YES&aut_wt=1.0&obj_wt=1.0&ttl_wt=0.3&txt_wt=3.0&aut_wgt=YES&obj_wgt=YES&ttl_wgt=YES&txt_wgt=YES&ttl_sco=YES&txt_sco=YES&version=1""" % locals(
    )
    simbadLink = """http://simbad.u-strasbg.fr/simbad/sim-coo?protocol=html&NbIdent=1&Radius=1&Radius.unit=arcmin&CooFrame=FK5&CooEpoch=2000&CooEqui=2000&Coord=%(ra)sd%(dec)sd""" % locals(
    )
    extinctionLink = """http://ned.ipac.caltech.edu/cgi-bin/nph-calc?in_csys=Equatorial&in_equinox=J2000.0&obs_epoch=2000.0&lon=%(ra)sd&lat=%(dec)sd&pa=0.0&out_csys=Galactic&out_equinox=J2000.0""" % locals(
    )
    sdssExactLocation = """http://skyserver.sdss3.org/public/en/tools/chart/image.aspx?ra=%(ra)s&dec=%(dec)s&scale=0.25&opt=GS&width=512&height=512""" % locals(
    )
    vizier = """http://vizier.u-strasbg.fr/viz-bin/VizieR-4?-pos&-c.eq=J2000&-c.rs=30&-c=%(ra)s%(dec)s""" % locals(
    )

    linkList = [nedLink, adsLink, simbadLink,
                extinctionLink, sdssExactLocation, vizier]
    nameList = ["ned", "ads papers", "simbad",
                "extinction", "sdss - exact location", "vizier"]
    dropDownLinks = []
    for l, n in zip(linkList, nameList):
        dropDownLink = khufu.a(
            content=n,
            href=l,
            openInNewTab=True
        )
        dropDownLink = khufu.li(
            # IF A SUBMENU FOR DROPDOWN THIS SHOULD BE <UL>
            content=dropDownLink,
        )
        dropDownLinks.append(dropDownLink)

    popover = khufu.popover(
        tooltip=True,
        placement="bottom",  # [ top | bottom | left | right ]
        trigger="hover",  # [ False | click | hover | focus | manual ]
        title="explode all web service tools",
        content=False,
        delay=20
    )

    linkExploder = khufu.dropdown(
        buttonSize='small',
        buttonColor='primary',  # [ default | sucess | error | warning | info ]
        menuTitle='<i class="icon-wrench2"></i>',
        splitButton=False,
        linkList=dropDownLinks,
        separatedLinkList=False,
        popover=popover,
        pull=False,
        htmlClass=False,
        direction='up',  # [ down | up ]
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    footerColumn = khufu.grid_column(
        span=12,  # 1-12
        offset=0,  # 1-12
        content="""%(atels)s %(linkExploder)s""" % locals(),
        pull=False,  # ["right", "left", "center"]
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    ticket_footer_bar = khufu.grid_row(
        responsive=True,
        columns=footerColumn,
        htmlId=False,
        htmlClass="ticketFooter",
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    return ticket_footer_bar


def _get_atel_list(
        log,
        transientBucketId,
        atelData):
    """ get atels for object

    **Key Arguments:**
        - ``log`` -- logger
        - ``transientBucketId`` -- the transientBucketId
        - ``atelData`` -- the atel matches for the objects displayed on the webpage

    **Return:**
        - ``atelLinks`` -- the names of the atels linked to original pages
    """
    log.debug('starting the ``_get_atels`` function')

    rows = []
    for dataPoint in atelData:
        if dataPoint["transientBucketId"] == transientBucketId:
            row = dataPoint
            rows.append(row)

    atelLinks = []
    for row in rows:
        atelLink = khufu.a(
            content=row["name"].replace("atel_", "ATel "),
            href=row["surveyObjectUrl"],
            openInNewTab=True
        )
        atelLink = khufu.li(
            content=atelLink,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        atelLinks.append(atelLink)

    atelDropdown = ""
    if len(atelLinks):
        num = len(atelLinks)
        text = """%(num)s x ATel</i>""" % locals()

        popover = khufu.popover(
            tooltip=True,
            placement="bottom",  # [ top | bottom | left | right ]
            trigger="hover",  # [ False | click | hover | focus | manual ]
            title="explode all atel links",
            content=False,
            delay=20
        )

        atelDropdown = khufu.dropdown(
            buttonSize='small',
            # [ default | sucess | error | warning | info ]
            buttonColor='primary',
            menuTitle=text,
            splitButton=False,
            linkList=atelLinks,
            separatedLinkList=False,
            pull=False,
            htmlClass=False,
            direction='up',  # [ down | up ]
            onPhone=True,
            onTablet=True,
            onDesktop=True,
            popover=popover,
        )

    return atelDropdown
