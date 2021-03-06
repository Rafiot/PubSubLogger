#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pubsublogger',
    version='1.2.2',
    author='Raphaël Vinot',
    author_email='raphael.vinot@circl.lu',
    maintainer='Raphaël Vinot',
    url='https://github.com/Rafiot/PubSubLogger',
    description='Logging system using the PubSub functionality of Redis.',
    packages=['pubsublogger'],
    scripts=['log_subscriber'],
    test_suite="test",
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Logging'
    ],
    install_requires=['redis', 'logbook']
)
