#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
"""
Front end skript.
"""
import sys

from .parser import run_command


def main():
    """Main command used by `setuptools`."""
    run_command(sys.argv[1:])
