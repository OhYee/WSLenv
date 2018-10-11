buildList = ["git", "gcc", "g++", "python",
             "pylint", "autopep8", "rm", "ll", "ls", ]

fmt = ""
with open("format.py", "r") as f:
    fmt = f.read()

import os
for exe in buildList:
    with open(exe+".py", "w") as f:
        f.write(fmt.format(exe))
    os.system("pyinstaller -F "+exe+".py")
    os.remove(exe+".py")
    os.remove(exe+".spec")
