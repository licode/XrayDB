#!/usr/bin/env python
import os
import sys
import shutil
from setuptools import setup

dbfile = 'xraydb.sqlite'

required_modules = ('sqlalchemy', 'json', 'numpy', 'scipy')
def check_dependencies(modules):
    missing = []
    for mod in modules:
        try:
            x = __import__(mod)
        except ImportError:
            missing.append(mod)

    if len(missing) > 0:
        print('The following python packages are needed to use xraydb.py:')
        print(' ')
        print('      %s ' % ('and '.join(missing)))
        print(' ')
        print(' Please install these and try again.')
        sys.exit(1)

check_dependencies(required_modules)

# copy db from ../.. to xraydb
shutil.copy(os.path.join('..', '..', dbfile),
            os.path.join('xraydb', dbfile))

setup(name = 'xraydb',
      version = '1.0.1',
      author = 'Matthew Newville',
      author_email = 'newville@cars.uchicago.edu',
      url          = 'http://github.com/XraySpectroscopy/XrayDB',
      download_url = 'http://github.com/XraySpectroscopy/XrayDB',
      requires = ('numpy', 'sqlalchemy'),
      license = 'BSD',
      description = "X-ray Reference Data for the Elements",
      platforms = ('Windows', 'Linux', 'Mac OS X'),
      classifiers=['Intended Audience :: Science/Research',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering'],
      package_dir = {'xraydb': 'xraydb'},
      packages = ['xraydb'],
      package_data = {'xraydb': [dbfile]})
