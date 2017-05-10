import os
import setuptools
# -*- coding: utf-8 -*-
## PyHum (Python program for Humminbird(R) data processing) 
## has been developed at the Grand Canyon Monitoring & Research Center,
## U.S. Geological Survey
##
## Author: Daniel Buscombe
## Project homepage: <https://github.com/dbuscombe-usgs/PyHum>
##
##This software is in the public domain because it contains materials that originally came from 
##the United States Geological Survey, an agency of the United States Department of Interior. 
##For more information, see the official USGS copyright policy at 
##http://www.usgs.gov/visual-id/credit_usgs.html#copyright
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.

#"""
# ____        _   _                         
#|  _ \ _   _| | | |_   _ _ __ ___    _   _ 
#| |_) | | | | |_| | | | | '_ ` _ \  (_) (_)
#|  __/| |_| |  _  | |_| | | | | | |  _   _ 
#|_|    \__, |_| |_|\__,_|_| |_| |_| (_) (_)
#       |___/                               
#
##+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
#|b|y| |D|a|n|i|e|l| |B|u|s|c|o|m|b|e|
#+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|d|b|u|s|c|o|m|b|e|@|u|s|g|s|.|g|o|v|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
#|U|.|S|.| |G|e|o|l|o|g|i|c|a|l| |S|u|r|v|e|y|
#+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+

#"""

"""
PyHum - a Python framework for sidescan data texture classification.

PyHum is an open-source project dedicated to provide a Python framework for
processing low-cost sidescan data. It provides parsers for Humminbird file formats,
and signal processing routines which allow the manipulation of sidescan data and automated texture classification 

For more information visit http://dbuscombe-usgs.github.io/PyHum/

:install:
    python setup.py install
    sudo python setup.py install
    
:test:
    python -c "import PyHum; PyHum.test.dotest()"

:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
    
    This software is in the public domain because it contains materials that
    originally came from the United States Geological Survey, an agency of the
    United States Department of Interior. For more information, 
    see the official USGS copyright policy at
    http://www.usgs.gov/visual-id/credit_usgs.html#copyright
    Any use of trade, product, or firm names is for descriptive purposes only 
    and does not imply endorsement by the U.S. government.
    
"""

setuptools.setup(
    name='PyHum',
    version='0.0.1',
    packages=setuptools.find_packages(),
    package_data={'PyHum': ['*.SON', '*.DAT','*.h', '*.IDX', '*.txt', '*.png']},
    description='Python/Cython scripts to read Humminbird DAT and associated SON files, export data, carry out rudimentary radiometric corrections to data, and classify bed texture using the algorithm detailed in Buscombe, Grams, Smith, (2015) "Automated riverbed sediment classification using low-cost sidescan sonar", Journal of Hydraulic Engineering, 10.1061/(ASCE)HY.1943-7900.0001079, 06015019',
    long_description=open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'README.md')).read(),

    license = "GNU GENERAL PUBLIC LICENSE v3",
    keywords='sidescan sonar humminbird sediment substrate classification',
    author='Daniel Buscombe',
    author_email='dbuscombe@usgs.gov',
    url='https://github.com/dbuscombe-usgs/PyHum',
    download_url ='https://github.com/dbuscombe-usgs/PyHum/archive/master.zip',
    install_requires = ['numpy','scipy','Pillow',
                        'matplotlib', 'cython', 'pyproj', 'scikit-image', 
                        'simplekml', 'joblib', 'basemap', 'scikit-learn', 
                        'pyresample', 'dask', 'toolz', 'pandas'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Topic :: Scientific/Engineering'],
)
