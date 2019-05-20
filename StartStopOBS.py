#! /usr/bin/python
#https://kb.froglogic.com/download/attachments/10223762/obs_wrapper.py?version=1&modificationDate=1498577881000
#https://kb.froglogic.com/display/KB/Example+-+Recording+a+screen+movie+of+the+test+execution
import getpass
import os
import sys
import subprocess
import tempfile
import time

def main():
    if len(sys.argv) <= 1:
        print("Provide Valid Input")
        sys.exit(1)
    elif sys.argv[1] == "option 2":
        Option1()
    else:
        Option2()


def Option1():
    # For unixish systems:
    args = ["obs"]
    cwd = None
    # For Windows:
    if sys.platform == "win32":
        cwd = r"C:\Program Files (x86)\obs-studio\bin\64bit"
        args = [os.path.join(cwd, "obs64.exe")]
    args.append("--startrecording")
    args.append("--minimize-to-tray")
    p = subprocess.Popen(args=args, cwd=cwd 
                         # , stdout=subprocess.PIPE
                         # , stderr=subprocess.STDOUT
                         )
    print("OBS PID: %s" % p.pid)
    fn = os.path.join(tempfile.gettempdir(), "obs.%s.pid" % getpass.getuser())
    print("OBS PID file: %s" % fn)
    f = open(fn, "w")
    f.write("%s" % p.pid)
    f.close()

def Option2():
    fn = os.path.join(tempfile.gettempdir(), "obs.%s.pid" % getpass.getuser())
    if not os.path.exists(fn):
        print("OBS PID file does not exists: %s" % fn)
        sys.exit(2)
    print("OBS PID file: %s" % fn)
    f = open(fn, "r")
    pid = f.read()
    f.close()
    print("OBS PID: %s" % pid)
    # For unixish systems:
    args = ["kill", "%s" % pid]
    # For Windows:
    if sys.platform == "win32":
        args = ["taskkill", "/f", "/pid", "%s" % pid]
    subprocess.Popen(args=args).communicate()
    os.remove(fn)

if __name__ == "__main__":
    main()
