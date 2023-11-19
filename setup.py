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


def my_test_suite():
    import unittest

    test_loader = unittest.TestLoader()
    return test_loader.discover("tests", pattern="test*.py")


with open("RyuzakiLib/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]


with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        self.status("installation requirements..")
        os.system("pip3 install -e .")

        self.status("Minimally you should create a Source Distribution:...")
        os.system("python3 setup.py sdist")

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("python3 setup.py bdist_wheel --universal")

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(version))
        os.system("git push --tags")

        sys.exit()


project_urls = {
    "Bug Tracker": "https://github.com/TeamKillerX/RyuzakiLib/issues",
    "Documentation": "https://docs.randydev.my.id/",
    "Source Code": "https://github.com/TeamKillerX/RyuzakiLib",
}

setup(
    name="RyuzakiLib",
    version=version,
    description="RyuzakiLib Powerfull base on Pyrogram",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="TeamKillerX",
    author_email="killerx@randydev.my.id",
    python_requires="~=3.7",
    url="https://github.com/TeamKillerX/RyuzakiLib/",
    project_urls=project_urls,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    test_suite="setup.my_test_suite",
    install_requires=requires,
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    cmdclass={
        "upload": UploadCommand,
    },
)
