#!/usr/bin/env Python
# System information gathering script 
import subprocess

cmd = "uname -a"
print "\nSystem information (%s):\n" % cmd
subprocess.call(cmd, shell=True)

cmd = "df -h"
print "\nDiskspace (%s):\n" % cmd
subprocess.call(cmd, shell=True)

