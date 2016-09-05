#!/usr/bin/env python
"""
Simple script for quick install of virtual environment that places under
autoenv and initiate a default installation from `.enwrc`.
"""

from setuptools import setup, find_packages

setup(
    name="enw",
    version="0.2",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'enw = enw.__main__:main',
            'envwrap = enw.__main__:main',
        ]},
    install_requires=[
        "virtualenv", "autoenv", "argcomplete"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='virtualenv autoenv configuration',
    description=\
    "Tool for simple administrating of multiple python virtual environment "\
    "with virtualenv and autoenv.",
    author="Jonathan Feinberg",
    author_email="jonathf@gmail.com",
    license="GPL3",
    url="https://github.com/jonathf/enw",
)
