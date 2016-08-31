#!/usr/bin/env python
"""
Simple script for quick install of virtual environment that places under
autoenv and initiate a default installation from `.envmgrrc`.
"""

import sys
import os
from setuptools import setup, find_packages

if os.environ.get("VIRTUAL_ENV", ""):
    print("please install envmgr outside virtual environment.")
    sys.exit(1)

setup(
    name="envmgr",
    version="0.1",
    description=\
    "Tool for autmoatically administrating python virtual environment",
    author="Jonathan Feinberg",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['envmgr = envmgr.__main__:main']},
    install_requires=[
        "virtualenv", "autoenv"
    ],
)
