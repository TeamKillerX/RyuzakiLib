#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
import re
from shutil import rmtree

from setuptools import find_packages, setup, Command

with open("RyuzakiLib/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]


with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        self.status('installation requirements..')
        os.system('pip3 install -e .')

        self.status('Minimally you should create a Source Distribution:...')
        os.system('python3 setup.py sdist')

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('python3 setup.py bdist_wheel --universal')

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(version))
        os.system('git push --tags')

        sys.exit()

setup(
    name="RyuzakiLib",
    version=version,
    description="RyuzakiLib Powerfull base on Pyrogram",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="TeamKillerX",
    author_email="killerx@randydev.my.id",
    python_requires="~=3.9, ~=3.10",
    url="https://github.com/TeamKillerX/RyuzakiLib/",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    test_suite="setup.my_test_suite",

    install_requires=requires,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
