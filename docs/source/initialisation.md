# Initialisation 

Before using marshall_webapp you need to use the `init` command to generate a user settings file. Running the following creates a [yaml](https://learnxinyminutes.com/docs/yaml/) settings file in your home folder under `~/.config/marshall_webapp/marshall_webapp.yaml`:

```bash
marshall_webapp init
```

The file is initially populated with marshall_webapp's default settings which can be adjusted to your preference.

If at any point the user settings file becomes corrupted or you just want to start afresh, simply trash the `marshall_webapp.yaml` file and rerun `marshall_webapp init`.

<!-- Once created, open the settings file in any text editor and follow the in-file instructions to populate the missing settings values (usually given an ``XXX`` placeholder).  -->



## Modifying the Settings

Once created, open the settings file in any text editor and make any modifications needed. 


## Basic Python Setup

If you plan to use `marshall_webapp` in your own scripts you will first need to parse your settings file and set up logging etc. One quick way to do this is to use the `fundamentals` package to give you a logger, a settings dictionary and a database connection (if connection details given in settings file):

```python
## SOME BASIC SETUP FOR LOGGING, SETTINGS ETC
from fundamentals import tools
from os.path import expanduser
home = expanduser("~")
settingsFile  = home + "/.config/marshall_webapp/marshall_webapp.yaml"
su = tools(
    arguments={"settingsFile": settingsFile},
    docString=__doc__,
)
arguments, settings, log, dbConn = su.setup()
```
