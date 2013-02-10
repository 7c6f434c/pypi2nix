# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import os


setup(
    name = "python2nix",
    version = "0.0.1",
    author = u"Rok Garbas, Cillian de Róiste",
    description = (
        "Scripts and tools to help create nix package expressions for "
        "python projects"),
    license = "GPL",
    keywords = "NixOS Nix Packaging",
    url = "http://nixos.org",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
    ],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'distutils2',
    ],
    entry_points = {
        'console_scripts': ['buildout2nix = python2nix:buildout2nix',],
    }
)
