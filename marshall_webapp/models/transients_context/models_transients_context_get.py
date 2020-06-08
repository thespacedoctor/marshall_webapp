#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `models_transients_context_get.py` resource*

:Author:
    David Young

:Date Created:
    October 9, 2014
"""
from __future__ import division
from future import standard_library
standard_library.install_aliases()
from builtins import zip
from builtins import object
from past.utils import old_div
import sys
import os
import khufu
import collections
import urllib.request, urllib.parse, urllib.error
import re


class models_transients_context_get(object):
    """
    The worker class for the models_transients_context_get module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
    """

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
        self.defaultQs = {
            "format": "json",
        }

        log.debug("instansiating a new 'models_transients_context_get' object")

        return None

    def close(self):
        del self
        return None

    def get(self):
        """execute the get method on the models_transients_context_get object

        **Return:**
            - ``responseContent`` -- the reponse to send to the browser
        """
        self.log.debug('starting the ``get`` method')

        transientBucketId = self.elementId

        # GRAB THE LIGHTCURVE DATA FOR THE OBJECT
        sqlQuery = """
            select * from sherlock_crossmatches where transient_object_id in (select transientBucketId from transientBucket where replacedByRowId = 0 and transientBucketId = %(transientBucketId)s);
        """ % locals()

        context = self.request.db.execute(sqlQuery).fetchall()

        aladinFOV = 50.
        snCat = []
        agnCat = []
        ntCat = []
        starCat = []
        cvCat = []
        otherCat = []
        bsCat = []

        transTypes = ["sn", "nt", "cv", "agn",
                      "variablestar", "vs", "?", "unclear", "bs"]
        cats = [snCat, ntCat, cvCat, agnCat,
                starCat, starCat, otherCat, otherCat, bsCat]
        colors = ["#268bd2", "#d33682", "#859900",
                  "#b58900", "#cb4b16", "#cb4b16", "#6c71c4", "#6c71c4", "#A0A0A0"]
        # blue #268bd2
        # magenta #d33682
        # green #859900
        # yellow #b58900
        # orange #cb4b16
        # violet #6c71c4

        sourceType = ["galaxy", "agn/qso", "star", "cv/cb", "other"]
        icons = ["spinner5", "target3", "star3", "sun6", "help2"]
        iconsUnicode = [u"", u"", u"", u"", u""]
        # iconsUnicode = [u"a", u"a", u"a", u"a", u"a"]

        from astrocalc.coords import unit_conversion
        # ASTROCALC UNIT CONVERTER OBJECT
        converter = unit_conversion(
            log=self.log
        )

        for c in context:
            c = dict(c)

            # UPDATE ALADIN FOV
            if c["original_search_radius_arcsec"] * 6.0 > aladinFOV:
                aladinFOV = c["original_search_radius_arcsec"] * 6.0

            c["object_link"] = None
            objectName = urllib.parse.quote(c["catalogue_object_id"])

            if "ned" in c["catalogue_table_name"].lower():
                c[
                    "object_link"] = "https://ned.ipac.caltech.edu/cgi-bin/objsearch?objname=%(objectName)s&extend=no&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=RA+or+Longitude&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES" % locals()

            elif "sdss" in c["catalogue_table_name"].lower():
                c[
                    "object_link"] = "http://skyserver.sdss.org/dr12/en/tools/explore/Summary.aspx?id=%(objectName)s" % locals()

                ra = converter.ra_decimal_to_sexegesimal(
                    ra=c["raDeg"],
                    delimiter=""
                )
                dec = converter.dec_decimal_to_sexegesimal(
                    dec=c["decDeg"],
                    delimiter=""
                )
                c["catalogue_object_id"] = "SDSS J" + ra[0:9] + dec[0:9]
            elif "milliquas" in c["catalogue_table_name"].lower():
                c[
                    "object_link"] = "https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3query.pl?bparam_name=%(objectName)s&navtrail=%%3Ca+class%%3D%%27navpast%%27+href%%3D%%27https%%3A%%2F%%2Fheasarc.gsfc.nasa.gov%%2FW3Browse%%2Fall%%2Fmilliquas.html%%27%%3E+Choose+Tables%%3C%%2Fa%%3E+%%3E+%%3Ca+class%%3D%%27navpast%%27+href%%3D%%27%%2Fcgi-bin%%2FW3Browse%%2Fw3table.pl%%3FREAL_REMOTE_HOST%%3D143.117.37.81%%26tablehead%%3Dname%%253Dmilliquas%%26Action%%3DMore%%2BOptions%%26REAL_REMOTE_HOST%%3D143%%252E117%%252E37%%252E81%%26Equinox%%3D2000%%26Action%%3DMore%%2BOptions%%26sortby%%3Dpriority%%26ResultMax%%3D1000%%26maxpriority%%3D99%%26Coordinates%%3DEquatorial%%26tablehead%%3Dname%%253Dmilliquas%%26Action%%3DParameter%%2BSearch%%27%%3EParameter+Search%%3C%%2Fa%%3E&popupFrom=Query+Results&tablehead=name%%3Dheasarc_milliquas%%26description%%3DMillion+Quasars+Catalog+%%28MILLIQUAS%%29%%2C+Version+4.5+%%2810+May+2015%%29%%26url%%3Dhttp%%3A%%2F%%2Fheasarc.gsfc.nasa.gov%%2FW3Browse%%2Fgalaxy-catalog%%2Fmilliquas.html%%26archive%%3DN%%26radius%%3D1%%26mission%%3DGALAXY+CATALOG%%26priority%%3D5%%26tabletype%%3DObject&dummy=Examples+of+query+constraints%%3A&varon=name&bparam_name%%3A%%3Aunit=+&bparam_name%%3A%%3Aformat=char25&varon=ra&bparam_ra=&bparam_ra%%3A%%3Aunit=degree&bparam_ra%%3A%%3Aformat=float8%%3A.5f&varon=dec&bparam_dec=&bparam_dec%%3A%%3Aunit=degree&bparam_dec%%3A%%3Aformat=float8%%3A.5f&varon=bmag&bparam_bmag=&bparam_bmag%%3A%%3Aunit=mag&bparam_bmag%%3A%%3Aformat=float8%%3A4.1f&varon=rmag&bparam_rmag=&bparam_rmag%%3A%%3Aunit=mag&bparam_rmag%%3A%%3Aformat=float8%%3A4.1f&varon=redshift&bparam_redshift=&bparam_redshift%%3A%%3Aunit=+&bparam_redshift%%3A%%3Aformat=float8%%3A6.3f&varon=radio_name&bparam_radio_name=&bparam_radio_name%%3A%%3Aunit=+&bparam_radio_name%%3A%%3Aformat=char22&varon=xray_name&bparam_xray_name=&bparam_xray_name%%3A%%3Aunit=+&bparam_xray_name%%3A%%3Aformat=char22&bparam_lii=&bparam_lii%%3A%%3Aunit=degree&bparam_lii%%3A%%3Aformat=float8%%3A.5f&bparam_bii=&bparam_bii%%3A%%3Aunit=degree&bparam_bii%%3A%%3Aformat=float8%%3A.5f&bparam_broad_type=&bparam_broad_type%%3A%%3Aunit=+&bparam_broad_type%%3A%%3Aformat=char4&bparam_optical_flag=&bparam_optical_flag%%3A%%3Aunit=+&bparam_optical_flag%%3A%%3Aformat=char3&bparam_red_psf_flag=&bparam_red_psf_flag%%3A%%3Aunit=+&bparam_red_psf_flag%%3A%%3Aformat=char1&bparam_blue_psf_flag=&bparam_blue_psf_flag%%3A%%3Aunit=+&bparam_blue_psf_flag%%3A%%3Aformat=char1&bparam_ref_name=&bparam_ref_name%%3A%%3Aunit=+&bparam_ref_name%%3A%%3Aformat=char6&bparam_ref_redshift=&bparam_ref_redshift%%3A%%3Aunit=+&bparam_ref_redshift%%3A%%3Aformat=char6&bparam_qso_prob=&bparam_qso_prob%%3A%%3Aunit=percent&bparam_qso_prob%%3A%%3Aformat=int2%%3A3d&bparam_alt_name_1=&bparam_alt_name_1%%3A%%3Aunit=+&bparam_alt_name_1%%3A%%3Aformat=char22&bparam_alt_name_2=&bparam_alt_name_2%%3A%%3Aunit=+&bparam_alt_name_2%%3A%%3Aformat=char22&Entry=&Coordinates=J2000&Radius=Default&Radius_unit=arcsec&NR=CheckCaches%%2FGRB%%2FSIMBAD%%2FNED&Time=&ResultMax=10&displaymode=Display&Action=Start+Search&table=heasarc_milliquas" % locals()
            elif ("ps1" not in c["catalogue_table_name"].lower()) and ("ritter" not in c["catalogue_table_name"].lower()) and ("down" not in c["catalogue_table_name"].lower()) and ("guide_star" not in c["catalogue_table_name"].lower()) and ("kepler" not in c["catalogue_table_name"].lower()):
                c[
                    "object_link"] = "http://simbad.u-strasbg.fr/simbad/sim-id?Ident=%(objectName)s&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit+id" % locals()

            if c["object_link"]:
                c["catalogue_object_id"] = khufu.a(
                    content=c["catalogue_object_id"],
                    href=c["object_link"],
                    openInNewTab=True
                )

            if c["catalogue_object_type"].lower() == "other":
                c["catalogue_object_type"] = c["catalogue_object_subtype"]

            # transient_object_id': 871327L,
            # distance_modulus': None,
            # association_type': 'SN',
            # rank': 9L,
            # original_search_radius_arcsec': 20.0,
            # catalogue_object_dec': 6.09801031993,
            # catalogue_view_name': 'tcs_view_galaxy_sdss_photo_stars_galaxies_dr12',
            # id': 129686L,
            # direct_distance_modulus': None,
            # scale': None,
            # direct_distance': None,
            # catalogue_object_subtype': '3',
            # catalogue_object_ra': 31.3035672863,
            # catalogue_object_type': 'galaxy',
            # catalogue_table_name': 'tcs_cat_sdss_photo_stars_galaxies_dr12',
            # catalogue_object_id': '1237667227685224623',
            # search_name': 'sdss phot sn angular',
            # separation': 17.031327044,
            # catalogue_table_id': 47,
            # date_added': datetime.datetime(2015, 9, 22, 16, 28, 37),
            # major_axis_arcsec': None,
            # physical_separation_kpc': None,
            # distance': None, 'radius_color': '#268bd2',
            # direct_distance_scale': None,
            # association_rank': None,
            # z': None}

            other = True
            for s, i in zip(sourceType, iconsUnicode):

                if c["catalogue_object_type"].lower() in s:
                    rank = c["rank"]
                    c[
                        "label"] = """%(i)s%(rank)s""" % locals()
                    other = False

            if other == True:
                rank = c["rank"]
                c[
                    "label"] = u"""%(rank)s""" % locals()

            c["radius_color"] = None
            for tt, cat, col in zip(transTypes, cats, colors):
                if c["association_type"].lower() == tt:
                    c["radius_color"] = col
                    cat.append(c)

            dist = c["distance"]
            if not dist:
                dist = "-"
            else:
                dist = "%(dist)0.1f Mpc" % locals()

            asep = c["separationArcsec"]
            dsep = c["physical_separation_kpc"]

            if dsep:
                sep = "%(asep)0.1f\" / %(dsep)0.1f Kpc" % locals()
            else:
                sep = "%(asep)0.1f\"" % locals()

            c["details"] = "<em>source type: </em>" + \
                c["catalogue_object_type"]
            c["details"] += "<br/><em>transient association: </em>" + \
                c["association_type"]
            c["details"] += "<br/><em>catalogue: </em>" + \
                c["catalogue_table_name"].replace(
                    "tcs_cat", "").replace("_", " ")
            c[
                "details"] += "<br/><em>distance to source: </em>%(dist)s" % locals()
            c[
                "details"] += "<br/><em>separation: </em>%(sep)s" % locals()

            regex = re.compile(r'(v\d{1,3}) (\d{1,3})( (\d{1,3}))?')
            c["catalogue_table_name"] = regex.sub(
                "\g<1>.\g<2>", c["catalogue_table_name"])

        catalogues = {
            "nt": {
                "color": "#859900",
                "data": ntCat
            },
            "agn": {
                "color": "#dc322f",
                "data": agnCat
            },
            "star": {
                "color": "#b58900",
                "data": starCat
            },
            "cv": {
                "color": "#cb4b16",
                "data": cvCat
            },
            "other": {
                "color": "#6c71c4",
                "data": otherCat
            },
            "sn": {
                "color": "#268bd2",
                "data": snCat
            },
            "bs": {
                "color": "#A0A0A0",
                "data": bsCat
            }
        }

        aladinParameters = {}
        aladinFOV = old_div(aladinFOV, 3600.)
        aladinParameters["FOV"] = float("""%(aladinFOV)0.3f""" % locals())
        aladinParameters["search_perimeter_width"] = 0.9

        json = {
            "aladin_parameters": aladinParameters,
            "catalogues": catalogues,
            "catalogueOrder": ["sn", "other", "star", "cv", "agn", "nt", "bs"]
        }

        self.log.debug('completed the ``get`` method')
        return json

    def _set_default_parameters(
            self):
        """ set default parameters
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        if "format" not in self.qs:
            self.qs["format"] = self.defaultQs["format"]

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    def get_metadata(
            self):
        """ extra metadata
        """
        self.log.debug('starting the ``get_metadata`` method')

        transientBucketId = self.elementId

        sqlQuery = u"""
            select * from transientBucketSummaries where transientBucketId = %(transientBucketId)s
        """ % locals()
        extraMetadataTmp = self.request.db.execute(sqlQuery).fetchall()
        extraMetadata = []
        extraMetadata[:] = [dict(list(zip(list(row.keys()), row)))
                            for row in extraMetadataTmp]

        self.log.debug('completed the ``get_metadata`` method')
        return extraMetadata

    # xt-class-method
