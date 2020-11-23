### IfxAlchemy
The InformixAlchemy adapter provides a SQLAlchemy interface to Informix database

Please note that this project is still under active development. Please report any bugs in the issue tracker

Example:

from sqlalchemy import create_engine
from sqlalchemy.dialects import registry
from sqlalchemy.orm import sessionmaker

#import IfxPyDbi as dbapi2

registry.register("informix",        "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.IfxPy",  "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.pyodbc", "IfxAlchemy.pyodbc", "IfxDialect_pyodbc")

from sqlalchemy import MetaData, Table, Column, Integer

ConStr = 'informix://<username>:<password>@<machine name>:<port number>/<database name>;SERVER=<server name>'
engine = create_engine(ConStr)

connection = engine.connect()

connection.execute("drop table if exists employee");
connection.execute("create table employee (id int, fname varchar(20), lname varchar(20), salary money, purchase DATE )")
connection.execute("insert into employee values(1, 'Sheetal', 'J',  20100.19, 2019-02-02 )")
connection.execute("insert into employee values(2, 'Joe', 'T',  20111.19, 2019-11-023 )")
connection.execute("update employee set id=200 where id=2 ")
result = connection.execute("select * from employee")


for row in result:
     print("id:", row[0])
     print("fName:", row[1])
     print("lname:", row[2])
     print("Salary:", row[3])
     print("Purchase:", row[4])

connection.close()
print( "Done2" )


### Current state 
Ready for use


### To install Informix Alchemy from source
```bash
# Standard Python setup should be used
cd InformixAlchemy
# rm -rf build 

python  setup.py  build
python  setup.py  install
```

### Try
```bash
cd InformixAlchemy\scratchpad
python test1.py
```
