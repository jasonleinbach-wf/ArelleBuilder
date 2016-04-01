from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["jdcal", "lxml", "openpyxl", "pg8000", "PyMySQL", "rdflib", "arelle", "dqc-us-rules", "pkutils"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(  name = "Arelle",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("arelle.CntlrWinMain.py")])
