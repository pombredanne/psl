#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except:
    description = open('README.md').read()

setup(name="publicsuffixlist",
      version="0.2.7",
      packages=["publicsuffixlist",],
      package_data = {
          "publicsuffixlist": [
              "effective_tld_names.dat",
              "test_psl.txt",
          ]},
      author="ko-zu",
      author_email="causeless@gmail.com",
      description="publicsuffixlist implement",
      long_description=description,
      url="https://github.com/ko-zu/psl",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
          "Topic :: Internet :: Name Service (DNS)",
          "Topic :: Text Processing :: Filters",
          "Operating System :: OS Independent",
          
        ],
      )


