# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='meta-reference',
    version=VERSION,
    author=u'Leslie Kepaletswe, Erik van Widenfelt',
    author_email='leslie.kep@gmail.com, ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/meta-trial/meta-reference',
    license='GPL license, see LICENSE',
    description='meta',
    long_description=README,
    zip_safe=False,
    keywords='django edc meta',
    install_requires=['edc_reference'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
