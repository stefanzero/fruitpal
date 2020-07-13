
Requirements
^^^^^^^^^^^^

This Django Rest-Framework application was developed with Python 3.8, 
but it will probably work with any Python version >= 3.6.  In the code
samples below, python3.8 can be replaced with python3.6 or python3.7.


.. image:: https://fruitpal.stefanzero.com/static/project-fruitpal.jpg
   :target: https://fruitpal.stefanzero.com/static/project-fruitpal.jpg
   :alt: Project Fruitpal


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

  This directory contains the files for the

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

Sample Project Data
^^^^^^^^^^^^^^^^^^^

Several auxiliary programs are included that populate the database with
sample data.  These programs and their input data files are in the 
directory **fruitapp/scripts** and **fruitapp/scripts/sample_data**.

The Django package **django-extensions** is used to allow manage.py 
to execute Python "scripts" which actually load the data.  These have
already been run (and do not need to be run again), and the resulting
data is in the file db.sqlite3.

.. code-block:: bash

   python3.8 manage.py runscript add_countries
   python3.8 manage.py runscript add_commodity_data

Tests
^^^^^

The Unit Tests are in the directory fruit_app/tests for testing the 
models and the views.  They are run by:

.. code-block:: bash

   python3.8 manage.py test
