#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='edx-drf-extensions',
    version='0.1.1',
    description='edX extensions of Django REST Framework',
    author='edX',
    url='https://github.com/edx/edx-drf-extensions',
    license='AGPL',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
    packages=['edx_rest_framework_extensions'],
    install_requires=[
        'django>=1.8.9,<1.10',
        'djangorestframework>=3.2.3,<4.0.0',
        'python-dateutil>=2.0',
        'requests>=2.7.0,<3.0.0',
    ],
)