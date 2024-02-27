#!/usr/bin/env python

from setuptools import setup, find_packages

description = "Some simple dynamical systems implemented in python"
version="0.0.1"

setup(name="dynamical_systems",
    version=version,
    description=description,
    url="https://github.com/Chris-Pedersen/dynamical_systems",
    author="Chris Pedersen",
    author_email="c.pedersen@nyu.edu",
    packages=find_packages(),
    )
