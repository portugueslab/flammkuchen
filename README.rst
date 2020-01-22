.. image:: https://travis-ci.org/portugueslab/flammkuchen.svg?branch=master
    :target: https://travis-ci.org/portugueslab/flammkuchen

.. image:: https://img.shields.io/pypi/v/flammkuchen.svg
    :target: https://pypi.python.org/pypi/flammkuchen
   
.. image:: https://img.shields.io/badge/license-BSD%203--Clause-blue.svg?style=flat
    :target: http://opensource.org/licenses/BSD-3-Clause 


Flammkuchen
===========

Library for flexible HDF5 saving/loading. It was forked from the `deepdish library <https://github.com/uchicago-cs/deepdish>`_
from the University of Chicago to maintain its convenient i/o module.


Installation
------------
::

    pip install flammkuchen




Main feature
------------
The primary feature of flammkuchen (ex deepdish) is its ability to save and load all kinds of
data as HDF5. It can save any Python data structure, offering the same ease of
use as pickling or `numpy.save <http://docs.scipy.org/doc/numpy/reference/generated/numpy.save.html>`__.
However, it improves by also offering:

- Interoperability between languages (HDF5 is a popular standard)
- Easy to inspect the content from the command line (using ``h5ls`` or our
  specialized tool ``ddls``)
- Highly compressed storage (thanks to a PyTables backend)
- Native support for scipy sparse matrices and pandas ``DataFrame`` and ``Series``
- Ability to partially read files, even slices of arrays

An example:

.. code:: python

    import flammkuchen as fl

    d = {
        'foo': np.ones((10, 20)),
        'sub': {
            'bar': 'a string',
            'baz': 1.23,
        },
    }
    fl.save('test.h5', d)

This can be reconstructed using ``fl.load('test.h5')``, or inspected through
the command line using either a standard tool::

    $ h5ls test.h5
    foo                      Dataset {10, 20}
    sub                      Group

Or, better yet, our custom tool ``ddls`` (or ``python -m fl.ls``)::

    $ ddls test.h5
    /foo                       array (10, 20) [float64]
    /sub                       dict
    /sub/bar                   'a string' (8) [unicode]
    /sub/baz                   1.23 [float64]

Further, one can use the metadata dynamically in a python script to load
a subset of data with an unknown shape:

.. code:: python

    import flammkuchen as fl

    foo_shape = fl.meta("test.h5", "/foo").shape
    # (10, 20)

    for i in range(foo_shape[0]):
        a_tiny_slice = fl.load("test.h5", "/foo", sel=fl.aslice[i, :])
        print(a_tiny_slice.shape)
        # (20, ) 

Read more at `Saving and loading data <https://github.com/portugueslab/flammkuchen/blob/master/io.rst>`__.

