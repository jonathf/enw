"""
Main functions performing parsing and executing program.
"""
import sys
import os
import shutil
import argparse
import argcomplete
import re

RCFILE = os.path.join(".enw")


def adjust_autoenv(pypath):
    """
    Add path to virtual enviroment to `.env` file.

    The function will either create file if it doesn't exists,
    replace old source lines, or append if none is found.

    Args:
        pypath (str) : path to the python virtual enviroment folder.
    """
    actpath = os.path.abspath(
        os.path.join(pypath, "bin", "activate"))
    source_line = "source %s" % actpath

    if not os.path.isfile(".env"):
        with open(".env", "w") as dst:
            dst.write(source_line)
    else:
        with open(".env") as src:
            env = src.read()
        regex = r"^source .*\.py\d+%sbin%sactivate$" % (os.sep, os.sep)
        if re.findall(regex, env):
            env = re.sub(regex, source_line, env)
            with open(".env", "w") as dst:
                dst.write(env)
        else:
            with open(".env", "a") as dst:
                dst.write(env)


def pip_install(pypath):
    """
    Pip install default programs from `.enw` file if it exists.

    Args:
        pypath (str) : path to the python virtual enviroment folder.
    """
    pippath = os.path.abspath(os.path.join(pypath, "bin", "pip"))

    cmd = "%s install -U pip" % pippath
    print(cmd)
    os.system(cmd)

    curdir = curdir_saved = os.path.abspath(os.path.curdir)
    stack = []
    while True:
        path = os.path.join(curdir, RCFILE)
        if os.path.isfile(path):
            stack.insert(0, path)

        path = os.path.abspath(os.path.join(curdir, os.path.pardir))
        if curdir == path:
            break
        curdir = path

    for rcfile in stack:

        os.chdir(os.path.dirname(rcfile))
        with open(rcfile) as src:
            lines = src.readlines()
        for line in lines:
            cmd = "%s install %s" % (pippath, line)
            print(cmd)
            os.system(cmd)

    os.chdir(curdir_saved)


def run_args(version=3, force=False, install_pip=False, **kwargs):
    """
    Run main program.

    Args:
        version (int, float) : The python version number to one decimal.
        force (bool) : Override old python enviroment if exist.
        install_pip (bool) : Install programs with pip from `~/.enw`.
    """
    if version == int(version):
        version = "%d" % version
    else:
        version = "%1.1f" % version
    pypath = ".py%s" % version.replace(".", "")

    if force and os.path.isdir(pypath):
        shutil.rmtree(pypath)

    if not os.path.isdir(pypath):
        cmd = "virtualenv -p python%s %s" % (version, pypath)
        print(cmd)
        os.system(cmd)

    adjust_autoenv(pypath)
    if install_pip:
        pip_install(pypath)


def set_args(parser):
    """
    Attach arguments to parser.

    Args:
        parser (ArgumentParser) : parser to attach arguments to.
    """
    parser.add_argument(
        "-f", "--force", action="store_true",
        help="override old envirmonment."
    )
    parser.add_argument(
        "-i", "--install-pip", action="store_true",
        help="install packages from `~/.enw`"
    )
    parser.add_argument(
        "version", type=float, nargs="?", default=3,
        help="python version"
    )
    parser.set_defaults(func=run_args)


def run_command(args):
    """
    Run commands as if on the command line.

    Args:
        args (str, list) : Command flags to be parsed.
    """
    if isinstance(args, str):
        args = args.split(" ")

    parser = argparse.ArgumentParser(description="enw")
    set_args(parser)
    argcomplete.autocomplete(parser)
    args = parser.parse_args(args)
    args.func(**vars(args))
