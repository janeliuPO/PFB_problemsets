#!/usr/bin/env python3
import sys

janes_faves = {}

janes_faves['animal'] = 'bunnies'
janes_faves['dessert'] = 'pie'
janes_faves['vacay'] = 'beach'
janes_faves['person'] = 'greg'
janes_faves['organism'] = 'vibrio'
janes_faves['organism'] = sys.argv[1]

for thing in janes_faves:
    fave = janes_faves[thing]
    print(thing)

print('Enter a thing from the list above:')
x = input()
print("Jane's favorite", x , "is", janes_faves[x])
