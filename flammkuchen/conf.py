from __future__ import division, print_function, absolute_import
import os
import sys
from configparser import ConfigParser


def config():
    """
    Loads and returns a ConfigParser from ``~/.flammkuchen.conf``.
    """
    conf = ConfigParser()
    # Set up defaults
    conf.add_section('io')
    conf.set('io', 'compression', 'zlib')

    conf.read(os.path.expanduser('~/.flammkuchen.conf'))
    return conf
