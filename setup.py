# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)
README = open(os.path.join(here, 'README.rst')).read()

setup(
	name='PackageUtil',
	version='1.3',
	author='Philip Trauner',
	author_email='philip.trauner@aol.com',
	url='https://github.com/PhilipTrauner/PackageUtil',
	packages=find_packages(),
	description='Clean up and uninstall OS X packages with ease.',
	long_description=README,
	classifiers=[
		'Development Status :: 4 - Beta',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.3',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: MIT License',
		'Environment :: Console'
	],
	keywords='osx pkg remove forget',
	entry_points={
		'console_scripts': [
			'packageutil = PackageUtil.CLI:main',
		],
	}
)
