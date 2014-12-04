#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = "0.0.1"

with open("README.rst") as f:
    long_description = f.read() + '\n'

setup(
    name='subile',
    version=__version__,
    license='MIT',
    description='Download subtitles in multiple languages from the terminal',
    long_description=long_description,
    keywords="subtitles video caption media watch show film documentary",
    url='https://github.com/marcwebbie/subile',
    author='Marcwebbie',
    author_email='marcwebbie@gmail.com',
    scripts=["bin/subile"],
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    test_suite='tests.test',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Video',
        'Topic :: Internet',
    ],
)
