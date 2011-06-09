#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author:        alisue
# date:            2011/03/22
#
from setuptools import setup, find_packages

version = "0.1rc2"

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
        name="uamd",
        version=version,
        description = "User Agent Mobile Detect",
        long_description=read('README.mkd'),
        classifiers = [
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP',
        ],
        keywords = "mobile detect HTTP_USER_AGENT user_agent",
        author = "Alisue",
        author_email = "lambdalisue@hashnote.net",
        url=r"https://github.com/lambdalisue/uamd",
        download_url = r"https://github.com/lambdalisue/uamd/tarball/master",
        license = 'BSD',
        packages = find_packages(),
        #include_package_data = True,
        zip_safe = True,
        install_requires=['setuptools', 'IPy', 'BeautifulSoup'],
)

