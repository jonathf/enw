envmgr - Environment Manager
----------------------------

``envmgr`` is a simple wrapper for creating a python virtual environment using
``virtualenv``, then creates a local ``autoenv`` source link in the same
folder, and installes all the default tools that you want in every environment
(like e.g. ipython).

Installation
------------

To install, just run::

    python setup.py install

This will install the dependencies ``virtualenv`` and ``autoenv``. The latter
has to be activated by as normal by running something like::

    echo "source ``which activate.sh``" >> ~/.bashrc

or if on mac::

    echo "source ``which activate.sh``" >> ~/.bash_profile

The script is designed only to work on Linux and Mac.

Usage
-----

For basic usage, just run the basic wrapper::

    envmgr 3

It will create a virtual environment under the folder name ``.py3``. Sourcing
of the file ``.py3/bin/activate`` wil be placed in a file ``.env``. This will
activate the environment everytime you enter the folder or one of its
subfolders.

In addition, the script will look for the file ``~/.envmgrrc``. It will read
this file and install its content using ``.py3/bin/pip install -r`` as if it
was a ``requirements.txt`` file.

Obviously, if you want to use another python version, this is possible by
changing the number. For example::

    envmgr 2.7

For other options to the tool, run::

    envmgr -h
