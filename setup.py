#!/usr/bin/env python3 -u
# -*- coding: utf-8 -*-
# copyright: scikit-risk developers, BSD-3-Clause License (see LICENSE file)
"""Install script for scikit-risk."""

import codecs
import os
import re

import setuptools

__author__ = ["RNKuhns"]


# Inspired by scikit-learn and sktime setup.py files
def read(*parts):
    """Read a file.

    intentionally *not* adding an encoding option to open, See:
    https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    """
    with codecs.open(os.path.join(HERE, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    """Find the version."""
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


MIN_PYTHON_VERSION = "3.7"
MIN_REQUIREMENTS = {
    "numpy": "1.19.3",
    "pandas": "1.1.0",
    "scikit-learn": "1.0.0",
    "statsmodels": "0.12.1",
    "numba": "0.53",
}
MAX_REQUIREMENTS = {
    "statsmodels": "0.12.1",
}

HERE = os.path.abspath(os.path.dirname(__file__))

WEBSITE = "https://github.com/RNKuhns/scikit-risk"
DISTNAME = "scikit-risk"
DESCRIPTION = "A unified Python toolbox for credit risk analysis"
with codecs.open("README.md", encoding="utf-8-sig") as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = "R. Kuhns"
MAINTAINER_EMAIL = "rnkuhns@gmail.com"
URL = WEBSITE
LICENSE = "BSD-3-Clause"
DOWNLOAD_URL = "https://pypi.org/project/scikit-risk/#files"
PROJECT_URLS = {
    "Issue Tracker": "https://github.com/RNKuhns/scikit-risk/issues",
    "Documentation": WEBSITE,
    "Source Code": "https://github.com/RNKuhns/scikit-risk/",
}
VERSION = find_version("skrisk", "__init__.py")
PACKAGES = setuptools.find_packages(exclude=("tests"))
INSTALL_REQUIRES = [
    *[
        "{}>={}".format(package, version)
        for package, version in MIN_REQUIREMENTS.items()
    ],
    *[
        "{}<={}".format(package, version)
        for package, version in MAX_REQUIREMENTS.items()
    ],
    "wheel",
]
TESTS_REQUIRES = ["pytest"]
CLASSIFIERS = [
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Scientific/Engineering",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]

SETUP_REQUIRES = ["wheel"]

# Optional setuptools features
# For some commands, use setuptools
SETUPTOOLS_COMMANDS = {
    "install",
    "develop",
    "release",
    "build_ext",
    "bdist_egg",
    "bdist_rpm",
    "bdist_wininst",
    "install_egg_info",
    "build_sphinx",
    "egg_info",
    "easy_install",
    "upload",
    "bdist_wheel",
    "--single-version-externally-managed",
    "sdist",
}

setuptools.setup(
    name=DISTNAME,
    version=VERSION,
    packages=PACKAGES,
    url=URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    license=LICENSE,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRES,
    python_requires=">={}".format(MIN_PYTHON_VERSION),
)
