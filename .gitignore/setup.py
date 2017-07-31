#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='persistQstore',
    version=__import__('persistQstore').__version__,
    description=(
        ' disk based persistent queue in Python.'
    ),
    long_description=open('README.rst').read(),
    author='Ranjith',
    author_email='ranjith@dataglen.com',
    maintainer='Ranjith',
    maintainer_email='ranjith@dataglen.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
