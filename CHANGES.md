
## Marshall Webapp Release Notes

fixed: list text now shown in pending classification tickets identity blocks (previously blank)
move-to buttons can now be set/altered via the yaml settings file. This gives marshall administrator full customisation of the triage workflow
best name is selected in both table view and plain-text outputs
json output now reports akas (name and url) for each transient
fixed csv and plain text downloads
allow for debug toolbar over https
https switch added to the setting file. Set to False for plain http (`https: True` is the default)  
default parameters for the marshall/transients state can be set in the settings file. For example, show all transients below declination of 30:

    ```yaml
    default_filters:
        filterBy1: decDeg
        filterValue1: 30
        filterOp1: "<" 
    ```

all links in sidebar now show as "selected" (white background) if the user is looking at that list
**FIXED**: sdss link now use the new skyserver api

**v3.1.1 - May 7, 2021**

* **ENHANCEMENT**: SSL certificate now installed on the pessto.org domain. All traffic is now encrypted and secure. All `http` requests should also be redirected to `https`.
* **FIXED**: classification summary info on each ticket is now the latest and most relevant. At times an older redshift report was being presented.

**v3.1.0 - March 17, 2021**

* **REFACTOR** search function more forgiving, but also more accurate and MUCH faster
* **REFACTOR** adding new sources via the "create new ticket button" now faster
* **ENHANCEMENT** AT/SN names now set as the 'master' or headline name in each transient ticket. All other names and links added to *aka* section.
* **ENHANCEMENT**: added light echo to classification options
* **FIXED**: issue where transient history logs were not getting parsed correctly resulting in ticket not loading in marshall interface
* **FIXED** database connector, needed to create new tickets and add classifications, pings MySQL server and reconnects if connection is broken *before* executing actions. This hopefully fixes the long-standing issues with these 2 features.

**v3.0.9 - January 11, 2021**

* **FEATURE** documentation for the marshall webapp is on [readthedocs](https://marshall-webapp.readthedocs.io/en/master/). This is mainly for developer reference so far.
* **FIXED** the context visualisation is now displaying correctly to show all sherlock crossmatches (see context tab on transient tickets)

**v3.0.8 - December 15, 2020**

* **REFACTOR** added ability to set classification priority when moving ticket to classification list
* **FIXED** fixing cache links so images appear and downloads work correctly

**v3.0.7 - December 4, 2020**

* **REFACTOR** settings files clean up and consolidation
* **FIXED** classification bug squashed

**v3.0.6 - December 4, 2020**

* **REFACTOR** moved a sherlock book-keeping query from front-end code to database procedure. Should decrease page load times.
* **FIXED** sorting lists on 'latest comment'.

**v3.0.5 - December 3, 2020**

* **FIXED** date formats, broken aka links, broken stats pages and broken table view

**v3.0.4 - December 2, 2020**

* **FIXED** comment function (legacy unicode fix)

**v3.0.3 - December 2, 2020**

* **FIXED** search function

**v3.0.2 - November 17, 2020**

* **Enhancement** added config files for cluster
* **Enhancement** added ability to connect to a non-standard database port issue

**v3.0.1 - July 6, 2020**

* **Fixed** unittest database import metadata lock issue
* **Fixed** bug in search resource

**v3.0.0 - June 25, 2020**

* Now compatible with Python 3.*
