# Load the following modules by default
from flammkuchen.conf import config
try:
    import tables
    _pytables_ok = True
    del tables
except ImportError:
    _pytables_ok = False

if _pytables_ok:
    from flammkuchen.hdf5io import load, save, ForcePickle, Compression, aslice, meta
else:
    def _f():
        raise ImportError("You need PyTables for this function")
    load = save = _f

__all__ = ['load', 'save', 'ForcePickle', 'Compression', 'aslice', 'config', 'meta']


VERSION = (0, 9, 0)
ISRELEASED = False
__version__ = '{0}.{1}.{2}'.format(*VERSION)
if not ISRELEASED:
    __version__ += '.git'
