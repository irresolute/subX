try:
	from setuptools import setup ,find_packages
except ImportError:
	from distutils.core import setup , find_packages

from subX import __version__ #version number

def readFile(fName):
	with open(fName) as f:
		lines = f.read()
	return lines

setup(
	name = 'subX',
	version = __version__,
	author = 'Shashank Kumar',
	author_email = 'shashank.kumar.apc13@itbhu.ac.in',
	description = ('simple tool to download subtitles. '),
	long_description = open('README.rst').read(),
	license = 'MIT',
	keywords = 'subtitles download movies tv shows',
	url = 'http://github.com/irresolute/subX',
	packages = find_packages(),
	scripts =  ['bin/sub'],
	install_requires = ['requests','wxgtk2.8'],
	classifiers = [
				'Development Status :: 3 - Alpha',
				'Intended Audience :: Linux Users',
				'Programming Language :: Python :: 2.7'

				'Topic :: Utilities',
				'license :: OSI Approved :: MIT License',
	]
	)
