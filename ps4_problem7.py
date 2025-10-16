#!/usr/bin/env python3
import sys

numbers = [101,2,15,22,95,33,2,27,72,15,52]
for number in numbers:
    if number%2 == 0: #use the == and after if statement, use colon
        print(number) #further indent this

sorted_numbers = sorted(numbers)

print(sorted_numbers)

sum_even = 0
for num in numbers:
    if num%2 == 0:
        sum_even = sum_even + num 


sum_odd = 0
for num in numbers:
    if num%2 != 0:
        sum_odd = sum_odd + num 

print(f'''Sum of even numbers: {sum_even:<0}'
Sum of odds: {sum_odd:<0}''')