# -*- coding: utf-8 -*-
# setup.py
# ~~~~~~~~
# Copyright 2013 - Stephane Wirtel <stephane@wirtel.be>
#
from setuptools import setup, find_packages

setup(
    name='pylogrotate',
    version='0.0.1',
    author='Stephane Wirtel',
    author_email='stephane@wirtel.be',
    packages=find_packages(),
    install_requires=['pygments'],
    entry_points = """
    [pygments.lexers]
    logrotate = pylogrotate.lexer:LogrotateLexer
    """
)
