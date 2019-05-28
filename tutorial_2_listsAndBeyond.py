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


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line


multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)


s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')
        
        
for i in range(5):
    print("Doing important work. i =", i)
    
    
i = 0
while i < 10:
    print(i, end=' ')
    i += 1


#List comprehensions
print('')
squares = []
for n in range(10):
    squares.append(n**2)
print(squares)


squares = [n**2 for n in range(10)]
print(squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)


# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)


print([32 for planet in planets])


def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])


print(count_negatives([-1,-2,-3,5,6,9,10,-100,-34]))


## List comparison, following will throw an error
#[1, 2, 3, 4] > 2

def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]


# Turns out that range(0) == range(-1) - they're both empty. So if meals has length 0 or 1, we just won't do any iterations of our for loop.
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for index in range(len(meals)-1):
        if meals[index] == meals[index+1]:
            return True
    return False





#In addition, Python's triple quote syntax for strings lets us include newlines literally (i.e. by just hitting 'Enter' on our keyboard, rather than using the special '\n' sequence). We've already seen this in the docstrings we use to document our functions, but we can use them anywhere we want to define a string.

triplequoted_hello = """hello
world"""
print(triplequoted_hello)


# Yes, we can even loop over them
print([char+'! ' for char in planet])

#['P! ', 'l! ', 'u! ', 't! ', 'o! ']

#But a major way in which they differ from lists is that they are immutable. We can't modify them.

#planet[0] = 'B'
# planet.append doesn't work either

#---------------------------------------------------------------------------
#TypeError                                 Traceback (most recent call last)
#<ipython-input-12-6ca42463b9f9> in <module>()
#----> 1 planet[0] = 'B'
#      2 # planet.append doesn't work either
#
#
#TypeError: 'str' object does not support item assignment


# ALL CAPS
claim = "Pluto is a planet!"
claim.upper()

'PLUTO IS A PLANET!'

# all lowercase
claim.lower()


#Going between strings and lists: .split() and .join()

#str.split() turns a string into a list of smaller strings, breaking on whitespace by default. This is super useful for taking you from one big string to a list of words.

words = claim.split()
print(words)




#Occasionally you'll want to split on something other than whitespace:

datestr = '1956-01-31'
year, month, day = datestr.split('-')

#str.join() takes us in the other direction, sewing a list of strings up into one long string, using the string it was called on as a separator.

print('/'.join([month, day, year]))

position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")



#This is getting hard to read and annoying to type. str.format() to the rescue.

print("{}, you'll always be the {}th planet to me.".format(planet, position))

#"Pluto, you'll always be the 9th planet to me."

#Notice how we didn't even have to call str() to convert position from an int. format() takes care of that for us.


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)





#Python has dictionary comprehensions with a syntax similar to the list comprehensions we saw in the previous tutorial.

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)


numbers = {'one':1, 'two':2, 'three':3}
for k in numbers:
    print("{} = {}".format(k, numbers[k]))
    
    
    

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
print(' '.join(sorted(planet_to_initial.values())))




#The very useful dict.items() method lets us iterate over the keys and values of a dictionary simultaneously. (In Python jargon, an item refers to a key, value pair)

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
    
    
#Your function should meet the following criteria

#- Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.” 
#- She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
#- Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.
 
def word_search(documents, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices





#Wouldn't it be great if we could refer to all the variables in the math module by themselves? i.e. if we could just refer to pi instead of math.pi or mt.pi? Good news: we can do that.

from math import *
print(pi, log(32, 2)













