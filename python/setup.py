import re
import os
import re
import sys

from glob import glob
from setuptools import setup, find_packages

SRC_FOLDER = '.'
PKG_NAME = 'spid_cie_oidc'

INSTALL_REQUIRES = [
    "Django",
    "cryptojwt",
    "pydantic",
    "pytz",
    "aiohttp",
    "requests",
    "pydantic[email]",
    #"djagger",
    "djagger@git+https://github.com/stefanmcds-mnt/djagger",
]

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()

with open(f'{SRC_FOLDER}{os.path.sep}{PKG_NAME}/__init__.py', 'r') as fd:
    VERSION = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE
    ).group(1)

LICENSE = "License :: OSI Approved :: Apache Software License"

setup(
    name=PKG_NAME,
    version=VERSION,
    description="SPID/CIE OIDC Federation Entity",
    long_description=README,
    long_description_content_type='text/markdown',
    author='STEFAN MCDS S.a.s.',
    author_email='info@stefan-mcds.it',
    license=LICENSE,
    url=f"https://github.com/stefanmcds-mnt/{PKG_NAME.replace('_', '-')}",
    packages=[PKG_NAME, ],
    package_dir={f"{PKG_NAME}": f"{SRC_FOLDER}/{PKG_NAME}"},

    package_data={
        f"{PKG_NAME}": [
            i.replace(
                f'{SRC_FOLDER}{os.path.sep}{PKG_NAME}{os.path.sep}', ''
            )
            for i in glob(
                f'{SRC_FOLDER}{os.path.sep}{PKG_NAME}{os.path.sep}**',
                recursive=True
            )
            if i and '__pycache__' not in i
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        LICENSE,
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
)
