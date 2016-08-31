envmgr - Environment Manager
----------------------------

``envmgr`` is a simple wrapper for creating a python virtual environment using
``virtualenv``. In addition it creates a local ``autoenv`` file that contains
a sourcing commands for said virtual environment. On top of that it can then
automatically install a set of default tools over ``pip`` from your newly
installed virtual environment, without activating it.

Obviously, all of this can be done by hand, but the idea is to simplify the
process that you keep doing every time, include installing default tools that
you normally always use. (In my case that entails ``ipython``, ``pylint`` and
``pydocstyle``.)

Installation
------------

To install, just run::

    python setup.py install

This will install the dependencies ``virtualenv`` and ``autoenv``. The latter
has to be activated (as normal) by running something like::

    echo "source ``which activate.sh``" >> ~/.bashrc

or if on a mac::

    echo "source ``which activate.sh``" >> ~/.bash_profile

The script is designed only to work on Linux and Mac.

Usage
-----

For basic usage, just run the basic wrapper::

    envmgr

It will create a virtual environment (which default to ``python3``) under the
folder name ``.py3``. Sourcing of the file ``.py3/bin/activate`` will be placed
in a file ``.env``. This will activate the environment everytime you enter the
folder or one of its subfolders.

In addition, the script will look for the file ``~/.envmgrrc``. It will read
this file and install its content using ``pip install -r`` as if it
was a ``requirements.txt`` file using the newly installed virtual environment.

If you want to use another python version, this is possible by
adding a positional version number. For example::

    envmgr 2.7

By default, the wrapper do not reinstall the virtual environment. This implies
that ``envmgr`` can be used to quickly switching between different versions of
Python. It does this by rewriting the content of ``.env`` file.

If however, you do want to reinstall an environment, this is also possible::

    envmgr -f 2.7
