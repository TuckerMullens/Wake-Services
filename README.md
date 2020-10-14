# Wake-Services
CSC 331 Software Engineering - Wake Services Repo

Hey everyone here is some general information/an overview of what is contained
in this repository and how to start development on it!

###############################################################################
INSTALLATION:

-It is recommended that you use a virtualenv for the packages that you'll need
for this web app (unless you're using PyCharm, then you don't have to worry about
installing this).
-The packages needed for this app are listed in the "requirements.txt" file.
-NOTE that before you do the installation steps below, you HAVE TO HAVE Python
as well as pip installed (and virtualenv if you're not using PyCharm), THIS IS
VERY IMPORTANT.

-------------------------------------------------------------------------------
NON-PYCHARM USERS
-Start up a new virtualenv
-Activate the virtualenv
-Run the following command:

  pip install -r requirements.txt

-------------------------------------------------------------------------------
PYCHARM USERS
-Open up the repository folder in PyCharm
-Open up the terminal (At the bottom of the PyCharm window)
-Run the following command:

  pip install -r requirements.txt

###############################################################################
RUNNING THE APP:

-Open up your terminal/command prompt
-Start up your virtualenv (don't worry about this step if you're using PyCharm)
-Run the following command in this directory to run the web app:

  python app.py

(If that doesn't work, on some systems 'python' is named as 'py', so try this:
py app.py

-Then open up your browser to the URL that the terminal displays
-To stop the app press Ctrl + C in the terminal

###############################################################################
CONTENTS:

-------------------------------------------------------------------------------
templates

This folder contains the html templates for the web app which it renders when
the browser lands on the specified URL.

-------------------------------------------------------------------------------
static

This folder contains the css files for the web application, or in other words
the files which define the format and styling for the html pages. Images/logos
may be added to this folder later.

-------------------------------------------------------------------------------
app.py

The python file for the web app. This handles all of the redirecting/rerouting
of the app's URLs.

-------------------------------------------------------------------------------
requirements.txt

A text file containing the 3rd party packages used for the app. This list may
continue to grow as we start development.

###############################################################################
