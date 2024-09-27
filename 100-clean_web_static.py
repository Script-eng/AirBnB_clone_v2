#!/usr/bin/python3
# Deletes out of date archives

from fabric.api import *
import os

env.hosts = ['100.26.238.151', '100.25.183.127']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): Is the number of archive files to keep.
    If the number is 0 or 1, only keep the most recent archive. If
    number is 2, keep the most recent and second-most recent archives,
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
