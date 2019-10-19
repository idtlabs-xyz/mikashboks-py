#!/usr/bin/env python
from setuptools import setup, find_packages

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession

# LONG_DESCRIPTION = open('README.rst').read()
REQUIREMENTS = [str(ir.req) for ir in parse_requirements('requirements.txt', session=PipSession())
                if not (getattr(ir, 'link', False) or getattr(ir, 'url', False))]

setup(
    name='mikashbokspy',
    version='0.0.7',
    description='Common python utilities for mikashboks microservices in a aws lambda environment',
    author='Salton Massally',
    author_email='smassally@idtlabs.xyz',
    url='https://github.com/idtlabs-xyz/mikashboks-py',
    packages=find_packages(exclude=['tests']),
    platforms=['any'],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
