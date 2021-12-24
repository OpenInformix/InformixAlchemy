
from sqlalchemy import create_engine
from sqlalchemy.dialects import registry

# import IfxPyDbi as dbapi2

registry.register("informix",        "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.IfxPy",  "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.pyodbc", "IfxAlchemy.pyodbc", "IfxDialect_pyodbc")

import IfxAlchemy.IfxPy
import IfxAlchemy.pyodbc

ConStr = 'informix://<UserName>:<Password>@<HostName>:<Port Number>/<Database Name>;SERVER=<Server Name>'
engine = create_engine(ConStr)

connection = engine.connect()
connection.execute('drop table if exists t1911')
connection.execute('create table t1911(c1 int, c2 char(20), c3 float, c4 varchar(10))')
connection.execute("insert into t1911 values(1, 'Sheetal', 12.01, 'Hello')")
result = connection.execute('select * from  t1911')

for row in result:
    print("c1:", row[0])
    print("c2:", row[1])
    print("c3:", row[2])
    print("c4:", row[3])
connection.close()
print( "Done2" )
