#!/bin/bash

# This script converts Markdown to Restructured Text for the creating
# documentation using the Python Sphinx package.

# Installation of Fruitpal is described in Readme.md and
# build/html/index.html

# The virtual environment must be activated before running this script.
mdToRst Readme.md > docs/Readme.rst
