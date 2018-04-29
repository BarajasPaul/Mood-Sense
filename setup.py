#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Mood-Sense',
    version='1.0',
    description='Python Flask Training',
    author='Paul Barajas',
    author_email='paul.barajas@linux.com',
    url='https://github.com/BarajasPaul/Mood-Sense',
    packages=['flask', 'passlib', 'flask-mongoengine', 'flask_httpauth'],
)
