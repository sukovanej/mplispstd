#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='mplispstd',
    version='0.1',
    packages=[
        'mplispstd',
        'mplispstd.io',
        'mplispstd.math',
        'mplispstd.python',
        'mplispstd.string',
        'mplispstd.env',
    ],
    install_requires=[
        'mplisp',
    ]
)
