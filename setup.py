# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_biotime/__init__.py
from frappe_biotime import __version__ as version

setup(
	name='frappe_biotime',
	version=version,
	description='Intragrate frappe (ERPNext) with BioTime (ZKTech).',
	author='Mainul Islam',
	author_email='mainulkhan94@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
