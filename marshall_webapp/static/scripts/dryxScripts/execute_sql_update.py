#!/usr/local/bin/python
# encoding: utf-8
"""
execute_sql_update.py
=====================
:Summary:
    Execute a SQL udpate query

:Author:
    David Young

:Date Created:
    July 1, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete, extract all code out of the main function and add cl commands
    @review: make internal function private
    @review: pull all general functions and classes into dryxPythonModules
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import dryxPython.logs as dl
from dryxPython import mysql as dms

######################################################
# MAIN LOOP - USED FOR DEBUGGING OR WHEN SCRIPTING   #
######################################################


def main():
    """
    The code executed on webpage load
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import cgi
    import cgitb
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import dryxPython.commonutils as dcu
    import dryxPython.htmlframework as dhf

    ################ > SETUP ##################
    # ENABLE DEBUGGING
    cgitb.enable()
    log = emptyLogger()

    # GRAB FIELD STORAGE ARGUMENTS
    fs = cgi.FieldStorage()
    # UNPACK FIELDSTORAGE VALUES TO LOCAL()
    params = {}
    for key in fs.keys():
        params[key] = fs[key].value
    defaultFields = dhf.urls.default_fields.default_fields()
    for k, v in defaultFields.iteritems():
        if k not in params.keys():
            params[k] = v
    for arg, val in params.iteritems():
        varname = arg
        if isinstance(val, str) or isinstance(val, unicode):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))

    debugging = 1
    if "debugging" in locals() and debugging == 1:
        print 'Content-Type: text/html\n\n'
        print "<html>"
        print "<head>"
        print "<title>Hello - Second CGI Program</title>"
        print "</head>"
        print "<body>"
        print "FS has length %s" % (len(fs),)
        for k, v in params.iteritems():
            print "<h3>%s = %s</h3>" % (k, v,)
        print "</body>"
        print "</html>"

    # GRAB SETTINGS
    import yaml
    moduleDirectory = os.path.dirname(__file__)
    index = moduleDirectory.index("assets")
    pathToDocRoot = moduleDirectory[:index + 6]
    pathToSettingsFile = pathToDocRoot + \
        "/settings/path_to_settings.yaml"
    stream = file(pathToSettingsFile, 'r')
    yamlContent = yaml.load(stream)
    stream.close()

    if int(settingsFile) > 1:
        settingsFile = "path to settings file %(settingsFile)s" % locals()
    else:
        settingsFile = "path to settings file"

    if not yamlContent[settingsFile]:
        message = 'Please make sure settingsFile is the settings file in %s ' % (
            pathToSettingsFile,)
        log.critical(message)
        raise AttributeError(message)
    else:
        pathToSettingsFile = yamlContent[settingsFile]
        stream = file(yamlContent[settingsFile], 'r')
        settings = yaml.load(stream)
        stream.close()

    log = dl.setup_dryx_logging(
        yaml_file=yamlContent[settingsFile]
    )
    # SETUP A DATABASE CONNECTION BASED ON WHAT ARGUMENTS HAVE BEEN PASSED
    dbConn = False
    if 'settings' in locals() and "database settings" in settings:
        host = settings["database settings"]["host"]
        user = settings["database settings"]["user"]
        passwd = settings["database settings"]["password"]
        dbName = settings["database settings"]["db"]
        dbConn = True
    if dbConn:
        import MySQLdb as ms
        dbConn = ms.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=dbName,
            use_unicode=True,
            charset='utf8'
        )
        log.debug('dbConn: %s' % (dbConn,))

    # x-url-for-cgi-page

    ################ > VARIABLE SETTINGS ######
    # SETUP THE VARIOUS URL TOKEN VALUES
    dms.execute_mysql_write_query(
        sqlQuery=sqlQuery,
        dbConn=dbConn,
        log=log
    )

    ################ >ACTION(S) ###############
    # xpessto-marshall-webpage-template
    # xdhf-print-as-json-to-cgi
    # redirect-with-cgi

    dbConn.commit()
    dbConn.close()
    return

###################################################################
# CLASSES                                                         #
###################################################################


class emptyLogger:

    def info(self, argu):
        pass

    def error(self, argu):
        pass

    def debug(self, argu):
        pass

    def critical(self, argu):
        pass

    def warning(self, argu):
        pass

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
