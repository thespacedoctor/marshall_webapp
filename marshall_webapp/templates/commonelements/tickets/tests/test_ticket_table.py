import os
import nose
from .. import ticket_table

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE


def setUpModule():
    import logging
    import logging.config
    import yaml

    from pessto_marshall_engine.commonutils.getpackagepath import getpackagepath

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    moduleDirectory = os.path.dirname(__file__)
    global pathToOutputDir, pathToInputDir
    pathToInputDir = moduleDirectory + "/input/"
    pathToOutputDir = moduleDirectory + "/output/"

    # SETUP THE TEST LOG FILE
    global testlog
    testlog = open(pathToOutputDir + "tests.log", 'w')

    # SETUP LOGGING
    loggerConfig = """
    version: 1
    formatters:
        file_style:
            format: '* %(asctime)s - %(name)s - %(levelname)s (%(filename)s > %(funcName)s > %(lineno)d) - %(message)s  '
            datefmt: '%Y/%m/%d %H:%M:%S'
        console_style:
            format: '* %(asctime)s - %(levelname)s: %(filename)s:%(funcName)s:%(lineno)d > %(message)s'
            datefmt: '%H:%M:%S'
        html_style:
            format: '<div id="row" class="%(levelname)s"><span class="date">%(asctime)s</span>   <span class="label">file:</span><span class="filename">%(filename)s</span>   <span class="label">method:</span><span class="funcName">%(funcName)s</span>   <span class="label">line#:</span><span class="lineno">%(lineno)d</span> <span class="pathname">%(pathname)s</span>  <div class="right"><span class="message">%(message)s</span><span class="levelname">%(levelname)s</span></div></div>'
            datefmt: '%Y-%m-%d <span class= "time">%H:%M <span class= "seconds">%Ss</span></span>'
    handlers:
        console:
            class: logging.StreamHandler
            level: DEBUG
            formatter: console_style
            stream: ext://sys.stdout
    root:
        level: DEBUG
        handlers: [console]"""

    logging.config.dictConfig(yaml.load(loggerConfig))
    global log
    log = logging.getLogger(__name__)

    # SETUP DB CONNECTION
    import MySQLdb as ms
    dbConfig = """
    version: 1
    db: pessto_marshall_sandbox
    host: localhost
    user: root
    password: root
    """
    connDict = yaml.load(dbConfig)
    global dbConn
    dbConn = ms.connect(
        host=connDict['host'],
        user=connDict['user'],
        passwd=connDict['password'],
        db=connDict['db'],
    )
    # x-import-test-database

    return None


def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None


class test_ticket_table():

    def test_ticket_table_function(self):
        import khufu
        import pessto_marshall_engine.webapp.marshall.webpage as webpage

        ticket = khufu.image(
            # [ industrial | gray | social ]
            src='holder.js/1200x200/auto/industrial/text:object ticket',
        )

        ticket = khufu.grid_column(
            span=12,  # 1-12
            offset=0,  # 1-12
            content=ticket,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        ticket = khufu.grid_row(
            responsive=True,
            columns=ticket,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        ticketList = [ticket, ticket, ticket, ticket, ticket, ticket, ticket]

        kwargs = {}
        kwargs["log"] = log
        kwargs["ticketList"] = ticketList

        thisObject = ticket_table.ticket_table(**kwargs)

        mainContent = thisObject

        import khufu
        navBar = khufu.navBar(
            brand='pessto',
            contentList=[],
            dividers=False,
            fixedOrStatic=False,
            location='top',
            responsive=False,
            dark=False
        )
        sideBar = khufu.image(
            src='holder.js/500x700/auto/industrial/text:sidebar',
        )
        kwargs = {}
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        kwargs["bodyId"] = "workflow page"
        kwargs["pageTitle"] = "PESSTO Marshall"
        kwargs["topNavBar"] = navBar
        kwargs["sideBar"] = sideBar
        kwargs["mainContent"] = mainContent
        # kwargs["assetsPath"] = ""
        thisWebObject = webpage.webpage(**kwargs)
        print thisWebObject
        pathToWriteFile = pathToOutputDir + "webpage.html"
        try:
            log.debug("attempting to open the file %s" % (pathToWriteFile,))
            writeFile = open(pathToWriteFile, 'w')
        except IOError, e:
            message = 'could not open the file %s' % (pathToWriteFile,)
            log.critical(message)
            raise IOError(message)
        writeFile.write(thisWebObject)
        writeFile.close()

    # x-class-to-test-named-worker-function
