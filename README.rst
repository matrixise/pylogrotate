pylogrotate
===========

Introduction
------------

A Logrotate Lexer for Pygments and Sphinx, this lexer is very simple and not
developed for a full cover of the logrotate grammar. Please you can contribute
to this project if you want to improve it.

.. _installation:

Installation
------------

.. code-block:: bash

    git clone git://github.com/matrixise/pylogrotate.git

    virtualenv ~/.virtualenvs/pylogrotate
    source ~/.virtualenvs/pylogrotate

    cd pylogrotate
    python setup develop

Usage
-----

.. _pygmentize:

Pygmentize
~~~~~~~~~~

If you want to use it with ``pygmentize``, just download it and install it in a
VirtualEnv, see :ref:`installation`.

    pygmentize -l logrotate -O full -f /tmp/test.html logrotate.conf

Sphinx
~~~~~~

In order to use it with Sphinx, just install it and define in your ``conf.py``
file a ``setup`` function as defined in the below example.

.. code-block:: python

    def setup(app):
       from pylogrotate.lexer import LogrotateLexer
       app.add_lexer('logrotate', LogrotateLexer())
