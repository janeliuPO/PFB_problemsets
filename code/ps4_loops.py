#!/usr/bin/env python3
import sys

count = 1
while count < 101:
    print(count)
    count+=1
print("Done")

 #this should bring out the numbers 1 to 100

count = 0
count_sum = 0
while count < 100:
    count = count + 1
    count_sum = count_sum + count

print(count_sum)

#this sums the numbers between 0 and 100

count = 11
factorial = 1
while count > 1:
    count = count - 1
    factorial = factorial * count
print(factorial)
