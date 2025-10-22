#!/usr/bin/env python3
import sys

min = int(sys.argv[1])
max = int(sys.argv[2])+1

list = [i for i in range(min,max) if i%2 != 0]
print(list)


