# -*- encoding: utf8 -*-
import os
import json
from setuptools import setup, find_packages


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

version_info = json.load(open(os.path.join(BASE_DIR, 'passconfig', 'version.json')))

setup(
    name='passconfig',
    version=version_info['version'],
    author=version_info['author'],
    author_email=version_info['author_email'],
    description='View/Highlight KEGG Pathway',
    long_description=open(os.path.join(BASE_DIR, 'README.md')).read(),
    long_description_content_type="text/markdown",
    url='https://github.com/suqingdong/passconfig',
    license='BSD License',
    install_requires=open(os.path.join(BASE_DIR, 'requirements.txt')).read().split(),
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'kegg_viewer = kegg_viewer.bin.main:main',
    ]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries'
    ]
)