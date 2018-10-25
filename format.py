import sys
import os
import re
import time

debug = False
command = "{}"


def pathToWSL(path):
    path = re.sub('([A-Za-z]):[/|\\\\]', "/mnt/\\1/", path)
    path = re.sub('\\\\', '/', path)

    if path[0:2] == '[[':
        path = "<'" + path[2:]+"'"
    elif path[0:2] == ']]':
        path = ">'" + path[2:]+"'"
    elif path[0] != '-':bash
        path = "'" + path + "'"
  
    return path


def pathToWindows(path):
    path = re.sub('/mnt/([A-Za-z])/', "\\1:/", path)
    return path


class Log():
    content = ""

    def write(self, text):
        self.content += str(text) + "\n"

    def save(self):
        self.content = time.strftime("%Y-%m-%d %H:%M:%S") + "\n" + self.content
        with open("wsl.log", "a") as f:
            f.write(self.content)


if __name__ == "__main__":
    args = []
    for arg in sys.argv:
        args.append(pathToWSL(arg))
    com = " ".join(args[1:])

    if debug:
        log = Log()
        log.write(sys.argv)
        log.write(args)
        log.write('bash -c "' + (command if command != "run" else "") + " " + com + '"')
        log.save()

    out = os.popen('bash -c "' + (command if command != "run" else "") + " " + com + '"').read()

    print(pathToWindows(out))
