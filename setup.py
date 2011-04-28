#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "colorex",
    version = "2.0",
    author = "Julien Antony",
    author_email = "julien.antony@scopart.fr",
    description = ("console tool that displays files highlighting some patterns with colors"),
    license = "GPLv3",
    keywords = "log color logfile",
    url = "http://www.scopart.fr/index.php/colorex/",
    scripts=['colorex'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Topic :: System",
        "License :: OSI Approved :: GNU General Public License (GPL)",

    ],
)
