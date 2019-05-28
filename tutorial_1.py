#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:01:25 2019
@author: manish
"""

spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

print(type(spam_amount))
print(type(19.95))

#a / b 	True division 	Quotient of a and b, true division always gives float
#a // b 	Floor division 	Quotient of a and b, removing fractional parts
#a ** b 	Exponentiation 	a raised to the power of b
#Order of numeric operations (PEMDAS)-Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.


print(min(1, 2, 3))
print(max(1, 2, 3))

print(abs(32))
print(abs(-32))


print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

# Following will throw an exception
#ValueError: invalid literal for int() with base 10: '5f'
#print(int('5f') + 1)




def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


def least_difference_noreturn(a, b, c):
    """Don't return anything, the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)

help(least_difference)
print(least_difference(1, 10, 100),least_difference(1, 10, 10),least_difference(5, 6, 7),) # Python allows trailing commas in argument lists. How nice is that?)
print(least_difference_noreturn(1, 10, 100),least_difference_noreturn(1, 10, 10),least_difference_noreturn(5, 6, 7),) # Python allows trailing commas in argument lists. How nice is that?)


print(1, 2, 3, sep=' < ')
print(1, 2, 3, sep=',')
print(1, 2, 3)



def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")


def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)




#Functions that operate on other funcitons are called "Higher order functions." You probably won't write your own for a little while. But there are higher order functions built into Python that you might find useful to call.
#Here's an interesting example using the max function.
#By default, max returns the largest of its arguments. But if we pass in a function using the optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax').
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)


def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
#    pass
    return round(num,2)

print(round_to_two_places(3.14159))


print("Output of rounding")
print(round(1333.14157,1))
print(round(1333.14157,0))
print(round(1333.14157,-1))
print(round(1333.14157,-2))

## bool
x = True
print(x)
print(type(x))


#Python adopts the if and else often used in other languages; its more unique keyword is elif, a contraction of "else if". In these conditional clauses, elif and else blocks are optional; additionally, you can include as many elif statements as you would like.
#Note especially the use of colons (:) and whitespace to denote separate blocks of code. This is similar to what happens when we define a function - the function header ends with :, and the following line is indented with 4 spaces. All subsequent indented lines belong to the body of the function, until we encounter an unindented line, ending the function definition.
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)


print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"


def quiz_message(grade):
    outcome = 'failed' if grade < 50 else 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)
    
quiz_message(45)
quiz_message(75)



def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return True if int(ketchup) + int(mustard) + int(onion) == 1 else False

print('exactly_one_topping',exactly_one_topping(False,False,False))