#!/bin/bash

# This script:
# 1. loads the virtual environment
# 2. removes previous converted Readme file
# 3. runs m2r to convert markdown Readme.md to Readme.rst
# 4. move Readme.rst to docs/
# 5. runs the Sphinx makefile to create the documentation

source fruitpal-env/bin/activate
rm README.rst 2> /dev/null
m2r README.md
mv README.rst docs
make html
