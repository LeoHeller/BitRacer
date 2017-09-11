import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"
executables = [cx_Freeze.Executable("pineappleV2.pyw")]

cx_Freeze.setup(
    name="BitRacer",
    options={"build_exe": {"packages":["pygame","os"],
                           "include_files":["guy.png","road.png","trash.png"]}},
    executables = executables

    )