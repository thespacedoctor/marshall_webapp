#!/usr/local/bin/python
# encoding: utf-8
"""
models_transients_post.py
=========================
:Summary:
    The HTML template module for the `models_transients_post.py` resource

:Author:
    David Young

:Date Created:
    October 10, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
from datetime import datetime
from dryxPython import astrotools as dat
from marshallEngine.feeders.useradded import data, images


class models_transients_post():

    """
    The worker class for the models_transients_post module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        elementId=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        self.response = ""
        self.redirectUrl = ""
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'models_transients_post' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def post(self):
        """execute the post method on the models_transients_post object

        **Return:**
            - ``response`` -- the reponse to send to the browser
            - ``redirectUrl`` -- the URL to redirect to once the transient has been added

        **Todo**
        """
        self.log.debug('starting the ``post`` method')

        elementId = self.elementId

        # check the query string parameters for the correct variable required to
        # add a transient
        if set(("objectRa", "objectDec", "objectName")) <= set(self.request.params):
            self._add_new_transient()

        # add alert if nothing was added to the database
        if len(self.response) == 0:
            self.response = "Response from <code>" + \
                __name__ + "</code><BR><BR>No Action Was Performed<BR><BR>"
            if elementId:
                self.response += "The element selected was </code>%(elementId)s</code>" % locals(
                )
            else:
                self.response += "Resource Context selected (no element)" % locals(
                )

        self.log.debug('completed the ``post`` method')
        return self.response, self.redirectUrl

    def _add_new_transient(
            self):
        """ add new transient to the marshall

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
        """
        self.log.debug('starting the ``_add_new_transient`` method')

        # UNPACK DICTIONARY VALUES TO LOCAL()
        for arg, val in self.request.params.iteritems():
            varname = arg
            if isinstance(val, str) or isinstance(val, unicode):
                exec(varname + ' = """%s""" ' % (val,))
            else:
                exec(varname + " = %s" % (val,))
            self.log.debug('%s = %s' % (varname, val,))

        # CONVERT RA AND DEC IF REQUIRED
        try:
            tmp = float(objectRa)
        except:
            tmp = None
        if not tmp:
            objectRa = dat.ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(
                ra=objectRa
            )
        try:
            tmp = float(objectDec)
        except:
            tmp = None
        if not tmp:
            objectDec = dat.declination_sexegesimal_to_decimal.declination_sexegesimal_to_decimal(
                dec=objectDec
            )

        # GET DATES AND MJD
        if isinstance(objectDate, str) and "-" in objectDate:
            objectDate = datetime.strptime(
                objectDate + "T00:00:00.0", '%Y-%m-%dT%H:%M:%S.%f')
            mjd = dat.getMJDFromSqlDate(
                sqlDate=objectDate
            )
        elif isinstance(objectDate, float) or isinstance(objectDate, str):
            mjd = float(objectDate)
            objectDate = dat.getDateFromMJD(
                mjd
            )

        ticketAuthor = self.request.authenticated_userid

        # add some default null values
        if "objectRedshift" not in locals() or len(str(objectRedshift)) == 0:
            objectRedshift = "null"
        if "objectUrl" not in locals():
            objectUrl = "null"
        else:
            objectUrl = """ '%(objectUrl)s' """ % locals()
        if "objectImageStamp" not in locals():
            objectImageStamp = "null"
        else:
            objectImageStamp = """ '%(objectImageStamp)s' """ % locals()

        # now add the new transient to the `fs_user_added` table
        sqlQuery = u"""
            INSERT IGNORE INTO fs_user_added
                (candidateID,
                    targetImageUrl,
                    objectURL,
                    survey,
                    ra_deg,
                    dec_deg,
                    discMag,
                    mag,
                    observationMJD,
                    discDate,
                    suggestedType,
                    hostZ,
                    author,
                    ingested,
                    summaryRow,
                    dateCreated,
                    dateLastModified) VALUES ('%s',%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s',0,1,NOW(),NOW())""" % (
            objectName,
            objectImageStamp,
            objectUrl,
            objectSurvey,
            objectRa,
            objectDec,
            objectMagnitude,
            objectMagnitude,
            mjd,
            objectDate,
            u"SN",
            objectRedshift,
            ticketAuthor)
        self.request.db.execute(sqlQuery)
        self.request.db.commit()
        self.request.db.commit()

        # import the new objects in fs_user_added to transientBucket
        dbConn = self.request.registry.settings["dbConn"]

        print dbConn

        # IMPORT THE DATA AND IMAGES
        ingester = data(
            log=self.log,
            settings=self.request.registry.settings,
            dbConn=dbConn
        ).ingest(withinLastDays=3000)
        cacher = images(
            log=self.log,
            settings=self.request.registry.settings,
            dbConn=dbConn
        ).cache(limit=3000)

        # Create the redirect URL based on the name of the new object added
        self.redirectUrl = self.request.route_path(
            'transients_search', _query={'q': objectName})

        self.log.debug('completed the ``_add_new_transient`` method')
        return None

    # xt-class-method
