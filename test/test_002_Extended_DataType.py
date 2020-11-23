# copy C:\work\IfxPy\IfxPy\IfxPyDbi.py C:\Dev\Anaconda3\lib\site-packages\ifxpy-3.0.3-py3.7-win-amd64.egg\IfxPyDbi.py

from sqlalchemy import create_engine
from sqlalchemy.dialects import registry

# import IfxPyDbi as dbapi2

registry.register("informix",        "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.IfxPy",  "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.pyodbc", "IfxAlchemy.pyodbc", "IfxDialect_pyodbc")

import IfxAlchemy.IfxPy
import IfxAlchemy.pyodbc

#ConStr = "SERVER=ol_informix1410_3;DATABASE=sqlal_test;HOST=njdc-ldev11.prod.hclpnp.com;SERVICE=8572;UID=informix;PWD=2wo4D8QA;"
ConStr = 'informix://informix:2wo4D8QA@njdc-ldev11.prod.hclpnp.com:8572/sqlal_test;SERVER=ol_informix1410_3'
engine = create_engine(ConStr)

connection = engine.connect()
connection.execute('drop table if exists t1911')
connection.execute('DROP ROW TYPE if exists udt_t4 RESTRICT')
connection.execute('create ROW type udt_t4 (a int)')
connection.execute('create table t1911(c1 int, c2 char(20), c3 float, c4 varchar(10), s1 SET(int not null), m1  MULTISET(int not null), l1 LIST(bigint not null), u udt_t4)')
#connection.execute('create table t1911(c1 int, c2 char(20), c3 float, c4 varchar(10), s1 SET(int not null), (ROW(201)::udt_t4) )')
connection.execute('insert into t1911 values(1, "Sheetal", 12.01, "Hello", set{11, 10}, multiset{22, 33}, list{10000, 20000}, (ROW(201)::udt_t4) )')
result = connection.execute('select * from  t1911')

for row in result:
    print("c1:", row[0])
    print("c2:", row[1])
    print("c3:", row[2])
    print("c4:", row[3])
    print("s1:", row[4])
    print("ms:", row[5])
    print("list:", row[6])
    print("udt:", row[7])
connection.close()
print( "Done2" )
