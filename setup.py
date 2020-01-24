#!/usr/bin/env python

import re
import setuptools

from os import path

base_dir = path.abspath(path.dirname(__file__))

with open(path.join(base_dir, 'README.md')) as f:
    long_description = f.read()

with open(path.join(base_dir, 'flask_fontawesome', '__init__.py')) as f:
    version = re.search("^__version__ = '(?P<version>.*)'$",
                        f.read(),
                        re.MULTILINE).group('version')

setuptools.setup(
    name='Flask-FontAwesome',
    version=version,
    author='heartsucker',
    author_email='heartsucker@autistici.org',
    url='https://github.com/heartsucker/flask-fontawesome',
    description='FontAwesome for Flask',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'flask_fontawesome': 'flask_fontawesome'},
    packages=['flask_fontawesome'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    python_requires='>=3.5',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ),
)
