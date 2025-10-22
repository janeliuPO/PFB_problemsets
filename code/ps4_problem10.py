#!/usr/bin/env python3
import sys

min = int(sys.argv[1])
max = int(sys.argv[2])
range(min,max)
list_user = list(range(min,max))
for num in list_user:
    print(num)