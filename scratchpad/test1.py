
# copy C:\work\IfxPy\IfxPy\IfxPyDbi.py C:\Dev\Anaconda3\lib\site-packages\ifxpy-3.0.3-py3.7-win-amd64.egg\IfxPyDbi.py

from sqlalchemy import create_engine
from sqlalchemy.dialects import registry

# import IfxPyDbi as dbapi2

registry.register("informix",        "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.IfxPy",  "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.pyodbc", "IfxAlchemy.pyodbc", "IfxDialect_pyodbc")

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=xxxxx;"
ConStr = 'informix://informix:xxxxx@127.0.0.1:9088/db1;SERVER=ids0'
engine = create_engine(ConStr)

connection = engine.connect()
# result = connection.execute("select username from users")
# for row in result:
#     print("username:", row['username'])
# connection.close()
print( "Done2" )

