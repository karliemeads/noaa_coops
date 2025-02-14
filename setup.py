# Read the contents of README.md file
from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="noaa_coops",
    version="0.1.10",
    description="Python wrapper for NOAA Tides & Currents Data and Metadata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GClunies/noaa_coops",
    author="Greg Clunies",
    author_email="greg.clunies@gmail.com",
    license="GNU GPL",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["noaa_coops"],
    install_requires=["requests", "numpy", "pandas>=1.1.3", "zeep"],
    zip_safe=False,
)
