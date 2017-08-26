#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='clb',
    version='0.0.1',
    description='CommandLine Baseball',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points="""
        [console_scripts]
        clb = clb.main:main
    """,
)