Informix Alchemy Adapter
========================

The Informix Alchemy adapter provides the Python/SQLAlchemy interface to Informix Servers.

Version
--------
x.x.x

Prerequisites
--------------
1. Python 3.5.x .
2. SQLAlchemy 0.7.3 or above.
3. IfxPy driver and IfxPyDbi

Install and Configuration
=========================
The Informix Alchemy Python Egg component (.egg) can be installed using the standard setuptools provided by the Python Easy Install through Python Enterprise
Application Kit community portal:
  http://peak.telecommunity.com/DevCenter/EasyInstall

Please follow the steps provided to Install "Easy Install" in the link above and follow up with these additional steps to install Informix Alchemy:

  1. To install Informix Alchemy from source
    Standard Python setup should be used::
        python setup.py build
        python setup.py install

Connecting
----------
A TCP/IP connection can be specified as the following::

	from sqlalchemy import create_engine

	e = create_engine("informix://user:pass@host[:port]/database")

For a local socket connection, exclude the "host" and "port" portions::

	from sqlalchemy import create_engine

	e = create_engine("informix://user:pass@/database")



Known Limitations in InfAlchemy  adapter for Informix databases
---------------------------------------------------------------
1) Non-standard SQL queries are not supported. e.g. "SELECT ? FROM TAB1"
2) For updations involving primary/foreign key references, the entries should be made in correct order. Integrity check is always on and thus the primary keys referenced by the foreign keys in the referencing tables should always exist in the parent table.
3) Unique key which contains nullable column not supported
4) UPDATE CASCADE for foreign keys not supported
5) DEFERRABLE INITIALLY deferred not supported
6) Subquery in ON clause of LEFT OUTER JOIN not supported


```

