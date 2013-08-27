# -*- coding: utf-8 -*-
# setup.py
# ~~~~~~~~
# Copyright 2013 - Stephane Wirtel <stephane@wirtel.be>
#
from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import *

class LogrotateLexer(RegexLexer):
    name = 'Logrotate configuration file'
    aliases = ['logrotate']
    filenames = []
    mimetypes = ['text/x-logrotate-conf']

    tokens = {
        'root': [
            (r'/[^\s;#]*', Name, 'stmt'), # pathname
            include('base')
        ],
        'block': [
            (r'[a-z]+', Keyword),
            (r'}', Punctuation),
            include('base'),
        ],
        'stmt': [
            (r'{', Punctuation, 'block'),
            include('base')
        ],
        'base': [
            (r'[0-9]+\b', Number.Integer),
            (r'#.*\n', Comment.Single),
            (r'([a-z0-9.-]+)(:)([0-9]+)', bygroups(Name, Punctuation, Number.Integer)),
            (r'/[^\s;#]*', Name), # pathname
            (r'\s+', Text),
        ]
    }


