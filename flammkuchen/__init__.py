# Load the following modules by default
from flammkuchen.conf import config
try:
    import tables
    _pytables_ok = True
    del tables
except ImportError:
    _pytables_ok = False

if _pytables_ok:
    from flammkuchen.hdf5io import load, save, ForcePickle, Compression
else:
    def _f():
        raise ImportError("You need PyTables for this function")
    load = save = _f


class MovedPackage(object):
    def __init__(self, old_loc, new_loc):
        self.old_loc = old_loc
        self.new_loc = new_loc

    def __getattr__(self, name):
        raise ImportError('The package {} has been moved to {}'.format(
            self.old_loc, self.new_loc))

# This is temporary: remove after a few minor releases
__all__ = ['load', 'save', 'ForcePickle', 'Compression']

#
# __all__ = ['set_verbose',
#            'info',
#            'warning',
#            'bytesize',
#            'humanize_bytesize',
#            'memsize',
#            'span',
#            'apply_once',
#            'tupled_argmax',
#            'multi_range',
#            'config',
#            'timed',
#            'aslice',
#            ]

VERSION = (0, 9, 0)
ISRELEASED = False
__version__ = '{0}.{1}.{2}'.format(*VERSION)
if not ISRELEASED:
    __version__ += '.git'
