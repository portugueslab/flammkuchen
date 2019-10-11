#!/usr/bin/env python
from __future__ import division, print_function, absolute_import 

from setuptools import setup
import os

if os.getenv('READTHEDOCS'):
    with open('requirements_docs.txt') as f:
        required = f.read().splitlines()
else:
    with open('requirements.txt') as f:
        required = f.read().splitlines()

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Scientific/Engineering',
]

args = dict(
    name='flammkuchen',
    version='0.3.4',
    url="https://github.com/uchicago-cs/flammkuchen",
    description="Deepdish fork for easy saving and loading of hdf5 files in python",
    maintainer='Luigi Petrucco, Vilim Stih @portugueslab',
    maintainer_email='luigi.petrucco@gmail.com',
    install_requires=required,
    extras_require={
        'image': ["skimage"],
    },
    scripts=['scripts/ddls'],
    packages=[
        'flammkuchen',
        'flammkuchen.parallel',
        'flammkuchen.io',
        'flammkuchen.util',
    ],
    license='BSD',
    classifiers=CLASSIFIERS,
)

setup(**args)
