#!/usr/bin/env python3
import sys #if we want sys.argv
import re #if we want reg expressions
import subprocess #if we want to run command lines from python

recent = subprocess.run(['ls','-ltrh'], stdout=subprocess.PIPE)
oops = subprocess.check_call(['ls','-ltrh'])
if oops == 0:
    print(f'everything is ok')
else:
    exit(1)

bytes = recent.stdout
stdout = bytes.decode('utf-8')
lines = stdout.splitlines()
recent_line = lines[-1]
recent_info = subprocess.run(['awk '], stdout=subprocess.PIPE)
print(lines[-1])

