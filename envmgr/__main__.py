import sys
import os
import shutil
import argparse

RCFILE = os.path.join(os.path.expanduser("~"), ".envmgrrc")


def run_args(version=3, force=False, **kwargs):

    # run outside env:
    if os.environ.get("VIRTUAL_ENV", ""):
        os.system("deactivate && " + " ".join(sys.argv))
        sys.exit(0)

    if version == int(version):
        version = "%d" % version
    else:
        version = "%1.1f" % version
    pypath = ".py%s" % version

    if force and os.path.isdir(pypath):
        shutil.rmtree(pypath)

    if not os.path.isdir(pypath):

        os.system("virtualenv -p python%s %s" % (version, pypath))
        actpath = os.path.abspath(
            os.path.join(pypath, "bin", "activate"))
        os.system('echo "source %s" > .env' % actpath)

    pippath = os.path.join(pypath, "bin", "pip")

    cmd = "%s install -U pip" % pippath
    print(cmd)
    os.system(cmd)

    if os.path.isfile(RCFILE):
        cmd = "%s isntall -r %s" % (pipfile, RCFILE)
        print(cmd)
        os.system(cmd)


def set_args(parser):
    parser.add_argument(
        "-f", "--force", action="store_true",
        help="override old envirmonment."
    )
    parser.add_argument(
        "-I", "--skip-install", action="store_true",
        help="do not load installes from `~/.envmgrrc`"
    )
    parser.add_argument(
        "version", type=float, nargs="?", default=3,
        help="python version"
    )
    parser.set_defaults(func=run_args)


def main():
    parser = argparse.ArgumentParser(description="envmgr")
    set_args(parser)
    args = parser.parse_args()
    args.func(**vars(args))
