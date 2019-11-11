``enw`` - Environment Wrapper
=============================

``enw`` is a wrapper tool for quick creation and switching between different
python virtual environments. In particular it allows for:

* Quick creation of new environments using ``virtualenv``.
* Automatic linking of said environment ``autoenv``, but without destroying local autoenv directives.
* Quick switching between python installation.
* Auto pip installation of programs that you know you want in all new environments (like e.g. ``ipython``).
* Quick reinstallations.

Obviously, all of this can be done by hand, but the idea is to simplify the
process that you keep doing many times, and do so in a way that is tractable.

Note that the core functionality of ``enw`` adds and replaces what python to
source in ``.env`` files. It does so carefully so that other content that you
may have added to the file is not affect.

Installation
------------

To install, run the following outside of any virtual environment::

    pip instal enw

This will install the dependencies ``virtualenv`` and ``autoenv``. The latter
has to be activated (as normal) by running something like::

    echo "source `which activate.sh`" >> ~/.bashrc

or if on a mac::

    echo "source `which activate.sh`" >> ~/.bash_profile

``enw`` will install environments, but by default will not activate them. If
you want it to also handle activation, you need to add a trigger for
``autoenv`` like so::

    echo "function enw(){ envwrap "$@";autoenv_init; }" >> ~/.bash_aliases

(Make sure that ``.bashrc``/``.bash_profile`` sources the content of
``.bash_aliases`` for this to work.)

Usage
-----

For basic usage, run the basic wrapper::

    enw

It will create a virtual environment (which default to ``python3``) under the
folder name ``.py3``. A line sourcing of the file ``.py3/bin/activate`` will be
placed in a file ``.env``. This will activate the environment everytime you
enter the folder or one of its subfolders.

If you want to use another python version, this is possible by
adding a positional version number. For example::

    enw 2.7

It will then repeat the whole process, but with the folder ``.py27``. To switch
back to Python 3 setup, just run::

    enw 3

If you *do* want to reinstall an environment, this is also possible::

    enw -f 2.7

In addition, if if is possible to use ``enw`` to install a suite of standard
packages. By including a ``-i`` flag, ``enw`` will look for the file
``.enw`` recursivly in the current directory and bellow it (much like
``autoenv``) and install its content using ``pip install -r``, using the newly
installed virtual environment.
