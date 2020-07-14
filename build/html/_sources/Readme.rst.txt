.. role:: raw-html-m2r(raw)
   :format: html


Requirements
^^^^^^^^^^^^

This Django Rest-Framework application was developed with Python 3.8, 
but it will probably work with any Python version >= 3.6.  In the code
samples below, python3.8 can be replaced with python3.6 or python3.7.


.. image:: https://fruitpal.stefanzero.com/static/project-fruitpal.jpg
   :target: https://fruitpal.stefanzero.com/static/project-fruitpal.jpg
   :alt: Project Fruitpal


.. image:: https://fruitpal.stefanzero.com/static/project-fruitpal-2.jpg
   :target: https://fruitpal.stefanzero.com/static/project-fruitpal-2.jpg
   :alt: Project Fruitpal-2


.. image:: https://fruitpal.stefanzero.com/static/project-fruitpal-3.jpg
   :target: https://fruitpal.stefanzero.com/static/project-fruitpal-3.jpg
   :alt: Project Fruitpal-3


Installation
^^^^^^^^^^^^


#. 
   Clone the Github repo in a directory of your choice.

   git clone https://github.com/stefanzero/fruitpal.git

#. 
   Create a virtual environment, activate it, then install
   all dependencies

   .. code-block:: bash

       cd fruitpal
       python3.8 -m venv fruitpal-env
       source fruitpal-env/bin/activate
       pip install -r requirements.txt

#. 
   Run the server on your local machine

   .. code-block:: bash

      python3.8 manage.py runserver

Project Organization
^^^^^^^^^^^^^^^^^^^^

After cloning the git repo, the following directories are created:


* 
  fruitpal

  This contains the main Django application, that contains the settings
  (settings.py), web server python interface (wsgi.py), and main 
  URL path configurations (urls.py)

* 
  fruit_app

  This is the Django application which contains the specific Models and
  Views for the API.

* 
  static

  Django STATIC_ROOT directory, where static files from installed 
  packages such as REST_FRAMEWORK are copied to by the admin command:

  .. code-block:: bash

     python3.8 manage.py collectstatic

  For convenience, these files have already been included in the git 
  repo and the collectstatic does not need to be run.

* 
  staticfiles

  Directory in settings.STATICFILES_DIRS, where other static assets can
  be deployed from.  

* 
  docs

  This project is documented using the Python Sphinx package.  The docs
  directory contains the configuration files and .rst files 
  (restructured text) for Sphinx.

* 
  build

  This directory contains the output HTML files from Sphinx.

The main directory includes a number of Bash scripts and configuration
files:


* 
  install.sh

  Creates the virtual environment

* 
  create_docs.sh

  Runs Sphinx to create the documentation.  

* 
  requirements.txt

  The Python packages output from

  .. code-block:: bash

     pip freeze > requirements.txt

* 
  Makefile

  Unix file for the **make** utility for Sphinx.

* 
  manage.py

  Main entry point for Django.  

* 
  db.sqlite3

  Database file  

Data Schema
^^^^^^^^^^^

As described above in the section "Project Fruitpal API", the main data
consists of an array of values for each Commodity Data item:


* COUNTRY
* COMMODITY
* FIXED_OVERHEAD
* VARIABLE_COST

where COUNTRY is the standard 2-letter country code.  The standard list
of world countries rarely changes (South Sudan was the last addition), 
so it is easy to create a table to contain all the country codes and 
corresponding names.  The list of "commodities" is highly subjective to
change, and while a table could be made to contain these, at this time,
the data schema simply uses a string to represent the commodity.

For this project, the data schema consists of only 2 tables:

COUNTRY


* country_code (2-letter string, primary key)
* name (varchar, max length 64)

COMMODITY_DATA


* id (int)
* country_code (as a Foreign key to the COUNTRY table)
* commodity (varchar, max length 256)
* fixed_overhead (decimal 8.2)
* variable_cost (decimal 8.2)

The COMMODITY_DATA table has a constraint that the combination of 
country_code and commodity must be unique.  Since COMMODITY_DATA 
requires a foreign key to the COUNTRY table, the COUNTRY table is first 
fully populated before items are entered into COMMODITY_DATA.  

Sample Project Data
^^^^^^^^^^^^^^^^^^^

Several auxiliary programs are included that populate the database with
sample data.  These programs and their input data files are in the 
directory **fruitapp/scripts** and **fruitapp/scripts/sample_data**.  The
web site "delishably" was scraped to get a list of all "fruits", and 
used to create the sample data file "commodity-data.json".   Wikipedia
was to get a list of every country 2-letter code and country name.  

The Django package **django-extensions** is used to allow manage.py 
to execute Python "scripts" which actually load the data.  These have
already been run (and do not need to be run again), and the resulting
data is in the file db.sqlite3.

.. code-block:: bash

   python3.8 manage.py runscript add_countries
   python3.8 manage.py runscript create_commodity_data --script-args num_countries=5 num_fruits=40
   python3.8 manage.py runscript add_commodity_data

The values in the sample file "commodity-data.json" was created using 
random values for fixed_overhead and variable_cost.  Each commodity has
5 random countries chosen to create this sample file.  To test that 
the sample API result for the "calculate" endpoint matches
the result for "mango", the sample file commodity-data.json does not 
have any entries for mango.  Instead a separate Django script is used 
to load the values from the project description.

.. code-block:: bash

   python3.8 manage.py runscript add_mangos

Tests
^^^^^

The Unit Tests are in the directory fruit_app/tests for testing the 
models and the views.  They are run by:

.. code-block:: bash

   python3.8 manage.py test

Deployment and URLs
^^^^^^^^^^^^^^^^^^^

This Django Project has been deployed at:

`https://fruitpal.stefanzero.com <https://fruitpal.stefanzero.com>`_

The relative URLs are:


* 
  /

  Project landing page with links to API URLs

* 
  /static/html/index.html

  Documentation  

* 
  /api/v1/commoditydata/\ :raw-html-m2r:`<pk>`

  GET, DELETE and UPDATE for a given primary key (id) of a commoditydata item

* 
  /api/v1/commiditydata

  GET and POST for all items in commoditydata table

* 
  /api/v1/countries/\ :raw-html-m2r:`<country_code>`

  GET, DELETE and UPDATE for a given country_code of a country item

* 
  /api/v1/countries

  GET and POST for all items in countries table

* 
  /api/v1/calculate/?COMMODITY=commodity&TONS=tons&PRICE=price

  GET to calculate trade data for query parameters COMMODITY, TONS, and
  PRICE
