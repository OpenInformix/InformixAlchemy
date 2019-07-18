#!/usr/bin/env python

from setuptools import setup
import os
import re


v = open(os.path.join(os.path.dirname(__file__), 'IfxAlchemy', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.rst')
if 'USE_PYODBC' in os.environ and os.environ['USE_PYODBC'] == '1':
    require = ['sqlalchemy>=0.7.3']
else:
    require = ['sqlalchemy>=0.7.3','IfxPy>=3.0.3']


setup(
         name='IfxAlchemy',
         version=VERSION,
         license='Apache License 2.0',
         description='SQLAlchemy support for Informix Servers',
         author='OpenInformix Development Team',
         url='http://pypi.python.org/pypi/IfxAlchemy/',
         keywords='sqlalchemy database interface for Informix servers',
         long_description_content_type='text/markdown',
         classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache License 2.0',
            'Operating System :: OS Independent',
            'Topic :: Databases :: Front-end, middle-tier'
        ],
         long_description=open(readme).read(),
         platforms='All',
         install_requires= require,
         packages=['IfxAlchemy'],
        entry_points={
         'sqlalchemy.dialects': [
                     'ifx=IfxAlchemy.IfxPy:IfxDialect_IfxPy',
                     'ifx.IfxPy=IfxAlchemy.IfxPy:IfxDialect_IfxPy',
                     # older "IfxAlchemy://" style for backwards
                     # compatibility
                     'IfxAlchemy=IfxAlchemy.IfxPy:IfxDialect_IfxPy',
                     'IfxAlchemy.pyodbc=IfxAlchemy.pyodbc:IfxDialect_pyodbc',
                    ]
       },
       zip_safe=False,
       tests_require=['nose >= 0.11'],
     )
