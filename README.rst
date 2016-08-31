envmgr - Environment Manager
----------------------------

``envmgr`` is a simple wrapper for creating a python virtual environment using
``virtualenv``. In addition it creates a local ``autoenv`` file that contains
a sourcing commands for said virtual environment. Lastly it will automatically
install a suite of default tools over ``pip`` from your newly installed virtual
environment, without activating it.

Obviously, all of this can be done by hand, but the idea is to simplify the
process that you keep doing many times. This includes installing default tools
that you normally always want to have in an virtual environment. (In my case
that entails ``ipython``, ``pylint`` and ``pydocstyle``.)

Installation
------------

To install, just run the following outside of any virtual environment::

    python setup.py install

This will install the dependencies ``virtualenv`` and ``autoenv``. The latter
has to be activated (as normal) by running something like::

    echo "source `which activate.sh`" >> ~/.bashrc

or if on a mac::

    echo "source `which activate.sh`" >> ~/.bash_profile

``envmgr`` will install environments, but by default will not activate them. If
you want it to also handle activation, by adding a trigger for ``autoenv``::

    echo "alias envmgr=\"envmgr && autoenv_init\"" >> ~/.bash_aliases

(This assumes that ``.bashrc``/``.bash_profile`` somehow sources the content of
``.bash_aliases``.)

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
Python. It does this by editing the content of ``.env`` file. It does so as
best as it can such that any user generated content stays intact.

If however, you *do* want to reinstall an environment, this is also possible::

    envmgr -f 2.7
