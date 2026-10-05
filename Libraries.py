#import keyword is used to import modules in Python. It allows you to access functions, classes, and variables defined in other files or libraries.
"""
import random 

coin = random.choice(['Heads', 'Tails'])

print(f"The coin landed on: {coin}")
"""


# from is a keyword used to import specific functions, classes, or variables from a module. It allows you to access only the desired components without importing the entire module. 
# For example, you can use 'from math import sqrt' to directly access the sqrt() function without needing to prefix it with 'math.'.
"""
from random import choice

coin = choice(['Heads', 'Tails'])
print(f"The coin landed on: {coin}")
"""

# random.randint(a, b) is a function from the random module that returns a random integer between a and b (inclusive). It can be used to generate random numbers within a specified range.
"""
import random 

number = random.randint(1, 10)
print(f"The random number between 1 and 10 is: {number}")
"""

# random.shuffle() is a function from the random module that randomly shuffles the elements of a list in place. It modifies the original list and does not return a new list.

import random

songs = ['Song A', 'Song B', 'Song C', 'Song D']
random.shuffle(songs)
for song in songs:
    print(song)

"""

import statistics

statistics.mean([1, 2, 3, 4, 5])  # Returns the mean (average) of the list

"""
