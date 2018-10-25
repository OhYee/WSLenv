import multiprocessing
import os
import time

buildList = [
    "run", "git", "gcc", "g++", "python", "pylint", "autopep8", "rm", "ll", "ls",
    "jaotc", "jarsigner", "javac", "javap", "jconsole", "jdeprscan", "jhsdb",
    "jinfo", "jlink", "jmod", "jrunscript", "jstack", "jstatd", "pack200",
    "rmid", "serialver", "jar", "java", "javadoc", "jcmd", "jdb", "jdeps",
    "jimage", "jjs", "jmap", "jps", "jshell", "jstat", "keytool", "rmic",
    "rmiregistry", "unpack200"
 ]


def compile_exe(exe,fmt):
    print(exe, "start")
    with open(exe+".py", "w") as f:
        f.write(fmt.format(exe))
    os.system("pyinstaller -F " + exe + ".py")
    os.remove(exe+".py")
    os.remove(exe+".spec")
    print(exe, "finish")


if __name__ == '__main__':
    fmt = ""
    with open("format.py", "r") as f:
        fmt = f.read()

    p = multiprocessing.Pool()

    for exe in buildList:
        p.apply_async(compile_exe, args=(exe,fmt))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')
