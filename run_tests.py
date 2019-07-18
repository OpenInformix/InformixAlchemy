from sqlalchemy.dialects import registry

registry.register("informix",        "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.IfxPy",  "IfxAlchemy.IfxPy", "IfxDialect_IfxPy")
registry.register("informix.pyodbc", "IfxAlchemy.pyodbc", "IfxDialect_pyodbc")

from sqlalchemy.testing import runner

runner.main()

