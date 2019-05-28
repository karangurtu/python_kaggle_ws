#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:50:08 2019
@Description : Mostly about lists
@author: manish
"""

primes = [2, 3, 5, 7]


hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]

print(len(hands))

print(primes,hands)
print(type(primes))

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(planets[0])
print(planets[1:3]) # this is inclusive of start and exclusing of final index
print(planets[:3]) # starting 3 (0,1,2)
print(planets[3:]) #
print(planets[1:-1]) # Print all but first and last
print(planets[-3:]) # last 3 planets

print(planets[-3:6]) # print the saturn as it is the -3 from last and [5] not count vise, index wise, from beginning
print(planets[-3:-2]) # print saturn again


planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

planets[:4] = ['Mercury', 'Venus', 'Earth']
print(planets)

print(len(planets))

planets.append('Pluto')

print(planets)

print(planets.pop())

print(planets)

print(planets.index('Earth'))

# Following will throw an error :ValueError: 'Pluto' is not in list
#print(planets.index('Pluto'))

print("Earth" in planets)



#Tuples
#
#Tuples are almost exactly the same as lists. They differ in just two ways.

#1: The syntax for creating them uses parentheses instead of square brackets

t = (1, 2, 3)

t = 1, 2, 3 # equivalent to above
t

#(1, 2, 3)

#2: They cannot be modified (they are immutable).
#t[0] = 100


print(len(planets))


