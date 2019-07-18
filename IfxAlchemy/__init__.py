
__version__ = '1.0.1'

from . import IfxPy, pyodbc, base


# default dialect
base.dialect = IfxPy.dialect

from .base import \
    BIGINT, BLOB, CHAR, CLOB, DATE, DATETIME, \
    DECIMAL, DOUBLE, DECIMAL,\
    GRAPHIC, INTEGER, INTEGER, LONGVARCHAR, \
    NUMERIC, SMALLINT, REAL, TIME, TIMESTAMP, \
    VARCHAR, VARGRAPHIC, dialect

#__all__ = (
    # TODO: (put types here)
#    'dialect'
#)
