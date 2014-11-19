#!/usr/local/bin/python
# encoding: utf-8
"""
update_git_repo.py
==================
:Summary:
    Update git repos on local machine by triggering this URL with the name of the repo you wish to update

:Author:
    David Young

:Date Created:
    June 24, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os

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
    import khufu

    ################ > SETUP ##################
    # ENABLE DEBUGGING
    cgitb.enable()

    # GRAB FIELD STORAGE ARGUMENTS
    fs = cgi.FieldStorage()
    # UNPACK FIELDSTORAGE VALUES TO LOCAL()
    params = {}
    for key in fs.keys():
        params[key] = fs[key].value
    defaultFields = khufu.urls.default_fields.default_fields()
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

    # log = dl.setup_dryx_logging(
    #     yaml_file=yamlContent[settingsFile]
    # )

    pathToWriteFile = settings["path to git_repos directory"] + \
        "/_updates_required_/%(repoName)s.gitupdates" % locals()
    try:
        #log.debug("attempting to open the file %s" % (pathToWriteFile,))
        writeFile = open(pathToWriteFile, 'w')
    except IOError, e:
        message = 'could not open the file %s' % (pathToWriteFile,)
        # log.critical(message)
        raise IOError(message)
    writeFile.close()

    # x-url-for-cgi-page

    ################ > VARIABLE SETTINGS ######
    # SETUP THE VARIOUS URL TOKEN VALUES

    ################ >ACTION(S) ###############
    # xpessto-marshall-webpage-template
    # xt-print-as-json-to-cgi
    # redirect-with-cgi

    # dbConn.commit()
    # dbConn.close()
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
