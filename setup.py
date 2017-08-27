#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='clb',
    version='0.0.1',
    description='Access to MLB game informations on terminal',
    author='prs-watch',
    url='https://github.com/prs-watch/CLB',
    packages=find_packages(),
    license='MIT License',
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3::only',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points="""
        [console_scripts]
        clb = clb.main:main
    """,
)