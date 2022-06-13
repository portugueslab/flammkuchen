from __future__ import absolute_import, division, print_function

import os
from configparser import ConfigParser


def config():
    """
    Loads and returns a ConfigParser from ``~/.flammkuchen.conf``.
    """
    conf = ConfigParser()
    # Set up defaults
    conf.add_section("io")
    conf.set("io", "compression", "zlib")

    conf.read(os.path.expanduser("~/.flammkuchen.conf"))
    return conf
