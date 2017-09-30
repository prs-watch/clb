#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='commandline-baseball',
    version='1.0.0',
    description='Access to MLB game informations on terminal',
    author='prs-watch',
    author_email='prs_watch@excite.co.jp',
    url='https://github.com/prs-watch/commandline-baseball',
    packages=['clb','clb.scraper'],
    license='MIT License',
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points="""
        [console_scripts]
        clb = clb.main:main
    """,
)
