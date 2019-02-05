#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

install_requirements = [
    "sceptre>=2.0"
]

setup(
    name='sceptre-identify-resolver',
    version="1.0.0",
    description="A set of Sceptre resolvers to help identify stacks",
    py_modules=['stack_name','stack_env'],
    long_description=readme,
    long_description_content_type="text/markdown",
    author="zaro0508",
    author_email="zaro0508@gmail.com",
    license='Apache2',
    url="https://github.com/cloudreach/sceptre",
    entry_points={
        'sceptre.resolvers': [
            'stack_name = stack_name:StackName',
            'stack_env = stack_env:StackEnvironment',
        ],
    },
    keywords="sceptre",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    install_requires=install_requirements,
    include_package_data=True,
    zip_safe=False,
)
