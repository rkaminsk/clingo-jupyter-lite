from pyodide import JsException
try:
    import clingo
except JsException:
    print("exception!!!")
