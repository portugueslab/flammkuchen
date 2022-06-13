from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("requirements_dev.txt") as f:
    required_dev = f.read().splitlines()

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Scientific/Engineering",
]

args = dict(
    name="flammkuchen",
    version="0.9.2",
    url="https://github.com/portugueslab/flammkuchen",
    description="Easy saving and loading of hdf5 files in python (forked from DeepDish)",
    maintainer="Luigi Petrucco, Vilim Stih @portugueslab",
    maintainer_email="luigi.petrucco@gmail.com",
    install_requires=required,
    extras_require=dict(dev=required_dev),
    packages=[
        "flammkuchen",
    ],
    license="BSD",
    classifiers=CLASSIFIERS,
)

setup(**args)
