__version__ = "0.9.2"


# Load the following modules by default
from flammkuchen.conf import config
from flammkuchen.hdf5io import (
    Compression,
    ForcePickle,
    aslice,
    load,
    meta,
    save,
)

__all__ = ["load", "save", "ForcePickle", "Compression", "aslice", "config", "meta"]
